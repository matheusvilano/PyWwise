from enum import IntEnum as _IntEnum, StrEnum as _StrEnum
from typing import Self as _Self


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
	"""Front left."""
	_FRONT_RIGHT = 0x2
	"""Front right."""
	_FRONT_CENTER = 0x4
	"""Front centre."""
	_LOW_FREQUENCY = 0x8
	"""Low-frequency."""
	_BACK_LEFT = 0x10
	"""Rear left."""
	_BACK_RIGHT = 0x20
	"""Rear right."""
	_BACK_CENTER = 0x100
	"""Rear centre."""
	_SIDE_LEFT = 0x200
	"""Side left."""
	_SIDE_RIGHT = 0x400
	"""Side right."""
	_TOP = 0x800
	"""Top centre."""
	_HEIGHT_FRONT_LEFT = 0x1000
	"""Front left."""
	_HEIGHT_FRONT_CENTER = 0x2000
	"""Front centre."""
	_HEIGHT_FRONT_RIGHT = 0x4000
	"""Front right."""
	_HEIGHT_BACK_LEFT = 0x8000
	"""Rear left."""
	_HEIGHT_BACK_CENTER = 0x10000
	"""Rear centre."""
	_HEIGHT_BACK_RIGHT = 0x20000
	"""Rear right."""
	
	LFE = _LOW_FREQUENCY
	"""0.1"""
	MONO = _FRONT_CENTER
	"""1.0"""
	
	STEREO = _FRONT_LEFT | _FRONT_RIGHT
	"""2.0"""
	STEREO_LFE = STEREO | LFE
	"""2.1"""
	
	TRI = STEREO | MONO
	"""3.0"""
	
	QUAD = STEREO | _SIDE_LEFT | _SIDE_RIGHT
	"""4.0"""
	
	_FIVE_ZERO = MONO | QUAD
	"""5.0"""
	FIVE_ONE = _FIVE_ZERO | LFE
	"""5.1"""
	FIVE_ONE_TWO = FIVE_ONE | _HEIGHT_FRONT_LEFT | _HEIGHT_FRONT_RIGHT
	"""5.1.2"""
	
	_SEVEN_ZERO = _FIVE_ZERO | _BACK_LEFT | _BACK_RIGHT
	"""7.0"""
	SEVEN_ONE = _SEVEN_ZERO | LFE
	"""7.1"""
	SEVEN_ONE_TWO = SEVEN_ONE | _HEIGHT_FRONT_LEFT | _HEIGHT_FRONT_RIGHT
	"""7.1.2"""
	SEVEN_ONE_FOUR = SEVEN_ONE | _HEIGHT_FRONT_LEFT | _HEIGHT_FRONT_RIGHT | _HEIGHT_BACK_LEFT | _HEIGHT_BACK_RIGHT
	"""7.1.4"""
	
	AMBISONICS_1ST = 0x0
	"""Ambisonics 1st order"""
	
	AMBISONICS_2ND = 0x0
	"""Ambisonics 2nd order"""
	
	AMBISONICS_3RD = 0x0
	"""Ambisonics 3rd order"""
	
	AMBISONICS_4TH = 0x0
	"""Ambisonics 4th order"""
	
	AMBISONICS_5TH = 0x0
	"""Ambisonics 5th order"""
	
	def get_name(self) -> str:  # _Self is not compatible with staticmethod.
		"""
		Gets the name of the speaker as shown in the docstring (documentation).
		:return: A string with the name of the speaker bit mask. If invalid, the returned string will contain "None".
		"""
		match self.value:
			case ESpeakerBitMask.LFE:
				return "0.1"
			case ESpeakerBitMask.MONO:
				return "1.0"
			case ESpeakerBitMask.STEREO:
				return "2.0"
			case ESpeakerBitMask.STEREO_LFE:
				return "2.1"
			case ESpeakerBitMask.TRI:
				return "3.0"
			case ESpeakerBitMask.QUAD:
				return "4.0"
			case ESpeakerBitMask._FIVE_ZERO:
				return "5.0"
			case ESpeakerBitMask.FIVE_ONE:
				return "5.1"
			case ESpeakerBitMask.FIVE_ONE_TWO:
				return "5.1.2"
			case ESpeakerBitMask._SEVEN_ZERO:
				return "7.0"
			case ESpeakerBitMask.SEVEN_ONE:
				return "7.1"
			case ESpeakerBitMask.SEVEN_ONE_TWO:
				return "7.1.2"
			case ESpeakerBitMask.SEVEN_ONE_FOUR:
				return "7.1.4"
			case ESpeakerBitMask.AMBISONICS_1ST:
				return "Ambisonics 1st order"
			case ESpeakerBitMask.AMBISONICS_2ND:
				return "Ambisonics 2nd order"
			case ESpeakerBitMask.AMBISONICS_3RD:
				return "Ambisonics 3rd order"
			case ESpeakerBitMask.AMBISONICS_4TH:
				return "Ambisonics 4th order"
			case ESpeakerBitMask.AMBISONICS_5TH:
				return "Ambisonics 5th order"


class EBasePlatform(_StrEnum):
    """An enumeration of all available base platforms."""
    
    ANDROID = "Android"
    """Android devices."""
    
    IOS = "iOS"
    """iOS devices."""
    
    LINUX = "Linux"
    """Linux devices."""
    
    MAC = "Mac"
    """macOS devices."""
    
    SWITCH = "Switch"
    """Nintendo Switch."""
    
    PS4 = "PS4"
    """Sony PlayStation 4."""
    
    PS5 = "PS5"
    """Sony PlayStation 5"""
    
    WINDOWS = "Windows"
    """Microsoft Windows"""
    
    XONE = "XboxOne"
    """Xbox One."""
    
    XSERIES = "XboxSeriesX"
    """Xbox Series (S and X)."""


class EBitDepth(_StrEnum):
	"""An enumeration of supported bit depths."""
	
	INT_16 = "int16"
	"""16-bit integer"""
	
	FLOAT_32 = "float32"
	"32-bit floating-point number."


class ESampleRate(_IntEnum):
	"""An enumeration of Sample Rates."""
	
	SR_48000 = 48000
	SR_44100 = 44100
	SR_36000 = 36000
	SR_32000 = 32000
	SR_28000 = 28000
	SR_24000 = 24000
	SR_22050 = 22050
	SR_20000 = 20000
	SR_18000 = 18000
	SR_16000 = 16000
	SR_14000 = 14000
	SR_12000 = 12000
	SR_11025 = 11025
	SR_10000 = 10000
	SR_8000 = 8000
	SR_6000 = 6000
	SR_3000 = 3000
	SR_2000 = 2000
	SR_1000 = 1000
	SR_500 = 500
	SR_300 = 300


class EWaveform(_StrEnum):
	"""An enumeration of the default waveforms available in Wwise."""
	
	SILENCE = "silence"
	SINE = "sine"
	TRIANGLE = "triangle"
	SQUARE = "square"
	WHITE_NOISE = "whiteNoise"
