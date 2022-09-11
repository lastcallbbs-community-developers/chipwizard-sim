from .models import *


__all__ = [
    "simulate_solution",
]


def flood_power(state: State):
    for _, cell in state.cells.items():
        cell.metal.powered = False
        cell.ntype.powered = False
        cell.ptype.powered = False
    for _, signal in state.signals.items():
        signal.output_value = False

    def flood(loc: Coords, layer: Layer):
        if loc.in_bounds():
            cell = state.cells[loc]
            lcell = cell.layer(layer)
            assert lcell
            if lcell.powered:
                return
            lcell.powered = True

            if cell.via:
                if cell.metal:
                    flood(loc, Layer.METAL_LAYER)
                if cell.ntype:
                    flood(loc, Layer.NTYPE_LAYER)
                if cell.ptype:
                    flood(loc, Layer.PTYPE_LAYER)

            if lcell.open:
                for d in lcell.connections:
                    flood(loc + d.delta(), layer)
        else:
            signal = state.signals[loc]
            assert layer == Layer.METAL_LAYER
            if signal.output_value:
                return
            signal.output_value = True

            for d in signal.connections:
                flood(loc + d.delta(), layer)

    for loc, signal in state.signals.items():
        if signal.type == SignalType.IN and signal.input_value:
            flood(loc, Layer.METAL_LAYER)


def simulate_solution(
    level: Level,
    solution: Solution,
    save_states: bool = False,
    save_substates: bool = False,
) -> SimulationResult:
    state = State.from_level_and_solution(level, solution)
    if save_states:
        states = [state.copy()]
    if save_substates:
        substates = [[state.copy()]]

    is_error = False

    signal_results = {
        loc: SignalResult(signal.name, signal.type, [], list(signal.values))
        for loc, signal in level.signals.items()
    }

    for tick in range(level.num_ticks):
        for loc, signal in level.signals.items():
            if signal.type == SignalType.IN:
                state.signals[loc].input_value = signal.values[tick]

        # Compute the gate state bitmask
        gate_state = sum(
            cell.tick_capacitor() << (loc.x * 5 + loc.y)
            for loc, cell in state.cells.items()
        )
        seen_gate_states = [gate_state]
        flood_power(state)
        if save_substates:
            cur_substates = [state.copy()]

        while True:
            next_gate_state = sum(
                cell.update_gates() << (loc.x * 5 + loc.y)
                for loc, cell in state.cells.items()
            )
            if next_gate_state == gate_state:
                break
            gate_state = next_gate_state

            if gate_state in seen_gate_states:
                is_error = True

            seen_gate_states.append(gate_state)
            flood_power(state)
            if save_substates:
                cur_substates.append(state.copy())

            if is_error:
                break

        if save_states:
            states.append(state.copy())
        if save_substates:
            substates.append(cur_substates)
        for loc, signal in state.signals.items():
            signal_results[loc].values.append(signal.output_value)

        if is_error:
            break

    is_correct = not is_error and all(
        signal.values == signal.target_values for _, signal in signal_results.items()
    )

    num_metal = 0
    num_ntype = 0
    num_ptype = 0
    num_capacitors = 0
    num_vias = 0
    num_npn_transistors = 0
    num_pnp_transistors = 0
    num_transistors = 0
    silicon_area = 0

    silicon_min_x, silicon_max_x = 6, -1
    silicon_min_y, silicon_max_y = 5, -1

    for loc, cell in solution.cells.items():
        cell.check()

        if cell.metal:
            num_metal += 1

        if cell.ntype:
            num_ntype += 1

        if cell.ptype:
            num_ptype += 1

        if cell.capacitor:
            num_capacitors += 1

        if cell.via:
            num_vias += 1

        if cell.is_transistor():
            num_transistors += 1
            if cell.n_on_top:
                num_pnp_transistors += 1
            else:
                num_npn_transistors += 1

        if cell.ntype or cell.ptype or cell.capacitor:
            silicon_area += 1
            silicon_min_x = min(silicon_min_x, loc.x)
            silicon_max_x = max(silicon_max_x, loc.x)
            silicon_min_y = min(silicon_min_y, loc.y)
            silicon_max_y = max(silicon_max_y, loc.y)

    silicon_volume = num_ntype + num_ptype + num_capacitors
    total_volume = silicon_volume + num_metal + num_vias

    silicon_width = max(silicon_max_x - silicon_min_x + 1, 0)
    silicon_height = max(silicon_max_y - silicon_min_y + 1, 0)
    silicon_size = silicon_width * silicon_height

    metrics = Metrics(
        is_correct=is_correct,
        is_error=is_error,
        num_metal=num_metal,
        num_bare_ntype = num_ntype - num_transistors,
        num_ntype = num_ntype,
        num_bare_ptype = num_ptype - num_transistors,
        num_ptype = num_ptype,
        num_capacitors=num_capacitors,
        num_vias=num_vias,
        num_npn_transistors=num_npn_transistors,
        num_pnp_transistors=num_pnp_transistors,
        num_transistors=num_transistors,
        silicon_area=silicon_area,
        silicon_volume=silicon_volume,
        total_volume=total_volume,
        silicon_width=silicon_width,
        silicon_height=silicon_height,
        silicon_size=silicon_size,
    )
    return SimulationResult(
        level=level,
        solution=solution,
        states=states if save_states else None,
        substates=substates if save_substates else None,
        signals=signal_results,
        metrics=metrics,
    )
