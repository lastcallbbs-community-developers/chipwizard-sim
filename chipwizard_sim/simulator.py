from copy import deepcopy

from .models import *


__all__ = ["simulate_step", "simulate_solution"]


def simulate_step(prv_state: State) -> State:
    nxt_state = deepcopy(prv_state)
    return nxt_state


def simulate_solution(level: Level, solution: Solution) -> SimulationResult:
    states = []

    num_metal = 0
    num_ntype = 0
    num_ptype = 0
    num_capacitors = 0
    num_vias = 0
    num_npn_transistors = 0
    num_pnp_transistors = 0
    num_transistors = 0
    num_silicon = 0

    silicon_min_x, silicon_max_x = 6, -1
    silicon_min_y, silicon_max_y = 5, -1

    for x in range(6):
        for y in range(5):
            cell = solution.cells[x][y]
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
                num_silicon += 1
                silicon_min_x = min(silicon_min_x, x)
                silicon_max_x = max(silicon_max_x, x)
                silicon_min_y = min(silicon_min_y, y)
                silicon_max_y = max(silicon_max_y, y)

    total_volume = num_silicon + num_metal + num_vias

    silicon_width = max(silicon_max_x - silicon_min_x + 1, 0)
    silicon_height = max(silicon_max_y - silicon_min_y + 1, 0)
    silicon_size = silicon_width * silicon_height

    metrics = Metrics(
        num_metal=num_metal,
        num_ntype=num_ntype,
        num_ptype=num_ptype,
        num_capacitors=num_capacitors,
        num_vias=num_vias,
        num_npn_transistors=num_npn_transistors,
        num_pnp_transistors=num_pnp_transistors,
        num_transistors=num_transistors,
        num_silicon=num_silicon,
        total_volume=total_volume,
        silicon_width=silicon_width,
        silicon_height=silicon_height,
        silicon_size=silicon_size,
    )
    return SimulationResult(
        level=level,
        solution=solution,
        states=states,
        metrics=metrics,
    )
