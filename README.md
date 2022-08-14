# ChipWizard Save File Parser + Simulator

A simple tool/library for parsing/validating solutions to ChipWizard™ Professional,
a subgame of [Last Call BBS](https://zachtronics.com/last-call-bbs/).

NOTE: This is a work in progress; no simulation is implemented, only static
analysis metrics.

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
