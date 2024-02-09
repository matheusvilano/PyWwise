from enum import IntEnum as _IntEnum


class EAkActionOnEventType(_IntEnum):
    STOP = 0
    PAUSE = 1
    RESUME = 2
    BREAK = 3
    RELEASE_ENVELOPE = 4


class EAkCurveInterpolation(_IntEnum):
    SINE = 0
    LOG1 = 1
    INV_S_CURVE = 2
    LINEAR = 3
    S_CURVE = 4
    EXP_1 = 5
    SINE_RECIP = 6
    EXP_3 = 7
    LAST_FADE_CURVE = 8
    CONSTANT = 9
