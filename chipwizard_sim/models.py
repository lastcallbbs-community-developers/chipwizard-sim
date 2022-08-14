from __future__ import annotations

from enum import Enum, unique
from dataclasses import dataclass
from typing import Optional


__all__ = [
    "Coords",
    "Direction",
    "CellComponent",
    "LayerCell",
    "Layer",
    "Cell",
    "Solution",
    "Signal",
    "SignalType",
    "SIGNAL_COORDS",
    "Level",
    "LayerCellState",
    "CellState",
    "State",
    "Metrics",
    "SignalResult",
    "SimulationResult",
]


@dataclass(eq=True, order=True, frozen=True)
class Coords:
    x: int
    y: int

    def in_bounds(self) -> bool:
        return 0 <= self.x < 6 and 0 <= self.y < 5

    def __add__(self, o: Coords) -> Coords:
        return Coords(self.x + o.x, self.y + o.y)


@unique
class Direction(Enum):
    RIGHT = 1
    UP = 2
    LEFT = 4
    DOWN = 8

    def opposite(self) -> Direction:
        return {
            Direction.RIGHT: Direction.LEFT,
            Direction.UP: Direction.DOWN,
            Direction.LEFT: Direction.RIGHT,
            Direction.DOWN: Direction.UP,
        }[self]

    def delta(self) -> Coords:
        if self == Direction.RIGHT:
            return Coords(+1, 0)
        elif self == Direction.UP:
            return Coords(0, +1)
        elif self == Direction.LEFT:
            return Coords(-1, 0)
        elif self == Direction.DOWN:
            return Coords(0, -1)
        else:
            assert False


@unique
class CellComponent(Enum):
    METAL = 1
    NTYPE = 2
    PTYPE = 4
    CAPACITOR = 8
    VIA = 16
    N_ON_TOP = 32


@dataclass
class LayerCell:
    exists: bool
    connections: set[Direction]

    def __bool__(self):
        return self.exists

    def check(self):
        if not self.exists:
            assert not self.connections


class Layer(Enum):
    METAL_LAYER = 0
    NTYPE_LAYER = 1
    PTYPE_LAYER = 2


@dataclass
class Cell:
    metal: LayerCell
    ntype: LayerCell
    ptype: LayerCell

    def layer(self, idx: Layer) -> LayerCell:
        return [self.metal, self.ntype, self.ptype][idx.value]

    capacitor: bool
    via: bool

    n_on_top: bool

    def is_transistor(self):
        return self.ntype and self.ptype

    def check(self):
        self.metal.check()
        self.ntype.check()
        self.ptype.check()

        if self.capacitor:
            # Capacitors can't overlap with silicon
            assert not self.ntype and not self.ptype

        if self.via:
            # Vias must go on raw ntype or ptype
            assert self.ntype or self.ptype
            assert not self.is_transistor()

        # Cannot have both ntype and ptype
        assert not (self.ntype.connections & self.ptype.connections)

        if self.is_transistor():
            base = self.ntype if self.n_on_top else self.ptype
            emi_col = self.ptype if self.n_on_top else self.ntype

            # Emitter/collector must have exactly 2 connections in opposite directions
            assert len(emi_col.connections) == 2 and sum(
                (d.delta() for d in emi_col.connections), Coords(0, 0)
            ) == Coords(0, 0)

            # Base must have at least one connection
            assert len(base.connections) >= 1


@dataclass
class Solution:
    cells: dict[Coords, Cell]
    selection: Optional[tuple[Coords, Coords]]
    save_string: Optional[str] = None

    def check(self):
        assert self.cells.keys() == {Coords(x, y) for x in range(6) for y in range(5)}
        for loc, cell in self.cells.items():
            cell.check()
            for layer in Layer:
                for d in cell.layer(layer).connections:
                    n_loc = loc + d.delta()
                    if n_loc.in_bounds():
                        assert (
                            d.opposite() in self.cells[n_loc].layer(layer).connections
                        )
                    else:
                        assert layer == Layer.METAL_LAYER and n_loc in SIGNAL_COORDS


class SignalType(Enum):
    IN = 0
    OUT = 1


@dataclass
class Signal:
    name: str
    type: SignalType
    values: list[bool]


SIGNAL_COORDS = [
    Coords(-1, 4),
    Coords(-1, 2),
    Coords(-1, 0),
    Coords(6, 4),
    Coords(6, 2),
    Coords(6, 0),
]


@dataclass
class Level:
    level_id: int
    level_name: str
    level_index: int  # for sorting

    num_ticks: int
    signals: dict[Coords, Signal]

    def __init__(
        self,
        level_id: int,
        level_name: str,
        level_index: int,
        signal_type: list[SignalType],
        signal_name: list[str],
        signal_values: list[list[int]],
    ):
        self.level_id = level_id
        self.level_name = level_name
        self.level_index = level_index
        assert len(signal_type) == len(signal_name) == len(signal_values) == 6
        self.num_ticks = len(signal_values[0])
        assert all(len(values) == self.num_ticks for values in signal_values)
        self.signals = {
            loc: Signal(name, type_, list(map(bool, values)))
            for loc, name, type_, values in zip(
                SIGNAL_COORDS,
                signal_name,
                signal_type,
                signal_values,
            )
        }


@dataclass
class LayerCellState:
    exists: bool
    connections: set[Direction]
    powered: bool = False
    open: bool = True

    def __bool__(self):
        return self.exists

    @classmethod
    def from_layer_cell(cls, layer_cell: LayerCell) -> LayerCellState:
        return cls(layer_cell.exists, layer_cell.connections)


@dataclass
class CellState:
    metal: LayerCellState
    ntype: LayerCellState
    ptype: LayerCellState

    def layer(self, idx: Layer) -> LayerCellState:
        return [self.metal, self.ntype, self.ptype][idx.value]

    capacitor: bool
    via: bool

    n_on_top: bool

    def is_transistor(self):
        return self.ntype and self.ptype

    def update_gates(self):
        if self.capacitor and self.metal:
            if not self.metal.powered:
                self.metal.open = False

        if self.is_transistor():
            if self.n_on_top:
                self.ptype.open = not self.ntype.powered
            else:
                self.ntype.open = self.ptype.powered

    def tick_capacitor(self):
        if self.capacitor and self.metal:
            self.metal.open = self.metal.powered

    @classmethod
    def from_cell(cls, cell: Cell) -> CellState:
        res = cls(
            metal=LayerCellState.from_layer_cell(cell.metal),
            ntype=LayerCellState.from_layer_cell(cell.ntype),
            ptype=LayerCellState.from_layer_cell(cell.ptype),
            capacitor=cell.capacitor,
            via=cell.via,
            n_on_top=cell.n_on_top,
        )
        res.update_gates()
        return res


@dataclass
class SignalState:
    name: str
    type: SignalType
    connections: set[Direction]

    input_value: bool = False
    output_value: bool = False

    @classmethod
    def from_signal(cls, signal: Signal) -> SignalState:
        return SignalState(signal.name, signal.type, set())


@dataclass
class State:
    cells: dict[Coords, CellState]
    signals: dict[Coords, SignalState]

    @classmethod
    def from_level_and_solution(cls, level: Level, solution: Solution) -> State:
        state = cls(
            cells={
                loc: CellState.from_cell(cell) for loc, cell in solution.cells.items()
            },
            signals={
                loc: SignalState.from_signal(signal)
                for loc, signal in level.signals.items()
            },
        )

        for loc, signal in state.signals.items():
            for d in Direction:
                n_loc = loc + d.delta()
                if (
                    n_loc.in_bounds()
                    and d.opposite() in state.cells[n_loc].metal.connections
                ):
                    signal.connections.add(d)

        return state

    def visualize(self) -> str:
        return ""


@dataclass
class Metrics:
    is_correct: bool
    is_error: bool

    # Counts of specific cell types
    # Note that num_ntype and num_ptype both count all transistors
    num_metal: int
    num_ntype: int
    num_ptype: int
    num_capacitors: int
    num_vias: int
    num_npn_transistors: int
    num_pnp_transistors: int

    # Aggregate statistics
    num_transistors: int
    num_silicon: int

    # Total of num_silicon + num_metal + num_vias
    total_volume: int

    silicon_width: int
    silicon_height: int
    silicon_size: int


@dataclass
class SignalResult:
    name: str
    type: SignalType

    values: list[bool]
    target_values: list[bool]


@dataclass
class SimulationResult:
    level: Level
    solution: Solution

    states: list[State]
    signals: dict[Coords, SignalResult]

    metrics: Metrics
