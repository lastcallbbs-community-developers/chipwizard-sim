# ChipWizard Save File Parser + Simulator

A simple tool/library for parsing/validating solutions to ChipWizard™ Professional,
a subgame of [Last Call BBS](https://zachtronics.com/last-call-bbs/).

NOTE: This is a work in progress; simulation is only lightly tested, though it
seems correct on some known edge cases.

## Usage

To validate and compute metrics for your own save file, use
```
python -m chipwizard_sim validate_all [--json] <save_file_path>
```
Save files are usually located at:
```
Windows: %USERPROFILE%\Documents\My Games\Last Call BBS\<user-id>\save.dat
Linux: $HOME/.local/share/Last Call BBS/<user-id>/save.dat
```
Alternatively, use `-` as the path to read from stdin.

To simulate/visualize a particular level, use
```
python -m chipwizard_sim simulate <level_name> <slot_number> <save_file_path>
```
Run `python -m chipwizard_sim` to see detailed format.

Sample output:

```
$ python -m chipwizard_sim simulate not-gate 0 ~/.local/share/Last\ Call\
BBS/7...5/save.dat
NOT Gate (Slot 0)
Metrics:
is_correct = True
is_error = False
num_metal = 8
num_bare_ntype = 1
num_ntype = 2
num_bare_ptype = 2
num_ptype = 3
num_capacitors = 0
num_vias = 3
num_npn_transistors = 0
num_pnp_transistors = 1
num_transistors = 1
silicon_area = 4
silicon_volume = 5
total_volume = 16
silicon_width = 2
silicon_height = 3
silicon_size = 6
footprint = 9

Solution:
┌───────────────────────────────────────────────────────┐
│                   ━ METAL     ═ SILICON               │
│         ┌─────┬─────┬─────┬─────┬─────┬─────┐         │
│         │     │     │     │     │     │     │         │
│     +V  │     │     │     │     │     │ M━━━━━ +V     │
│         │     │     │     │     │     │  ╲  │         │
│         │     │     │     │     │     │   P │         │
│         │     │     │     │     │     │   ║ │         │
│         ├─────┼─────┼─────┼─────┼─────┼───║─┤         │
│         │     │     │     │     │     │   ║ │         │
│         │     │     │     │     │ M   │   ║ │         │
│         │     │     │     │     │ ┃╲  │   P │         │
│         │     │     │     │     │ ┃ N═════N │         │
│         │     │     │     │     │ ┃   │   P │         │
│         ├─────┼─────┼─────┼─────┼─┃───┼───║─┤         │
│         │     │     │     │     │ ┃   │   ║ │         │
│   IN_A ━━━M━━━━━M━━━━━M━━━━━M━━━━━M   │ M━━━━━ OUT_X  │
│         │     │     │     │     │     │  ╲║ │         │
│         │     │     │     │     │     │   P │         │
│         │     │     │     │     │     │     │         │
│         ├─────┼─────┼─────┼─────┼─────┼─────┤         │
│         │     │     │     │     │     │     │         │
│         │     │     │     │     │     │     │         │
│         │     │     │     │     │     │     │         │
│         │     │     │     │     │     │     │         │
│         │     │     │     │     │     │     │         │
│         ├─────┼─────┼─────┼─────┼─────┼─────┤         │
│         │     │     │     │     │     │     │         │
│     +V  │     │     │     │     │     │     │  +V     │
│         │     │     │     │     │     │     │         │
│         │     │     │     │     │     │     │         │
│         │     │     │     │     │     │     │         │
│         └─────┴─────┴─────┴─────┴─────┴─────┘         │
│                                                       │
└───────────────────────────────────────────────────────┘
Final state:
┌───────────────────────────────────────────────────────┐
│                   ━ HIGH      ═ LOW                   │
│         ┌─────┬─────┬─────┬─────┬─────┬─────┐         │
│         │     │     │     │     │     │     │         │
│     +V  │     │     │     │     │     │ M━━━━━ +V     │
│         │     │     │     │     │     │  ╲  │         │
│         │     │     │     │     │     │   P │         │
│         │     │     │     │     │     │   ┃ │         │
│         ├─────┼─────┼─────┼─────┼─────┼───┃─┤         │
│         │     │     │     │     │     │   ┃ │         │
│         │     │     │     │     │ M   │   ┃ │         │
│         │     │     │     │     │ ║╲  │   P │         │
│         │     │     │     │     │ ║ N═════N │         │
│         │     │     │     │     │ ║   │   P │         │
│         ├─────┼─────┼─────┼─────┼─║───┼───┃─┤         │
│         │     │     │     │     │ ║   │   ┃ │         │
│   IN_A ═══M═════M═════M═════M═════M   │ M━━━━━ OUT_X  │
│         │     │     │     │     │     │  ╲┃ │         │
│         │     │     │     │     │     │   P │         │
│         │     │     │     │     │     │     │         │
│         ├─────┼─────┼─────┼─────┼─────┼─────┤         │
│         │     │     │     │     │     │     │         │
│         │     │     │     │     │     │     │         │
│         │     │     │     │     │     │     │         │
│         │     │     │     │     │     │     │         │
│         │     │     │     │     │     │     │         │
│         ├─────┼─────┼─────┼─────┼─────┼─────┤         │
│         │     │     │     │     │     │     │         │
│     +V  │     │     │     │     │     │     │  +V     │
│         │     │     │     │     │     │     │         │
│         │     │     │     │     │     │     │         │
│         │     │     │     │     │     │     │         │
│         └─────┴─────┴─────┴─────┴─────┴─────┘         │
│                                                       │
└───────────────────────────────────────────────────────┘

Signals:
+V: Correct
    Have: 11111111111111111111111111111111111111111111111111111111111
    Want: 11111111111111111111111111111111111111111111111111111111111
IN_A: Correct
    Have: 01001011010110111001011101110011111000110011111101001100010
    Want: 01001011010110111001011101110011111000110011111101001100010
+V: Correct
    Have: 11111111111111111111111111111111111111111111111111111111111
    Want: 11111111111111111111111111111111111111111111111111111111111
+V: Correct
    Have: 11111111111111111111111111111111111111111111111111111111111
    Want: 11111111111111111111111111111111111111111111111111111111111
OUT_X: Correct
    Have: 10110100101001000110100010001100000111001100000010110011101
    Want: 10110100101001000110100010001100000111001100000010110011101
+V: Correct
    Have: 11111111111111111111111111111111111111111111111111111111111
    Want: 11111111111111111111111111111111111111111111111111111111111
```

## Technical Notes

### Save file format

The relevant lines of `save.dat` are of the form
```
Volgograd.Solution.<LevelID>.<SaveSlot> = <SolutionString>
```
LevelID is the numeric ID of the level (see [this post](https://old.reddit.com/r/lastcallbbs/comments/wkgg96/comment/ijn4oo9/)).
SaveSlot is 0, 1, or 2 (0-indexed, unlike the game.)
SolutionString is is the binary solution file, zlib compressed and base64 encoded.

Credit to [yut23](https://github.com/yut23) for reverse engineering the binary
save format; see
<https://gist.github.com/yut23/5b6ded1b894b4b6f13ea26285b624f78> for a detailed
explanation.

Credit to [rolamni](https://www.reddit.com/u/rolamni) for transcribing the level files.
