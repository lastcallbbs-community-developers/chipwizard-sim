import sys

import argparse
import json
import dataclasses
from typing import Optional

from .models import *
from .savefile import *
from .levels import *
from .simulator import *


def get_level_from_name(level_name) -> Optional[Level]:
    level_name = level_name.strip().lower()
    for level in LEVELS:
        if level_name == level.level_name.lower():
            return level

    if "editor" in level_name:
        return LEVELS[-1]

    # Bonus level last names
    for level in LEVELS[15:29]:
        if level.level_name.split()[-1].lower() in level_name:
            return level

    # Try to parse 1-2, possibly with a leading "b" or "bonus"
    digits = [c for c in level_name if "0" <= c <= "9"]
    if len(digits) == 2:
        col, row = map(int, digits)
        return LEVELS[
            (15 if level_name.startswith("b") else 0) + (col - 1) * 3 + (row - 1)
        ]

    raise ValueError(f"Could not parse level name {level_name}")


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

    def run_validate_all(args):
        solutions = parse_save_file(args.save_file)

        json_result = []

        for level in LEVELS:
            for slot, solution in solutions[level.level_id].items():
                result = simulate_solution(level, solution)
                if args.json:
                    json_result.append(
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
                    )
                else:
                    print(f"{level.level_name} (Slot {slot})")
                    print(result.metrics)

        if args.json:
            print(json.dumps(json_result))

    parser_validate_all.set_defaults(func=run_validate_all)

    parser_simulate = subparsers.add_parser("simulate", help="Simulate one save")
    parser_simulate.add_argument(
        "level_name",
        type=get_level_from_name,
        help='Use "1-2" for the 2nd level in the 1st column of the base game, or "B4-3" for the 3rd level in the 4th column of the bonus levels, or a bonus level name (e.g. "Clark"). Use "B5-3" or "editor" for the puzzle editor.',
    )
    parser_simulate.add_argument(
        "slot_number",
        type=int,
        help="Use 0 for top-left, 1 for top-right, 2 for bottom-left, 3 for bottom-right",
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
            print(
                "Slot should be 0, 1, 2, or 3 for top-left, top-right, bottom-left, or bottom-right"
            )
            sys.exit(1)

        solution = solutions[level.level_id][slot]
        print(solution)
        result = simulate_solution(level, solution)
        print(f"{level.level_name} (Slot {slot})")
        print("Metrics:")
        for field in dataclasses.fields(Metrics):
            print(field.name, "=", getattr(result.metrics, field.name))

    parser_simulate.set_defaults(func=run_simulate)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
