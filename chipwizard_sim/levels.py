from .models import *


__all__ = ["LEVELS"]


LEVELS = [
    Level(
        level_id=2,
        level_name="Signal Crossover",
        level_index=0,
    ),
    Level(
        level_id=3,
        level_name="AND Gate",
        level_index=1,
    ),
    Level(
        level_id=1,
        level_name="OR Gate",
        level_index=2,
    ),
    Level(
        level_id=4,
        level_name="NOT Gate",
        level_index=3,
    ),
    Level(
        level_id=9,
        level_name="Power-on Reset",
        level_index=4,
    ),
    Level(
        level_id=22,
        level_name="Digital Signal Mixer",
        level_index=5,
    ),
    Level(
        level_id=12,
        level_name="Interrupt Controller",
        level_index=6,
    ),
    Level(
        level_id=13,
        level_name="Ignition Sequencer",
        level_index=7,
    ),
    Level(
        level_id=8,
        level_name="Equality Tester",
        level_index=8,
    ),
    Level(
        level_id=10,
        level_name="Dual Oscillator",
        level_index=9,
    ),
    Level(
        level_id=19,
        level_name="Safety Interlock",
        level_index=10,
    ),
    Level(
        level_id=11,
        level_name="PWM Solenoid Driver",
        level_index=11,
    ),
    Level(
        level_id=5,
        level_name="Electronic Lock",
        level_index=12,
    ),
    Level(
        level_id=7,
        level_name="Motor Controller",
        level_index=13,
    ),
    Level(
        level_id=20,
        level_name="Programmable Delay",
        level_index=14,
    ),
    Level(
        level_id=16,
        level_name="Synchrony Detector",
        level_index=15,
    ),
    Level(
        level_id=21,
        level_name="AND-OR Combo Gate",
        level_index=16,
    ),
    Level(
        level_id=15,
        level_name="Switch Debouncer",
        level_index=17,
    ),
    Level(
        level_id=17,
        level_name="Stepper Motor Driver",
        level_index=18,
    ),
    Level(
        level_id=14,
        level_name="Serial Number ROM",
        level_index=19,
    ),
    Level(
        level_id=18,
        level_name="Pulse Echo Detector",
        level_index=20,
    ),
]
assert all(i == level.level_index for i, level in enumerate(LEVELS))
