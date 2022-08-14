import base64
import zlib
from typing import Optional, cast

from .models import *
from .levels import LEVELS


__all__ = ["parse_solution", "dump_solution", "parse_save_file"]


def parse_solution(save_string: str) -> Solution:
    """parses a solution string"""
    dat = zlib.decompress(base64.b64decode(save_string, validate=True))

    def pop_int(b):
        nonlocal dat
        assert len(dat) >= b
        res = int.from_bytes(dat[:b], "little", signed=True)
        dat = dat[b:]
        return res

    # Version number
    version = pop_int(4)
    if version not in {1002}:
        raise ValueError(f"Unknown save file version {version}")

    def pop_cell_contents() -> Cell:
        components = pop_int(1)
        metal_connections = pop_int(1)
        ntype_connections = pop_int(1)
        ptype_connections = pop_int(1)
        cell = Cell(
            metal=LayerCell(
                bool(components & CellComponent.METAL.value),
                {d for d in Direction if metal_connections & d.value},
            ),
            ntype=LayerCell(
                bool(components & CellComponent.NTYPE.value),
                {d for d in Direction if ntype_connections & d.value},
            ),
            ptype=LayerCell(
                bool(components & CellComponent.PTYPE.value),
                {d for d in Direction if ptype_connections & d.value},
            ),
            capacitor=bool(components & CellComponent.CAPACITOR.value),
            via=bool(components & CellComponent.VIA.value),
            n_on_top=bool(components & CellComponent.N_ON_TOP.value),
        )
        cell.check()
        return cell

    cells: list[list[Optional[Cell]]] = [[None for _ in range(5)] for _ in range(6)]
    for y in range(5):
        for x in range(6):
            cells[x][y] = pop_cell_contents()

    has_selection = pop_int(1)
    assert has_selection in {0, 1}
    if has_selection:
        x = pop_int(4)
        y = pop_int(4)
        w = pop_int(4)
        h = pop_int(4)
        selection = (Coords(x, y), Coords(w, h))
    else:
        selection = None

    assert len(dat) == 0

    solution = Solution(
        cast(list[list[Cell]], cells), selection, save_string=save_string
    )
    solution.check()
    return solution


def dump_solution(solution: Solution) -> str:
    dat = b""

    def push_int(b, v):
        nonlocal dat
        dat += v.to_bytes(b, "little", signed=True)

    push_int(4, 1002)

    def push_cell_contents(cell: Cell):
        push_int(
            1,
            sum(
                [
                    (CellComponent.METAL.value if cell.metal else 0),
                    (CellComponent.NTYPE.value if cell.ntype else 0),
                    (CellComponent.PTYPE.value if cell.ptype else 0),
                    (CellComponent.CAPACITOR.value if cell.capacitor else 0),
                    (CellComponent.VIA.value if cell.via else 0),
                    (CellComponent.N_ON_TOP.value if cell.n_on_top else 0),
                ]
            ),
        )
        push_int(1, sum(d.value for d in cell.metal.connections))
        push_int(1, sum(d.value for d in cell.ntype.connections))
        push_int(1, sum(d.value for d in cell.ptype.connections))

    for y in range(5):
        for x in range(6):
            push_cell_contents(solution.cells[x][y])

    if solution.selection is not None:
        push_int(1, 1)
        push_int(4, solution.selection[0].x)
        push_int(4, solution.selection[0].y)
        push_int(4, solution.selection[1].x)
        push_int(4, solution.selection[1].y)
    else:
        push_int(1, 0)

    return base64.b64encode(zlib.compress(dat, level=9)).decode("ascii")


def parse_save_file(f) -> dict[int, dict[int, str]]:
    solutions = {level.level_id: {} for level in LEVELS}
    for line in f:
        line = line.rstrip("\n")
        if " = " in line:
            key, val = line.split(" = ")
            key = key.split(".")
            val = val.strip()
            if key[0] == "Volgograd" and key[1] == "Solution":
                level_id = int(key[2])
                save_slot = int(key[3])
                solutions[level_id][save_slot] = val
    return solutions
