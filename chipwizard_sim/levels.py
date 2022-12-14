from .models import *


__all__ = ["LEVELS"]


# fmt: off
LEVELS = [
    Level(
        level_id=2,
        level_name="Signal Crossover",
        level_index=0,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT, SignalType.IN, SignalType.OUT],
        signal_name=["IN_A", "+V", "IN_B", "OUT_B", "+V", "OUT_A"],
        signal_values=[
            [0,1,0,1,1,1,1,1,0,0,1,1,1,0,1,1,0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,0,0,0,0,1,1,1,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,1,1,1,1,0,0,0,1,0,0,1,1,1,1,1,0,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,0],
            [0,0,1,1,1,1,0,0,0,1,0,0,1,1,1,1,1,0,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,1,0,1,1,1,1,1,0,0,1,1,1,0,1,1,0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,0,0,0,1,0,0,0,0,1,1,1,0,0,0,1],
        ],
    ),
    Level(
        level_id=3,
        level_name="AND Gate",
        level_index=1,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT, SignalType.IN],
        signal_name=["IN_A", "+V", "IN_B", "+V", "OUT_X", "+V"],
        signal_values=[
            [1,0,0,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1,1,1,1,0,1,1,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,1,0,1,0,1,0,0,0,0,1,1,1,1,0,1,1,1,1,0,1,1,0,1,0,1,0,0,0,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,1,0,1,0,1,0,0,0,0,1,0,1,0,0,1,1,1,1,1,0,0,1,0,1,0,0,1,0,0,1,1,1,1,1,0,1,1,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ],
    ),
    Level(
        level_id=1,
        level_name="OR Gate",
        level_index=2,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT, SignalType.IN],
        signal_name=["IN_A", "+V", "IN_B", "+V", "OUT_X", "+V"],
        signal_values=[
            [0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,1,0,1,0,0,1,1,0,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,1,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,1,1,1,0,1,0,0,1,1,1,1,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ],
    ),
    Level(
        level_id=4,
        level_name="NOT Gate",
        level_index=3,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT, SignalType.IN],
        signal_name=["+V", "IN_A", "+V", "+V", "OUT_X", "+V"],
        signal_values=[
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,1,0,0,1,0,1,1,0,1,0,1,1,0,1,1,1,0,0,1,0,1,1,1,0,1,1,1,0,0,1,1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,0,1,0,0,1,1,0,0,0,1,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,1,1,0,1,0,0,1,0,1,0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,1,1,0,0,1,1,1,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ],
    ),
    Level(
        level_id=9,
        level_name="Power-on Reset",
        level_index=4,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT, SignalType.IN],
        signal_name=["+V", "+V", "+V", "+V", "RESET", "+V"],
        signal_values=[
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ],
    ),
    Level(
        level_id=22,
        level_name="Digital Signal Mixer",
        level_index=5,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT],
        signal_name=["IN_A", "IN_B", "IN_C", "IN_D", "+V", "OUT_X"],
        signal_values=[
            [0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1],
            [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0],
            [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,0,1,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,1,1,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,1,0,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,0,1,1,1,1,0,1],
        ],
    ),
    Level(
        level_id=12,
        level_name="Interrupt Controller",
        level_index=6,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT, SignalType.OUT, SignalType.OUT],
        signal_name=["IRQ_1", "IRQ_2", "IRQ_3", "OUT_1", "OUT_2", "OUT_3"],
        signal_values=[
            [0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,0],
            [0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,0,1,1,0,0,1,1,1,1,0,1,0,0,1,0,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,1,1,0,1,0,0,0,0,0,1,1,1,0,0],
            [1,0,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,0,1,1,1,1,0,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1],
            [0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,0],
            [0,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,1,1,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0],
            [1,0,0,0,0,1,0,0,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,0,1],
        ],
    ),
    Level(
        level_id=13,
        level_name="Ignition Sequencer",
        level_index=7,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT, SignalType.OUT, SignalType.OUT],
        signal_name=["+V", "RUN", "+V", "OUT_1", "OUT_2", "OUT_3"],
        signal_values=[
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
        ],
    ),
    Level(
        level_id=8,
        level_name="Equality Tester",
        level_index=8,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT, SignalType.IN],
        signal_name=["IN_A", "+V", "IN_B", "+V", "OUT_X", "+V"],
        signal_values=[
            [1,1,1,0,0,1,1,0,0,1,0,0,0,0,0,1,1,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,1,0,0,1,1,0,1,0,0,1,1,0,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,0,1,0,1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,1,1,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,1,0,1,1,1,1,0,0,1,0,1,1,1,0,0,1,0,0,0,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ],
    ),
    Level(
        level_id=10,
        level_name="Dual Oscillator",
        level_index=9,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT, SignalType.IN, SignalType.OUT],
        signal_name=["+V", "+V", "+V", "FAST", "+V", "SLOW"],
        signal_values=[
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1],
        ],
    ),
    Level(
        level_id=19,
        level_name="Safety Interlock",
        level_index=10,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT, SignalType.OUT, SignalType.OUT],
        signal_name=["IN_A", "+V", "IN_B", "OUT_A", "ALARM", "OUT_B"],
        signal_values=[
            [1,1,0,1,1,1,0,0,1,1,1,1,0,1,1,0,1,1,1,1,0,1,0,1,0,0,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1,0,1,1,1,1,1,1,0,1],
            [0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0],
            [1,1,0,1,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,1,0,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,0,1,1,0,1,1,1,1,1,1,0,1],
        ],
    ),
    Level(
        level_id=11,
        level_name="PWM Solenoid Driver",
        level_index=11,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT, SignalType.IN],
        signal_name=["+V", "HOLD", "+V", "+V", "COIL", "+V"],
        signal_values=[
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,0,1,1,1,1,0,1,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ],
    ),
    Level(
        level_id=5,
        level_name="Electronic Lock",
        level_index=12,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT],
        signal_name=["CODE_1", "CODE_2", "CODE_3", "CODE_4", "CODE_5", "OPEN"],
        signal_values=[
            [1,0,1,0,1,1,0,1,1,0,0,1,1,0,1,0,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,1,0,1,1,1,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0],
            [1,1,1,0,0,0,1,0,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1],
            [1,0,1,0,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,1,0,1,0,0,0,1,0,1,1,0,1,1,0,0,0,1,1,1],
            [0,0,1,1,0,0,0,1,1,0,1,0,1,1,0,0,0,1,0,0,0,0,1,0,0,1,1,0,1,0,0,0,0,1,1,0,0,1,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0],
            [1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,1,0,0,0,1,1,1,1,1,1,0,1,1,0,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,0,1,1,1,0],
            [0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
        ],
    ),
    Level(
        level_id=7,
        level_name="Motor Controller",
        level_index=13,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT, SignalType.IN],
        signal_name=["ON", "+V", "OFF", "+V", "MOTOR", "+V"],
        signal_values=[
            [0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,1,1,1,1,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,1,1,0,0,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ],
    ),
    Level(
        level_id=20,
        level_name="Programmable Delay",
        level_index=14,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT],
        signal_name=["TIME_3", "TIME_5", "TIME_8", "RUN", "+V", "ALARM"],
        signal_values=[
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0],
        ],
    ),
    Level(
        level_id=16,
        level_name="Synchrony Detector",
        level_index=15,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT, SignalType.IN],
        signal_name=["IN_A", "+V", "IN_B", "+V", "ALARM", "+V"],
        signal_values=[
            [0,1,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,1,0,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,0,0,1,0,1,1,0,1,0,1,0,0,1,1,0,0,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,1,0,0,0,1,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0,0,1,1,0,1,1,1,0,1,0,0,1,0,1,1,0,0,0,1,0,0,1,1,0,0,1,0,1,1,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ],
    ),
    Level(
        level_id=21,
        level_name="AND-OR Combo Gate",
        level_index=16,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT],
        signal_name=["IN_A", "+V", "IN_B", "GATE", "+V", "OUT_X"],
        signal_values=[
            [0,0,0,1,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,1,1,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,1,0,0,0,0,1,0,1,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,0,1,0,0,1,0,1,1,1,1,1,0,0,1,0,1,1,1,1,0,0,0,0,1,0,1,0,1],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,1,0,1,0,1,1,0,1,0,1,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,1,1,1,1,1,0,0,1,0,1,0,0,1,0,0,0,0,1,0,0,0,1],
        ],
    ),
    Level(
        level_id=15,
        level_name="Switch Debouncer",
        level_index=17,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT, SignalType.IN],
        signal_name=["+V", "NOISY", "+V", "+V", "CLEAN", "+V"],
        signal_values=[
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ],
    ),
    Level(
        level_id=17,
        level_name="Stepper Motor Driver",
        level_index=18,
        signal_type=[SignalType.IN, SignalType.OUT, SignalType.OUT, SignalType.OUT, SignalType.OUT, SignalType.IN],
        signal_name=["+V", "OUT_A+", "OUT_A-", "OUT_B+", "OUT_B-", "+V"],
        signal_values=[
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0],
            [0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1],
            [0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1],
            [1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ],
    ),
    Level(
        level_id=14,
        level_name="Serial Number ROM",
        level_index=19,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT, SignalType.IN],
        signal_name=["+V", "READ", "+V", "+V", "DATA", "+V"],
        signal_values=[
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,1,1,0,0,1,0,1,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,1,1,0,0,1,0,1,1,1,1,0,0,0,0,0,1,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ],
    ),
    Level(
        level_id=18,
        level_name="Pulse Echo Detector",
        level_index=20,
        signal_type=[SignalType.IN, SignalType.IN, SignalType.IN, SignalType.OUT, SignalType.IN, SignalType.OUT],
        signal_name=["PULSE", "+V", "RESET", "OUT_1", "+V", "OUT_2"],
        signal_values=[
            [0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0],
            [0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0],
        ],
    ),
]
# fmt: on
assert all(i == level.level_index for i, level in enumerate(LEVELS))
