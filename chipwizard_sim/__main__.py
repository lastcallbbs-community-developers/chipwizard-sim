import sys

import argparse
import contextlib
import json
import dataclasses
from typing import Optional
import multiprocessing

from .models import *
from .savefile import *
from .levels import *
from .simulator import *


def get_level_from_name(level_name) -> Optional[Level]:
    # Check case-insensitive without punctuation/spaces
    def normalize_name(s):
        return "".join(c for c in s.lower() if "a" <= c <= "z")

    level_name_norm = normalize_name(level_name)
    for level in LEVELS:
        if level_name_norm == normalize_name(level.level_name):
            return level

    raise ValueError(f"Could not parse level name {level_name!r}")


def process_solution(
    inp: tuple[Level, int, str]
) -> tuple[Level, int, Solution, SimulationResult]:
    level, slot, save_string = inp
    solution = parse_solution(save_string)
    # assert dump_solution(solution) == save_string
    result = simulate_solution(level, solution)
    return level, slot, solution, result


def main():
    parser = argparse.ArgumentParser(
        prog="python -m chipwizard_sim", description="Simulate ChipWizard solutions"
    )
    subparsers = parser.add_subparsers()

    parser_validate_all = subparsers.add_parser(
        "validate_all", help="Validate all solutions in a save file"
    )
    parser_validate_all.add_argument(
        "save_file", type=argparse.FileType(), help="Save file path (or - for stdin)"
    )
    parser_validate_all.add_argument(
        "--json", action="store_true", help="Use JSON output mode"
    )
    parser_validate_all.add_argument(
        "--include-solution", action="store_true", help="Include the solution save"
    )
    parser_validate_all.add_argument(
        "--max-parallelism",
        type=int,
        help="Maximum number of threads/processes to use (default 8)",
        default=8,
    )

    def run_validate_all(args):
        solutions = parse_save_file(args.save_file)

        json_result = []

        with (multiprocessing.Pool(args.max_parallelism) if args.max_parallelism > 1 else contextlib.nullcontext()) as pool:
            results = (pool.imap if pool is not None else map)(
                process_solution,
                (
                    (level, slot, save_string)
                    for level in LEVELS
                    for slot, save_string in solutions[level.level_id].items()
                ),
            )
            if args.json:
                json_result = [
                    dict(
                        level_name=level.level_name,
                        level_id=level.level_id,
                        **(
                            dict(solution=solution.save_string)
                            if args.include_solution
                            else {}
                        ),
                        **dataclasses.asdict(result.metrics),
                    )
                    for level, slot, solution, result in results
                ]
                print(json.dumps(json_result))
            else:
                for level, slot, solution, result in results:
                    print(f"{level.level_name} (Slot {slot})\n{result.metrics}")

    parser_validate_all.set_defaults(func=run_validate_all)

    parser_simulate = subparsers.add_parser("simulate", help="Simulate one save")
    parser_simulate.add_argument(
        "level_name",
        type=get_level_from_name,
        help="Use the string name from the game (case-insensitive)",
    )
    parser_simulate.add_argument(
        "slot_number",
        type=int,
        help="Slot number, 0-indexed (unlike in the game)",
    )
    parser_simulate.add_argument(
        "save_file", type=argparse.FileType(), help="Save file path (or - for stdin)"
    )

    def run_simulate(args):
        solutions = parse_save_file(args.save_file)
        level = args.level_name
        slot = args.slot_number
        if slot not in solutions[level.level_id]:
            print(f"No solution in slot {slot} for level {level.level_name}")
            print("Slot should be 0, 1, or 2 (unlike in the game)")
            sys.exit(1)

        save_string = solutions[level.level_id][slot]
        solution = parse_solution(save_string)
        result = simulate_solution(level, solution, save_states=True, save_substates=True)
        print(f"{level.level_name} (Slot {slot})")
        print("Metrics:")
        for field in dataclasses.fields(Metrics):
            print(field.name, "=", getattr(result.metrics, field.name))
        print()
        print("Solution:")
        print(solution.visualize(level))
        print("Final state:")
        assert result.states is not None
        print(result.states[-1].visualize())
        print()
        print("Signals:")
        for _, signal in result.signals.items():
            print(
                f"{signal.name}: {'Correct' if signal.values == signal.target_values else 'Incorrect'}"
            )
            print("    Have:", "".join("01"[v] for v in signal.values))
            print("    Want:", "".join("01"[v] for v in signal.target_values))

    parser_simulate.set_defaults(func=run_simulate)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
