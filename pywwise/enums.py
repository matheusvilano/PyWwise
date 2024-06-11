from enum import IntEnum as _IntEnum


class EActionOnEventType(_IntEnum):
    """Enumeration of available actions to be executed on an event (see `ak.soundengine.execute_action_on_event`)."""
    
    STOP = 0
    PAUSE = 1
    RESUME = 2
    BREAK = 3
    RELEASE_ENVELOPE = 4


class ECurveInterpolation(_IntEnum):
    """Enumeration of available curves for interpolation."""
    
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


class ESpeakerBitMask(_IntEnum):
    """Enumeration of common speaker bit masks."""
    
    _FRONT_LEFT = 0x1
    """Front left speaker bit mask"""
    _FRONT_RIGHT = 0x2
    """Front right speaker bit mask"""
    _FRONT_CENTER = 0x4
    """Front center speaker bit mask"""
    _LOW_FREQUENCY = 0x8
    """Low-frequency speaker bit mask"""
    _BACK_LEFT = 0x10
    """Rear left speaker bit mask"""
    _BACK_RIGHT = 0x20
    """Rear right speaker bit mask"""
    _BACK_CENTER = 0x100
    """Rear center speaker ("surround speaker") bit mask"""
    _SIDE_LEFT = 0x200
    """Side left speaker bit mask"""
    _SIDE_RIGHT = 0x400
    """Side right speaker bit mask"""
    _TOP = 0x800
    """Top speaker bit mask"""
    _HEIGHT_FRONT_LEFT = 0x1000
    """Front left speaker bit mask"""
    _HEIGHT_FRONT_CENTER = 0x2000
    """Front center speaker bit mask"""
    _HEIGHT_FRONT_RIGHT = 0x4000
    """Front right speaker bit mask"""
    _HEIGHT_BACK_LEFT = 0x8000
    """Rear left speaker bit mask"""
    _HEIGHT_BACK_CENTER = 0x10000
    """Rear center speaker bit mask"""
    _HEIGHT_BACK_RIGHT = 0x20000
    """Rear right speaker bit mask"""
    
    LFE = _LOW_FREQUENCY
    """0.1"""
    MONO = _FRONT_CENTER
    """1.0"""
    STEREO = _FRONT_LEFT | _FRONT_RIGHT
    """2.0"""
    QUAD = STEREO | _SIDE_LEFT | _SIDE_RIGHT
    """4.0"""
    FIVE_ZERO = MONO | QUAD
    """5.0"""
    FIVE_ONE = FIVE_ZERO | LFE
    """5.1"""
    SEVEN_ZERO = FIVE_ZERO | _BACK_LEFT | _BACK_RIGHT
    """7.0"""
    SEVEN_ONE = SEVEN_ZERO | LFE
    """7.1"""
    SEVEN_ONE_FOUR = SEVEN_ONE | _HEIGHT_FRONT_LEFT | _HEIGHT_FRONT_RIGHT | _HEIGHT_BACK_LEFT | _HEIGHT_BACK_RIGHT
    """7.1.4"""
