# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from typing import Self as _Self
from enum import Enum as _Enum, IntEnum as _IntEnum, StrEnum as _StrEnum


class EActionOnEventType(_IntEnum):
	"""Enumeration of available actions to be executed on an event (see `ak.soundengine.execute_action_on_event`)."""
	
	STOP = 0
	"""Stop"""
	
	PAUSE = 1
	"""Pause"""
	
	RESUME = 2
	"""Resume"""
	
	BREAK = 3
	"""Break"""
	
	RELEASE_ENVELOPE = 4
	"""Release Envelope"""


class EFadeCurve(_IntEnum):
	"""Enumeration of available curves for interpolation."""
	
	SINE = 0
	"""y = sin((PI/2)x)"""
	
	LOG1 = 1
	"""y = log2(1+x)"""
	
	INV_S_CURVE = 2
	"""y = 1 - (1-x)^2"""
	
	LINEAR = 3
	"""y = x"""
	
	S_CURVE = 4
	"""y = x^2 * (3-2x)"""
	
	EXP_1 = 5
	"""y = x^2"""
	
	SINE_RECIP = 6
	"""y = 1 - sin((PI/2)(1-x))"""
	
	EXP_3 = 7
	"""y = x^3"""
	
	_LAST_FADE_CURVE = 8
	"""y = last used function"""
	
	CONSTANT = 9
	"""y = 1"""


class EAttenuationCurveShape(_StrEnum):
	"""Enumeration of available curve shapes. Usually used with functions related to attenuation curves."""
	
	CONSTANT = "Constant"
	"""Constant value."""
	
	LINEAR = "Linear"
	"""Linear relationship."""
	
	LOG_1 = "Log1"
	"""Logarithmic curve."""
	
	LOG_2 = "Log2"
	"""Steeper logarithmic curve."""
	
	LOG_3 = "Log3"
	"""Steepest logarithmic curve."""
	
	S_CURVE = "SCurve"
	"""S-shaped curve."""
	
	INVERTED_S_CURVE = "InvertedSCurve"
	"""Inverted s-shaped curve."""
	
	EXPONENTIAL_1 = "Exp1"
	"""Exponential curve."""
	
	EXPONENTIAL_2 = "Exp2"
	"""Steeper exponential curve."""
	
	EXPONENTIAL_3 = "Exp3"
	"""Steepest exponential curve."""


class ESpeakerBitMask(_IntEnum):
	"""Enumeration of common speaker bit masks."""
	
	NONE = 0x0
	"""No output."""
	
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
	
	def get_name(self) -> str:
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
	"""48kHz"""
	
	SR_44100 = 44100
	"""44.1kHz"""
	
	SR_36000 = 36000
	"""36kHz"""
	
	SR_32000 = 32000
	"""32kHz"""
	
	SR_28000 = 28000
	"""28kHz"""
	
	SR_24000 = 24000
	"""24kHz"""
	
	SR_22050 = 22050
	"""22.05kHz"""
	
	SR_20000 = 20000
	"""20kHz"""
	
	SR_18000 = 18000
	"""18kHz"""
	
	SR_16000 = 16000
	"""16kHz"""
	
	SR_14000 = 14000
	"""14kHz"""
	
	SR_12000 = 12000
	"""12kHz"""
	
	SR_11025 = 11025
	"""11.025kHz"""
	
	SR_10000 = 10000
	"""10kHz"""
	
	SR_8000 = 8000
	"""8kHz"""
	
	SR_6000 = 6000
	"""6kHz"""
	
	SR_3000 = 3000
	"""3kHz"""
	
	SR_2000 = 2000
	"""2kHz"""
	
	SR_1000 = 1000
	"""1kHz"""
	
	SR_500 = 500
	"""500Hz"""
	
	SR_300 = 300
	"""300Hz"""


class EWaveform(_StrEnum):
	"""An enumeration of the default waveforms available in Wwise."""
	
	SILENCE = "silence"
	"""Silence (flat waveform)."""
	
	SINE = "sine"
	"""Standard sine waveform."""
	
	TRIANGLE = "triangle"
	"""Standard triangle waveform."""
	
	SQUARE = "square"
	"""Standard triangle waveform."""
	
	WHITE_NOISE = "whiteNoise"
	"""Random waveform."""


class EReturnOptions(_StrEnum):
	"""An enumeration of return options available in the Wwise Authoring API."""
	
	AUDIO_SOURCE_LANGUAGE = "audioSource:language"  # same as "audioSourceLanguage"
	"""The audio source's language. This assumes a child audio source exists."""
	
	AUDIO_SOURCE_MAX_DURATION_SOURCE = "audioSource:maxDurationSource"
	"""The audio source's maximum duration source. This assumes a child audio source exists."""
	
	AUDIO_SOURCE_MAX_RADIUS_ATTENUATION = "audioSource:maxRadiusAttenuation"
	"""The audio source's maximum radius attenuation. This assumes a child audio source exists."""
	
	AUDIO_SOURCE_PLAYBACK_DURATION = "audioSource:playbackDuration"
	"""The audio source's playback duration. This assumes a child audio source exists."""
	
	AUDIO_SOURCE_TRIM_VALUES = "audioSource:trimValues"  # same as "audioSourceTrimValues"
	"""The audio source's trim values. This assumes a child audio source exists."""
	
	CATEGORY = "category"
	"""The category."""  # TODO: What does this mean? Test, then enhance this docstring.
	
	CHILDREN_COUNT = "childrenCount"
	"""The amount of children. This accounts for Audio Sources."""
	
	CLASS_ID = "classId"
	"""The class ID (e.g. the ClassID of AuxBus is 3997712). Refer to the Wwise Objects Reference for more
    information."""
	
	CONVERTED_WEM_FILE_PATH = "convertedWemFilePath"  # same as "convertedFilePath"
	"""The path of the converted file (WEM)."""
	
	DURATION = "duration"
	"""The estimated duration of the object."""
	
	FILE_PATH = "filePath"
	"""The file path (if any). Usually used with Work Units and Sources."""
	
	GUID = "id"
	"""Global Unique Identifier"""
	
	IS_EXPLICIT_MUTE = "isExplicitMute"
	"""Whether the object is explicitly muted. This is represented by the blue fill on the [M] button in Wwise."""
	
	IS_EXPLICIT_SOLO = "isExplicitSolo"
	"""Whether the object is explicitly muted. This is represented by the yellow fill on the [S] button in Wwise."""
	
	IS_IMPLICIT_MUTE = "isImplicitMute"
	"""Whether the object is implicitly muted (e.g. muted parent)."""
	
	IS_IMPLICIT_SOLO = "isImplicitSolo"
	"""Whether the object is implicitly muted (e.g. soloed parent)."""
	
	IS_INCLUDED = "isIncluded"
	"""Whether the object is included. Not being included means it will not be converted or included in SoundBanks or
    other data."""
	
	IS_PLAYABLE = "isPlayable"
	"""Whether the object is playable (e.g. a Sound object is playable)."""
	
	MAX_DURATION_SOURCE = "maxDurationSource"
	"""The maximum duration of the source."""
	
	MAX_RADIUS_ATTENUATION = "maxRadiusAttenuation"
	"""Maximum attenuation radius."""
	
	MEDIA_SIZE = "mediaSize"
	"""The media size"""  # TODO: What is the unit of measurement here? Probably bytes, but we should check and add that to the docstring.
	
	MUSIC_PLAYLIST_ROOT = "music:playlistRoot"  # same as "musicPlaylistRoot"
	"""The music playlist root."""
	
	MUSIC_TRANSITION_ROOT = "music:transitionRoot"  # same as "musicTransitionRoot"
	"""The music transition root."""
	
	NAME = "name"
	"""The object's name."""
	
	NOTES = "notes"
	"""Notes attached to the object."""
	
	OBJECT_SIZE = "objectSize"
	"""The object size."""  # TODO: What is the unit of measurement here? Probably bytes, but we should check and add that to the docstring.
	
	ORIGINAL_FILE_PATH = "originalFilePath"  # same as "originalWavFilePath"
	"""The file path."""
	
	ORIGINAL_RELATIVE_FILE_PATH = "originalRelativeFilePath"
	"""The file path of the original asset, relative to the project folders."""
	
	OWNER = "owner"
	"""The owner of the object."""  # TODO: What does this mean? Same as parent? Test, then enhance this docstring. If same as parent, may be removed.
	
	PARENT = "parent"
	"""The parent of the object."""
	
	PATH = "path"
	"""The project path of the object (e.g. "/Actor-Mixer Hierarchy/Default Work Unit/Physics/Collisions/TestSound")."""
	
	PLAYBACK_DURATION = "playbackDuration"
	"""The playback duration."""
	
	PLUGIN_NAME = "pluginName"
	"""The name of the plugin."""
	
	POINTS = "points"
	"""Points."""  # TODO: What does this mean? Test, then enhance this docstring.
	
	SHORT_ID = "shortId"
	"""The ShortID of the object."""
	
	SOUNDBANK_BNK_FILE_PATH = "soundbank:bnkFilePath"  # same as "soundbankBnkFilePath"
	"""The path to the associated BNK file."""
	
	SOUND_CONVERTED_WEM_FILE_PATH = "sound:convertedWemFilePath"
	"""The sound object's source's converted WEM file path. This assumes the object in question is a Sound."""
	
	SOUND_ORIGINAL_WAV_FILE_PATH = "sound:originalWavFilePath"
	"""The sound object's source's original WAV file path. This assumes the object in question is a Sound."""
	
	STATE_GROUPS = "stateGroups"
	"""State groups."""
	
	STATE_PROPERTIES = "stateProperties"
	"""State properties."""
	
	STRUCTURE_SIZE = "structureSize"
	"""The size of the structure."""  # TODO: What is the unit of measurement here? Probably bytes, but we should check and add that to the docstring.
	
	SWITCH_CONTAINER_CHILD_CONTEXT = "switchContainerChild:context"  # same as "switchContainerChildContext"
	"""The context (re: children) of a Switch Container. This assumes the object in question is a Switch Container."""
	
	TOTAL_SIZE = "totalSize"
	"""The total size."""  # TODO: What is the unit of measurement here? Probably bytes, but we should check and add that to the docstring.
	
	TYPE = "type"
	"""The name of the type. Examples: RandomSequenceContainer, MusicTrack, AudioFileSource, etc."""
	
	WORK_UNIT = "workunit"
	"""The Work Unit the object belongs to."""
	
	WORK_UNIT_IS_DEFAULT = "workunit:isDefault"  # same as "workunitIsDefault"
	"""Whether the Work Unit is a default object. This assumes the object in question is a Work Unit."""
	
	WORK_UNIT_IS_DIRTY = "workunit:isDirty"  # same as "workunitIsDirty"
	"""Whether the Work Unit is dirty (has unsaved changes). This assumes the object in question is a Work Unit."""
	
	WORK_UNIT_TYPE = "workunit:type"  # same as "workunitType"
	"""The type of Work Unit (e.g. actual Work Unit vs Physical Folder). This assumes the object in question is a Work
    Unit."""
	
	def __hash__(self) -> int:
		""":return: The enum value, hashed."""
		return self.value.__hash__()
	
	@classmethod
	def get_defaults(cls) -> tuple[_Self, ...]:
		"""
		Gets the default return options for PyWwise. Those are usually used to construct WwiseObjectInfo instances.
		:return: A tuple containing the default return options.
		"""
		return EReturnOptions.GUID, EReturnOptions.NAME, EReturnOptions.TYPE, EReturnOptions.PATH


class EObjectType(tuple[int, int, str], _Enum):
	"""An enumeration of class IDs for all different Wwise objects."""
	
	UNKNOWN = -1, -1, "Unknown"
	ACOUSTIC_TEXTURE = 72, 4718608, "AcousticTexture"
	ACTION = 5, 327696, "Action"
	ACTION_EXCEPTION = 76, 4980752, "ActionException"
	ACTOR_MIXER = 8, 524304, "ActorMixer"
	ATTENUATION = 41, 2686992, "Attenuation"
	AUDIO_DEVICE = 71, 4653072, "AudioDevice"
	AUDIO_SOURCE = 0, 16, "AudioSource"
	AUX_BUS = 61, 3997712, "AuxBus"
	BLEND_CONTAINER = 29, 1900560, "BlendContainer"
	BLEND_TRACK = 30, 1966096, "BlendTrack"
	BUS = 21, 1376272, "Bus"
	CONTROL_SURFACE_BINDING = 67, 4390928, "ControlSurfaceBinding"
	CONTROL_SURFACE_BINDING_GROUP = 68, 4456464, "ControlSurfaceBindingGroup"
	CONTROL_SURFACE_SESSION = 66, 4325392, "ControlSurfaceSession"
	CONVERSION = 55, 3604496, "Conversion"
	CURVE = 14, 917520, "Curve"
	CUSTOM_STATE = 79, 5177360, "CustomState"
	DIALOGUE_EVENT = 46, 3014672, "DialogueEvent"
	EFFECT = 17, 1114128, "Effect"
	EFFECT_SLOT = 84, 5505040, "EffectSlot"
	EVENT = 4, 262160, "Event"
	EXTERNAL_SOURCE = 57, 3735568, "ExternalSource"
	EXTERNAL_SOURCE_FILE = 56, 3670032, "ExternalSourceFile"
	FOLDER = 2, 131088, "Folder"
	GAME_PARAMETER = 23, 1507344, "GameParameter"
	LANGUAGE = 75, 4915216, "Language"
	MARKER = 82, 5373968, "Marker"
	METADATA = 81, 5308432, "Metadata"
	MIDI_FILE_SOURCE = 80, 5242896, "MidiFileSource"
	MIDI_PARAMETER = 63, 4128784, "MidiParameter"
	MIXING_SESSION = 53, 3473424, "MixingSession"
	MODIFIER = 15, 983056, "Modifier"
	MODULATOR_ENVELOPE = 65, 4259856, "ModulatorEnvelope"
	MODULATOR_LFO = 64, 4194320, "ModulatorLfo"
	MODULATOR_TIME = 78, 5111824, "ModulatorTime"
	MULTI_SWITCH_ENTRY = 83, 655360016, "MultiSwitchEntry"
	MUSIC_CLIP = 60, 3932176, "MusicClip"
	MUSIC_CLIP_MIDI = 62, 4063248, "MusicClipMidi"
	MUSIC_CUE = 59, 3866640, "MusicCue"
	MUSIC_EVENT_CUE = 77, 5046288, "MusicEventCue"
	MUSIC_FADE = 39, 2555920, "MusicFade"
	MUSIC_PLAYLIST_CONTAINER = 34, 2228240, "MusicPlaylistContainer"
	MUSIC_PLAYLIST_ITEM = 36, 2359312, "MusicPlaylistItem"
	MUSIC_SEGMENT = 27, 1769488, "MusicSegment"
	MUSIC_STINGER = 38, 2490384, "MusicStinger"
	MUSIC_SWITCH_CONTAINER = 35, 2293776, "MusicSwitchContainer"
	MUSIC_TRACK = 28, 1835024, "MusicTrack"
	MUSIC_TRACK_SEQUENCE = 58, 3801104, "MusicTrackSequence"
	MUSIC_TRANSITION = 37, 2424848, "MusicTransition"
	OBJECT_SETTING_ASSOC = 24, 1572880, "ObjectSettingAssociation"  # wrongly listed as "ObjectSettingAssoc" in AK docs?
	PANNER = 42, 2752528, "Panner"
	PATH_2D = 11, 720912, "Path2d"
	PLATFORM = 69, 4522000, "Platform"
	PLUGIN_DATA_SOURCE = 54, 3538960, "PluginDataSource"
	POSITION = 12, 786448, "Position"
	PROJECT = 3, 196624, "Project"
	QUERY = 32, 2097168, "Query"
	RANDOM_SEQUENCE_CONTAINER = 9, 589840, "RandomSequenceContainer"
	RTPC = 22, 1441808, "Rtpc"  # AK docs list as capitalized ("Rtpc"), but return values are all caps?
	SEARCH_CRITERIA = 33, 2162704, "SearchCriteria"
	SOUND = 1, 65552, "Sound"
	SOUND_BANK = 18, 1179664, "SoundBank"
	SOUNDCASTER_SESSION = 26, 1703952, "SoundcasterSession"
	SOURCE_PLUGIN = 16, 1048592, "SourcePlugin"
	STATE = 6, 393232, "State"
	STATE_GROUP = 7, 458768, "StateGroup"
	SWITCH = 20, 1310736, "Switch"
	SWITCH_CONTAINER = 10, 655376, "SwitchContainer"
	SWITCH_GROUP = 19, 1245200, "SwitchGroup"
	TRIGGER = 40, 2621456, "Trigger"
	USER_PROJECT_SETTINGS = 51, 3342352, "UserProjectSettings"
	WORK_UNIT = 25, 1638416, "WorkUnit"
	
	@classmethod
	def from_plugin_id(cls, plugin_id: int):
		"""
		Gets an enum member by plugin ID.
		:param plugin_id: The plugin ID.
		:return: An enum member whose plugin ID matches the specified plugin ID. If no valid member was found, UNKNOWN
				 is returned instead.
		"""
		for member in cls:
			if member.get_plugin_id() == plugin_id:
				return member
		return cls.UNKNOWN
	
	@classmethod
	def from_class_id(cls, class_id: int):
		"""
		Gets an enum member by class ID.
		:param class_id: The class ID.
		:return: An enum member whose class ID matches the specified class ID. If no valid member was found, UNKNOWN
				 is returned instead.
		"""
		for member in cls:
			if member.get_class_id() == class_id:
				return member
		return cls.UNKNOWN
	
	@classmethod
	def from_type_name(cls, type_name: str):
		"""
		Gets an enum member by type name.
		:param type_name: The type name.
		:return: An enum member whose type name matches the specified type name. If no valid member was found, UNKNOWN
				 is returned instead.
		"""
		type_name = type_name.upper()  # The comparisons are all case-insensitive
		for member in cls:
			if member.get_type_name().upper() == type_name:
				return member
		return cls.UNKNOWN
	
	def get_plugin_id(self) -> int:
		""":return: The Wwise object type's PluginID."""
		return self.value[0]
	
	def get_class_id(self) -> int:
		""":return: The Wwise object type's ClassID."""
		return self.value[1]
	
	def get_type_name(self) -> str:
		""":return: The Wwise object type's name, as a string."""
		return self.value[2]


class EStartMode(_StrEnum):
	"""An enumeration of command add-on start options available in the Wwise Authoring API."""
	
	SINGLE_SELECTION_SINGLE_PROCESS = "SingleSelectionSingleProcess"
	"""SingleSelectionSingleProcess: only support single selection, starts the program once."""
	
	MULTIPLE_SELECTION_SINGLE_PROCESS_SPACE_SEPARATED = "MultipleSelectionSingleProcessSpaceSeparated"
	"""MultipleSelectionSingleProcessSpaceSeparated: program is started once with variables expanded to space separated
    arguments, each enclosed in double-quotes."""
	
	MULTIPLE_SELECTION_MULTIPLE_PROCESSES = "MultipleSelectionMultipleProcesses"
	"""MultipleSelectionMultipleProcesses: program is started once per selected item, in parallel. Each running instance
    receives one selected item."""
	
	def __hash__(self) -> int:
		""":return: The enum value, hashed."""
		return self.value.__hash__()


class ECommand(_StrEnum):
	"""An enumeration of all Wwise commands. Please keep in mind that the commands in this enumeration might be slightly
	inaccurate if you are using a version of Wwise that is not verified and tested with PyWwise."""
	
	ACTIVATE_NEXT_FLOATING_VIEW = "ActivateNextFloatingView"
	"""Activates the next floating view."""
	
	ACTIVATE_PREVIOUS_FLOATING_VIEW = "ActivatePreviousFloatingView"
	"""Activates the previous floating view."""
	
	CHECK_PROJECT_FILES = "CheckProjectFiles"
	"""Scans for Project and Work Unit files that have changed on disk."""
	
	CLOSE_CURRENT_OBJECT_TAB = "CloseCurrentObjectTab"
	"""Close the current object tab."""
	
	CLOSE_OBJECT_TABS_TO_THE_RIGHT = "CloseObjectTabsToTheRight"
	"""Close the object tabs to the right."""
	
	CLOSE_OTHER_OBJECT_TABS = "CloseOtherObjectTabs"
	"""Close the other object tabs."""
	
	CLOSE_PROJECT = "CloseProject"
	"""Closes the project."""
	
	CLOSE_VIEW = "CloseView"
	"""Closes the active view."""
	
	CONVERT = "Convert"
	"""Shows the Convert dialog for the specified objects. \n
    **Parameter**: objects - an array of objects"""
	
	CONVERT_ALL_PLATFORM = "ConvertAllPlatform"
	"""Converts the specified objects on all platforms. \n
    **Parameter**: objects - an array of objects"""
	
	CONVERT_CURRENT_PLATFORM = "ConvertCurrentPlatform"
	"""Converts the specified objects on the specified platform. If not specified, it uses the current platform or
    current selected objects. \n
    **Parameter**: objects - an array of objects platforms - an array of platforms (array of GUID string)"""
	
	CONVERT_SFX_TO_VOICE = "ConvertSFXToVoice"
	"""Converts the specified objects to Sound Voice objects. \n
    **Parameter**: objects - an array of objects"""
	
	CONVERT_TO_SOUND_SFX = "ConvertToSoundSFX"
	"""Converts the specified objects to Sound SFX objects.	\n
    **Parameter**: objects - an array of objects"""
	
	COPY_GUI_DS_PATHS_TO_CLIPBOARD = "CopyGUIDsPathsToClipboard"
	"""Copies the unique IDs (GUID) of the specified objects to clipboard. \n
    **Parameter**: objects - an array of objects"""
	
	COPY_PATHS_TO_CLIPBOARD = "CopyPathsToClipboard"
	"""Copies the Wwise project paths of the specified objects to clipboard. \n
    **Parameter**: objects - an array of objects"""
	
	COPY_SHORT_IDS_TO_CLIPBOARD = "CopyShortIDsToClipboard"
	"""Copies the short IDs (unsigned 32 bit) of the specified objects to clipboard. \n
    **Parameter**: objects - an array of objects"""
	
	COPY_WAQL_TO_CLIPBOARD = "CopyWAQLToClipboard"
	"""Generates a WAQL query with the specified object paths and copies it to clipboard. \n
    **Parameter**: objects - an array of objects"""
	
	CREATE_IN_GAC = "CreateInGAC"
	"""Creates the associated Nuendo objects for the specified objects using Game Audio Connect. \n
    **Parameter**: objects - an array of objects"""
	
	CREATE_NEW_SOUNDBANK = "CreateNewSoundbank"
	"""Creates a new SoundBank."""
	
	DETACH_CURRENT_OBJECT_TAB = "DetachCurrentObjectTab"
	"""Detach the current object tab."""
	
	DUPLICATE_CURRENT_OBJECT_TAB = "DuplicateCurrentObjectTab"
	"""Duplicate the current object tab."""
	
	EDIT_USER_PREFERENCES = "EditUserPreferences"
	"""Shows the User Preferences dialog for editing."""
	
	FIND_IN_PROJECT_EXPLORER_NEW_PINNED_VIEW = "FindInProjectExplorerNewPinnedView"
	"""Finds the specified object in the Project Explorer (New Pinned View). \n
    **Parameter**: objects - an array of objects"""
	
	FIND_IN_PROJECT_EXPLORER_SELECTION_CHANNEL1 = "FindInProjectExplorerSelectionChannel1"
	"""Finds the specified object in the Project Explorer (Selection Channel 1). \n
    **Parameter**: objects - an array of objects"""
	
	FIND_IN_PROJECT_EXPLORER_SELECTION_CHANNEL2 = "FindInProjectExplorerSelectionChannel2"
	"""Finds the specified object in the Project Explorer (Selection Channel 2). \n
    **Parameter**: objects - an array of objects"""
	
	FIND_IN_PROJECT_EXPLORER_SELECTION_CHANNEL3 = "FindInProjectExplorerSelectionChannel3"
	"""Finds the specified object in the Project Explorer (Selection Channel 3). \n
    **Parameter**: objects - an array of objects"""
	
	FIND_IN_PROJECT_EXPLORER_SELECTION_CHANNEL4 = "FindInProjectExplorerSelectionChannel4"
	"""Finds the specified object in the Project Explorer (Selection Channel 4). \n
    **Parameter**: objects - an array of objects"""
	
	FOCUS_NEXT = "FocusNext"
	"""Focuses the next control in the current view."""
	
	FOCUS_PREVIOUS = "FocusPrevious"
	"""Focuses the previous control in the current view."""
	
	FORCE_SAVE_PROJECT = "ForceSaveProject"
	"""Makes all Work Units dirty and saves the project."""
	
	GENERATE_ALL_SOUNDBANKS_ALL_PLATFORMS = "GenerateAllSoundbanksAllPlatforms"
	"""Generates all SoundBanks on all platforms."""
	
	GENERATE_ALL_SOUNDBANKS_ALL_PLATFORMS_AUTO_CLOSE = "GenerateAllSoundbanksAllPlatformsAutoClose"
	"""Generates all SoundBanks on all platforms (Progress dialog is closed automatically at the end of operation)."""
	
	GENERATE_ALL_SOUNDBANKS_CURRENT_PLATFORM = "GenerateAllSoundbanksCurrentPlatform"
	"""Generates all SoundBanks on the specified platform. If not specified, it uses the current platform. \n
    **Parameter**: platforms - an array of platforms (array of GUID string)"""
	
	GENERATE_ALL_SOUNDBANKS_CURRENT_PLATFORM_AUTO_CLOSE = "GenerateAllSoundbanksCurrentPlatformAutoClose"
	"""Generates all SoundBanks on the specified platform. If not specified, it uses the current platform
    (Progress dialog is closed automatically at the end of operation). \n
    **Parameter**: platforms - an array of platforms (array of GUID string)"""
	
	GENERATE_SELECTED_SOUNDBANKS_ALL_PLATFORMS = "GenerateSelectedSoundbanksAllPlatforms"
	"""Generates the specified SoundBank objects on all platforms. \n
    **Parameter**: objects - an array of objects"""
	
	GENERATE_SELECTED_SOUNDBANKS_ALL_PLATFORMS_AUTO_CLOSE = "GenerateSelectedSoundbanksAllPlatformsAutoClose"
	"""Generates the specified SoundBank objects on all platforms (Progress dialog is closed automatically at the end
    of operation). \n
    **Parameter**: objects - an array of objects"""
	
	GENERATE_SELECTED_SOUNDBANKS_CURRENT_PLATFORM = "GenerateSelectedSoundbanksCurrentPlatform"
	"""Generates the specified SoundBank objects on the specified platform. If not specified, it uses the current
    platform or current selected objects. \n
    **Parameter**: objects - an array of objects platforms - an array of platforms (array of GUID string)"""
	
	GENERATE_SELECTED_SOUNDBANKS_CURRENT_PLATFORM_AUTO_CLOSE = "GenerateSelectedSoundbanksCurrentPlatformAutoClose"
	"""Generates the specified SoundBank objects on the specified platform. If not specified, it uses the current
    platform or current selected objects (Progress dialog is closed automatically at the end of operation). \n
    **Parameter**: objects - an array of objects platforms - an array of platforms (array of GUID string)"""
	
	GENERATE_SOUNDBANKS_WITH_CURRENT_SETTINGS = "GenerateSoundbanksWithCurrentSettings"
	"""Generates SoundBanks using the current SoundBank Manager settings (Progress dialog is closed automatically at
    the end of operation)."""
	
	HELP = "Help"
	"""Shows the Wwise Help."""
	
	INSPECT = "Inspect"
	"""Inspects the specified objects. \n
    **Parameter**: objects - an array of objects"""
	
	INSPECT_NEXT = "InspectNext"
	"""Inspects the next object inspected."""
	
	INSPECT_PARENT = "InspectParent"
	"""Inspects the parent of the currently inspected object."""
	
	INSPECT_PREVIOUS = "InspectPrevious"
	"""Inspects the previous object inspected."""
	
	KEEP_OPEN_CURRENT_OBJECT_TAB = "KeepOpenCurrentObjectTab"
	"""Keep Open the current object tab."""
	
	LOAD_PRESET = "LoadPreset"
	"""Shows the Load Preset dialog for the active view."""
	
	LOAD_THEME_CLASSIC = "LoadThemeClassic"
	"""Loads the classic theme."""
	
	LOAD_THEME_DARK = "LoadThemeDark"
	"""Loads the dark theme."""
	
	LOAD_THEME_LIGHT = "LoadThemeLight"
	"""Loads the light theme."""
	
	LOAD_UNLOADED_WORK_UNITS = "LoadUnloadedWorkUnits"
	"""Loads currently unloaded Work Units."""
	
	MAXIMIZE_OBJECT_TAB_DEFAULT_VIEW = "MaximizeObjectTabDefaultView"
	"""Maximize the current default view of the object tabs."""
	
	MAXIMIZE_VIEW = "MaximizeView"
	"""Maximizes the active view."""
	
	MINIMIZE_OBJECT_TAB_DEFAULT_VIEW = "MinimizeObjectTabDefaultView"
	"""Minimize the current default view of the object tabs."""
	
	MINIMIZE_VIEW = "MinimizeView"
	"""Minimizes the active view."""
	
	MOVE_CURRENT_OBJECT_TAB_TO_THE_LEFT = "MoveCurrentObjectTabToTheLeft"
	"""Move the current tab to the left."""
	
	MOVE_CURRENT_OBJECT_TAB_TO_THE_RIGHT = "MoveCurrentObjectTabToTheRight"
	"""Move the current tab to the right."""
	
	MUTE = "Mute"
	"""Mutes the specified objects, or current selection if no object specified. \n
    **Parameter**: value - True or False to set the Mute state. If unspecified, the Mute state will be toggled.
    **Parameter**: objects - an array of objects"""
	
	NEW_PROJECT = "NewProject"
	"""Shows the New Project dialog."""
	
	NEXT_OBJECT_TAB = "NextObjectTab"
	"""Navigate to the next object tab."""
	
	NEXT_PERF_FRAME = "NextPerfFrame"
	"""Goes to next audio frame in Performance Graph."""
	
	OPEN_CONTAINING_FOLDER_SOUNDBANK = "OpenContainingFolderSoundbank"
	"""Opens a Windows Explorer window on the Containing folder of specified objects' SoundBank files.	\n
	**Parameter**: objects - an array of objects"""
	
	OPEN_CONTAINING_FOLDER_WAV = "OpenContainingFolderWAV"
	"""Opens a Windows Explorer window on the Containing folder of specified objects' wav files. \n
	**Parameter**: objects - an array of objects"""
	
	OPEN_CONTAINING_FOLDER_WORK_UNIT = "OpenContainingFolderWorkUnit"
	"""Opens a Windows Explorer window on the Containing folder of specified objects' Work Units. \n
	**Parameter**: objects - an array of objects"""
	
	OPEN_IN_EXTERNAL_EDITOR = "OpenInExternalEditor"
	"""Opens the specified objects in the first (index 0) External Editor. \n
    **Parameter**: objects - an array of objects"""
	
	OPEN_IN_EXTERNAL_EDITOR1 = "OpenInExternalEditor1"
	"""Opens the specified objects in the second (index 1) External Editor. \n
    **Parameter**: objects - an array of objects"""
	
	OPEN_IN_EXTERNAL_EDITOR2 = "OpenInExternalEditor2"
	"""Opens the specified objects in the third (index 2) External Editor. \n
    **Parameter**: objects - an array of objects"""
	
	OPEN_IN_EXTERNAL_EDITOR3 = "OpenInExternalEditor3"
	"""Opens the specified objects in the fourth (index 3) External Editor. \n
    **Parameter**: objects - an array of objects"""
	
	OPEN_IN_EXTERNAL_EDITOR4 = "OpenInExternalEditor4"
	"""Opens the specified objects in the fifth (index 4) External Editor. \n
    **Parameter**: objects - an array of objects"""
	
	OPEN_IN_GAC = "OpenInGAC"
	"""Opens the specified objects in Nuendo using Game Audio Connect. \n
    **Parameter**: objects - an array of objects"""
	
	OPEN_IN_NEW_TAB = "OpenInNewTab"
	"""Inspects the specified objects. \n
    **Parameter**: objects - an array of objects"""
	
	OPEN_IN_NEW_WINDOW = "OpenInNewWindow"
	"""Inspects the specified objects in a new window. \n
    **Parameter**: objects - an array of objects"""
	
	OPEN_IN_WWISE_WAVE_VIEWER = "OpenInWwiseWaveViewer"
	"""Opens specified objects in the Wwise Wave Viewer. \n
    **Parameter**: objects - an array of objects"""
	
	OPEN_PROJECT = "OpenProject"
	"""Shows the Open Project dialog."""
	
	PIN_VIEW = "PinView"
	"""Pins the active view."""
	
	POPOUT_OBJECT_TAB_DEFAULT_VIEW = "PopoutObjectTabDefaultView"
	"""Maximize the current default view of the object tabs"""
	
	PREVIOUS_OBJECT_TAB = "PreviousObjectTab"
	"""Navigate to the previous object tab."""
	
	PREVIOUS_PERF_FRAME = "PreviousPerfFrame"
	"""Goes to previous audio frame in Performance Graph."""
	
	PROFILER_FILTER_CLEAR_ALL = "ProfilerFilterClearAll"
	"""Clears all filters."""
	
	PROFILER_FILTER_CLEAR_CURRENT_VIEW = "ProfilerFilterClearCurrentView"
	"""Clears the profiler filter of the current view."""
	
	PROFILER_FILTER_EXCLUDE_OBJECT_NAME_FROM_CURRENT = "ProfilerFilterExcludeObjectNameFromCurrent"
	"""Adds the name of the selected object as an exclude to the filter text of the current view."""
	
	PROFILER_FILTER_PROMOTE_CURRENT_TO_ALL = "ProfilerFilterPromoteCurrentToAll"
	"""Copies the profiler filter of the current view to all other filters."""
	
	PROFILER_FILTER_SET_NAME_TO_CURRENT = "ProfilerFilterSetNameToCurrent"
	"""Sets the name of the selected object as the filter text of the current view."""
	
	PROFILER_FILTER_SET_PIPELINE_I_D = "ProfilerFilterSetPipelineID"
	"""Sets the profiler text filter to match a specific pipeline ID."""
	
	PROFILER_FILTER_SET_SELECTED_OBJECT_TO_CURRENT = "ProfilerFilterSetSelectedObjectToCurrent"
	"""Sets the currently selected object in the profiler filter of the current view."""
	
	PROFILER_FILTER_TOGGLE_CURRENT_MUTE_SOLO = "ProfilerFilterToggleCurrentMuteSolo"
	"""Toggles ON/OFF the mute/solo filtering in the current view."""
	
	PROFILER_FILTER_TOGGLE_CURRENT_SHOW_NOTHING_WHEN_EMPTY = "ProfilerFilterToggleCurrentShowNothingWhenEmpty"
	"""Toggles ON/OFF the Show Nothing when filter is empty."""
	
	PROFILER_FILTER_TOGGLE_LOCAL_GLOBAL = "ProfilerFilterToggleLocalGlobal"
	"""Toggles the profiler filter of the current view between link and unlink modes."""
	
	REDO = "Redo"
	"""Redoes the last undone operation."""
	
	RELOAD_COMMAND_ADDONS = "ReloadCommandAddons"
	"""Reloads all the custom command files in all the corresponding directories."""
	
	RELOAD_CURRENT_THEME = "ReloadCurrentTheme"
	"""Reloads the current user interface theme from disk. This is useful when implementing new themes."""
	
	RESET_ALL_MUTES = "ResetAllMutes"
	"""Resets all mutes currently active."""
	
	RESET_ALL_SOLOS = "ResetAllSolos"
	"""Resets all solos currently active."""
	
	RESTORE_VIEW = "RestoreView"
	"""Restores the active view."""
	
	SAVE_ALL_COUNTERS = "SaveAllCounters"
	"""Dumps the Performance Counters to a file."""
	
	SAVE_PRESET = "SavePreset"
	"""Shows the Load Preset dialog for the active view."""
	
	SAVE_PROJECT = "SaveProject"
	"""Saves the project."""
	
	SEARCH = "Search"
	"""Puts the focus on the search box. \n
    **Parameter**: value - the text (string) to be used for the search field"""
	
	SEARCH_COMMANDS = "SearchCommands"
	"""Puts the focus on the search box and enables the command search mode."""
	
	SEARCH_IN_CTRL = "SearchInCtrl"
	"""Opens the search box in the currently active control."""
	
	SEARCH_IN_CURRENT_VIEW = "SearchInCurrentView"
	"""Searches in the Current View if it has a search field. \n
    **Parameter**: value - the text (string) to be used for the search field"""
	
	SEARCH_IN_PROJECT_EXPLORER = "SearchInProjectExplorer"
	"""Searches in the Project Explorer (first available view). \n
    **Parameter**: value - the text (string) to be used for the search field"""
	
	SEARCH_IN_PROJECT_EXPLORER_NEW_PINNED_VIEW = "SearchInProjectExplorerNewPinnedView"
	"""Searches in the Project Explorer (New Pinned View). \n
    **Parameter**: value - the text (string) to be used for the search field"""
	
	SEARCH_IN_PROJECT_EXPLORER_SELECTION_CHANNEL1 = "SearchInProjectExplorerSelectionChannel1"
	"""Searches in the Project Explorer (Selection Channel 1). \n
    **Parameter**: value - the text (string) to be used for the search field"""
	
	SEARCH_IN_PROJECT_EXPLORER_SELECTION_CHANNEL2 = "SearchInProjectExplorerSelectionChannel2"
	"""Searches in the Project Explorer (Selection Channel 2). \n
    **Parameter**: value - the text (string) to be used for the search field"""
	
	SEARCH_IN_PROJECT_EXPLORER_SELECTION_CHANNEL3 = "SearchInProjectExplorerSelectionChannel3"
	"""Searches in the Project Explorer (Selection Channel 3). \n
    **Parameter**: value - the text (string) to be used for the search field"""
	
	SEARCH_IN_PROJECT_EXPLORER_SELECTION_CHANNEL4 = "SearchInProjectExplorerSelectionChannel4"
	"""Searches in the Project Explorer (Selection Channel 4). \n
    **Parameter**: value - the text (string) to be used for the search field"""
	
	SELECT_ONLINE_DOCUMENTATION = "SelectOnlineDocumentation"
	"""Selects CHM file as a documentation source."""
	
	SET_COLOR = "SetColor"
	"""Shows the Color Picker dialog for the specific objects. \n
    **Parameter**: objects - an array of objects"""
	
	SET_PROPERTY_SHEET_SPLIT_MODE_COLUMN = "SetPropertySheetSplitModeColumn"
	"""Sets the property sheet split mode to columns."""
	
	SET_PROPERTY_SHEET_SPLIT_MODE_NO = "SetPropertySheetSplitModeNo"
	"""Sets the property sheet split mode to not split."""
	
	SET_PROPERTY_SHEET_SPLIT_MODE_ROW = "SetPropertySheetSplitModeRow"
	"""Sets the property sheet split mode to rows."""
	
	SHOW_AUDIO_FILE_CACHE_CLEAR_DIALOG = "ShowAudioFileCacheClearDialog"
	"""Shows the Clear Audio File Cache dialog."""
	
	SHOW_AUDIO_FILES_CONVERSION_DIALOG = "ShowAudioFilesConversionDialog"
	"""Shows the Audio File Conversion dialog."""
	
	SHOW_AUDIO_FILES_IMPORTER = "ShowAudioFilesImporter"
	"""Shows the Audio File Importer dialog."""
	
	SHOW_AUDIO_PREFERENCES = "ShowAudioPreferences"
	"""Shows the Audio Preferences dialog."""
	
	SHOW_BATCH_RENAME = "ShowBatchRename"
	"""Shows the Batch Rename View, with the specified objects. \n
    **Parameter**: objects - an array of objects"""
	
	SHOW_BUG_REPORT = "ShowBugReport"
	"""Shows the Bug Report page."""
	
	SHOW_CONTACT_AK = "ShowContactAK"
	"""Shows AK's Contact Us page."""
	
	SHOW_CONTEXTUAL_HELP = "ShowContextualHelp"
	"""Shows the Contextual Help View for a specified property. \n
    **Parameter**: property - a pointer to a single CProp object"""
	
	SHOW_CONTROL_SURFACES_DLG = "ShowControlSurfacesDlg"
	"""Shows the Control Surfaces Settings dialog."""
	
	SHOW_DEFAULT_OBJECT_VALUES = "ShowDefaultObjectValues"
	"""Shows the Default Object Values dialog."""
	
	SHOW_DETAILS = "ShowDetails"
	"""Shows the details view with the specified objects. \n
    **Parameter**: objects - an array of objects"""
	
	SHOW_FILE_MANAGER = "ShowFileManager"
	"""Shows the File Manager dialog."""
	
	SHOW_GAC_SETTINGS = "ShowGACSettings"
	"""Shows the Nuendo Game Audio Connect setting."""
	
	SHOW_GAME_OBJECTS_VOICE_EXPLORER = "ShowGameObjectsVoiceExplorer"
	"""Focuses the Voice Explorer on the specified game object(s). \n
    **Parameter**: gameObjectIds - Ids of the game objects to show/select"""
	
	SHOW_KEYBOARD_SHORTCUTS = "ShowKeyboardShortcuts"
	"""Shows the Keyboard Shortcuts dialog."""
	
	SHOW_LANGUAGES = "ShowLanguages"
	"""Shows the Language Manager dialog."""
	
	SHOW_LEGAL_NOTICES = "ShowLegalNotices"
	"""Shows the legal notices dialog."""
	
	SHOW_LICENSE_MGR = "ShowLicenseMgr"
	"""Shows the License Manager dialog."""
	
	SHOW_LIST_VIEW = "ShowListView"
	"""Shows the List View on the specified objects. \n
    **Parameter**: objects - an array of objects value - the text (string) to be used for the search field"""
	
	SHOW_MULTI_EDITOR = "ShowMultiEditor"
	"""Shows the Multi Editor view on the specified objects. \n
    **Parameter**: objects - an array of objects"""
	
	SHOW_OBSTRUCTION_OCCLUSION_SETTINGS = "ShowObstructionOcclusionSettings"
	"""Shows the Project Settings dialog on the Obstruction/Occlusion tab."""
	
	SHOW_PASTE_PROPERTIES = "ShowPasteProperties"
	"""Shows the Paste Properties view on the specified object. \n
    **Parameter**: objects - an array of objects"""
	
	SHOW_PLATFORM_MANAGER = "ShowPlatformManager"
	"""Shows the Platform Manager dialog."""
	
	SHOW_PROFILER_SETTINGS = "ShowProfilerSettings"
	"""Shows the Profiler Settings dialog."""
	
	SHOW_PROJECT_SETTINGS = "ShowProjectSettings"
	"""Shows the Project Settings dialog."""
	
	SHOW_PROPERTY_HELP = "ShowPropertyHelp"
	"""Shows the Property Help View for a specified property. Deprecated, see ShowContextualHelp.
    **Parameter**: property - a pointer to a single CProp object."""
	
	SHOW_REFERENCE_VIEW = "ShowReferenceView"
	"""Shows the Reference View with the specified objects. \n
    **Parameter**: objects - an array of objects"""
	
	SHOW_REMOTE_CONNECTIONS = "ShowRemoteConnections"
	"""Shows the Remote Connections dialog."""
	
	SHOW_SCHEMATIC_VIEW = "ShowSchematicView"
	"""Shows the Schematic View on the specified objects. \n
    **Parameter**: value - the text (string) to be used for the search field objects - an array of objects"""
	
	SHOW_SOUND_BANK_DEFINITION_IMPORTER = "ShowSoundBankDefinitionImporter"
	"""Shows the Sound Bank Definition Importer dialog."""
	
	SHOW_SOUNDBANK_SETTINGS = "ShowSoundbankSettings"
	"""Shows the Project settings dialog, SoundBanks tab."""
	
	SHOW_SOURCE_EDITOR = "ShowSourceEditor"
	"""Shows the Source Editor on the specified objects. \n
    **Parameter**: objects - an array of objects"""
	
	SHOW_SPLASH_SCREEN = "ShowSplashScreen"
	"""Shows the initial Wwise loading screen (with the current software version)."""
	
	SHOW_USER_PREFERENCES = "ShowUserPreferences"
	"""Shows the User Preferences dialog."""
	
	SHOW_USER_PROJECT_SETTINGS = "ShowUserProjectSettings"
	"""Deprecated, see ShowDefaultObjectValues."""
	
	SHOW_USER_SOUNDBANK_SETTINGS = "ShowUserSoundbankSettings"
	"""Shows the user SoundBank settings dialog."""
	
	SHOW_VIEW_SETTINGS = "ShowViewSettings"
	"""Shows the view settings for the active view."""
	
	SHOW_VOICE_ASSETS_IMPORTER = "ShowVoiceAssetsImporter"
	"""Shows the Voice Asset Importer dialog."""
	
	SHOW_VOICE_INSPECTOR = "ShowVoiceInspector"
	"""Shows the Voice Inspector on the specified object. \n
    **Parameter**: objects - an array of objects voices - an array of voice (pipeline) Ids"""
	
	SHOW_VOICES_VOICE_EXPLORER = "ShowVoicesVoiceExplorer"
	"""Focuses the Voice Explorer on the specified voice(s). \n
    **Parameter**: voiceIds - Ids of the voices to show/select"""
	
	SHOW_WWISE_HELP = "ShowWwiseHelp"
	"""Shows the Wwise Help."""
	
	SHOW_WWISE_KNOWLEDGE_BASE = "ShowWwiseKnowledgeBase"
	"""Shows the Wwise Community Q&A."""
	
	SHOW_WWISE_SDK_DOCUMENTATION = "ShowWwiseSDKDocumentation"
	"""Shows the Wwise SDK documentation."""
	
	SOLO = "Solo"
	"""Solos the specified objects, or current selection if no object specified. \n
    **Parameter**: value - True or False to set the Solo state. If unspecified, the Solo state will be toggled.
    **Parameter**: objects - an array of objects"""
	
	SOURCE_CONTROL_ADD_WAV = "SourceControlAddWAV"
	"""Calls the Add command for the wav files associated with the specified objects on the Source Control plug-in
    (Perforce, SVN, etc). \n
    **Parameter**: objects - an array of objects"""
	
	SOURCE_CONTROL_ADD_WWU = "SourceControlAddWWU"
	"""Calls the Add command for the Work Units associated with the specified objects on the Source Control plug-in
    (Perforce, SVN, etc). \n
    **Parameter**: objects - an array of objects"""
	
	SOURCE_CONTROL_CHECKOUT_WAV = "SourceControlCheckoutWAV"
	"""Calls the Checkout command for the wav files associated with the specified objects on the Source Control plug-in
    (Perforce, SVN, etc). \n
    **Parameter**: objects - an array of objects"""
	
	SOURCE_CONTROL_CHECKOUT_WWU = "SourceControlCheckoutWWU"
	"""Calls the Checkout command for the Work Units associated with the specified objects on the Source Control plug-in
    (Perforce, SVN, etc). \n
    **Parameter**: objects - an array of objects"""
	
	SOURCE_CONTROL_COMMIT_WAV = "SourceControlCommitWAV"
	"""Calls the Commit command for the wav files associated with the specified objects on the Source Control plug-in
    (Perforce, SVN, etc). \n
    **Parameter**: objects - an array of objects"""
	
	SOURCE_CONTROL_COMMIT_WWU = "SourceControlCommitWWU"
	"""Calls the Commit/Submit command for the Work Units associated with the specified objects on the Source Control
    plug-in (Perforce, SVN, etc). \n
    **Parameter**: objects - an array of objects"""
	
	SOURCE_CONTROL_DIFF_WAV = "SourceControlDiffWAV"
	"""Calls the Diff command for the wav files associated with the specified objects on the Source Control plug-in
    (Perforce, SVN, etc). \n
    **Parameter**: objects - an array of objects"""
	
	SOURCE_CONTROL_DIFF_WWU = "SourceControlDiffWWU"
	"""Calls the Diff command for the Work Units associated with the specified objects on the Source Control plug-in
    (Perforce, SVN, etc). \n
    **Parameter**: objects - an array of objects"""
	
	SOURCE_CONTROL_REFRESH_ICONS = "SourceControlRefreshIcons"
	"""Refreshes the project status and the Source Control icons on Work Units."""
	
	SOURCE_CONTROL_REVERT_WAV = "SourceControlRevertWAV"
	"""Calls the Revert command for the wav files associated with the specified objects on the Source Control plug-in
    (Perforce, SVN, etc). \n
    **Parameter**: objects - an array of objects"""
	
	SOURCE_CONTROL_REVERT_WWU = "SourceControlRevertWWU"
	"""Calls the Revert command for the Work Units associated with the specified objects on the Source Control plug-in
    (Perforce, SVN, etc). \n
    **Parameter**: objects - an array of objects"""
	
	SOURCE_CONTROL_UPDATE_WAV = "SourceControlUpdateWAV"
	"""Calls the Update command for the wav files associated with the specified objects on the Source Control plug-in
    (Perforce, SVN, etc). \n
    **Parameter**: objects - an array of objects"""
	
	SOURCE_CONTROL_UPDATE_WWU = "SourceControlUpdateWWU"
	"""Calls the Update command for the Work Units associated with the specified objects on the Source Control plug-in
    (Perforce, SVN, etc). \n
    **Parameter**: objects - an array of objects"""
	
	SPLIT_CURRENT_TAB_TO_THE_RIGHT = "SplitCurrentTabToTheRight"
	"""Split the current tab, creating a new tab panel to the right."""
	
	START_CAPTURE = "StartCapture"
	"""Starts a profiling capture, does nothing if already started."""
	
	START_STOP_CAPTURE = "StartStopCapture"
	"""Starts a profiling capture, or stops it if already started."""
	
	STOP_CAPTURE = "StopCapture"
	"""Stops a profiling capture, does nothing if already stopped."""
	
	TOGGLE_EXPAND_COLLAPSE = "ToggleExpandCollapse"
	"""Toggles Expand/Collapse for the active floating view."""
	
	TOGGLE_FOLLOW_CAPTURE = "ToggleFollowCapture"
	"""Toggles the Show Live Data button in the toolbar."""
	
	TOGGLE_FOLLOW_OBJECT_SELECTION_IN_PROJECT_EXPLORER = "ToggleFollowObjectSelectionInProjectExplorer"
	"""Toggles the automatic following of object selection in Project Explorer."""
	
	TRANSPORT_DISABLE_MONITOR = "TransportDisableMonitor"
	"""Disables the inclusion button in the Transport Control."""
	
	TRANSPORT_DISABLE_ORIGINAL = "TransportDisableOriginal"
	"""Disables the Original button in the Transport Control."""
	
	TRANSPORT_DISPLAY_RTPC = "TransportDisplayRTPC"
	"""Switches the Transport Control to display Game Parameters."""
	
	TRANSPORT_DISPLAY_STATES = "TransportDisplayStates"
	"""Switches the Transport Control to display States."""
	
	TRANSPORT_DISPLAY_SWITCHES = "TransportDisplaySwitches"
	"""Switches the Transport Control to display Switches."""
	
	TRANSPORT_DISPLAY_TRIGGERS = "TransportDisplayTriggers"
	"""Switches the Transport Control to display Triggers."""
	
	TRANSPORT_ENABLE_MONITOR = "TransportEnableMonitor"
	"""Enables the inclusion button in the Transport Control."""
	
	TRANSPORT_ENABLE_ORIGINAL = "TransportEnableOriginal"
	"""Enables the Original button in the Transport Control."""
	
	TRANSPORT_PAUSE = "TransportPause"
	"""Pauses the object currently in playback in the Transport Control."""
	
	TRANSPORT_PIN = "TransportPin"
	"""Pins or unpins the Transport Control currently loaded object."""
	
	TRANSPORT_PIN_SELECTED = "TransportPinSelected"
	"""Pins the specified object, or current selection if no object is specified, to the Transport Control."""
	
	TRANSPORT_PLAY_DIRECTLY = "TransportPlayDirectly"
	"""Plays the object currently loaded in the Transport Control by bypassing properties that have an influence on the
    sound, such as the volume."""
	
	TRANSPORT_PLAY_STOP = "TransportPlayStop"
	"""Plays the object currently loaded in the Transport Control. If the playback is in progress, it stops the
    playback."""
	
	TRANSPORT_RESET = "TransportReset"
	"""Resets the Transport Control playback and internal states."""
	
	TRANSPORT_TOGGLE_MONITOR = "TransportToggleMonitor"
	"""Toggles the inclusion button in the Transport Control."""
	
	TRANSPORT_TOGGLE_ORIGINAL = "TransportToggleOriginal"
	"""Toggles the Original button in the Transport Control."""
	
	UNDO = "Undo"
	"""Undoes the last operation in the queue."""
	
	USE_AUDIO_OUTPUT_SYSTEM5 = "UseAudioOutputSystem5"
	"""Selects 5.1 as audio output system."""
	
	USE_AUDIO_OUTPUT_SYSTEM7 = "UseAudioOutputSystem7"
	"""Selects 7.1 as audio output system."""
	
	USE_AUDIO_OUTPUT_SYSTEM_DEFAULT = "UseAudioOutputSystemDefault"
	"""Selects default audio output system."""
	
	USE_AUDIO_OUTPUT_SYSTEM_STEREO_HEADPHONES = "UseAudioOutputSystemStereoHeadphones"
	"""Selects stereo headphones as audio output system."""
	
	USE_AUDIO_OUTPUT_SYSTEM_STEREO_SPEAKERS = "UseAudioOutputSystemStereoSpeakers"
	"""Selects stereo speakers as audio output system."""
	
	USE_ONLINE_DOCUMENTATION = "UseOnlineDocumentation"
	"""Selects Wwise website as a documentation source."""


class EImportOperation(_StrEnum):
	"""An enumeration of possible import operations."""
	
	CREATE_NEW_OBJECT = "CreateNewObject"
	"""Creation of a new object."""
	
	REPLACE_FILE = "ReplaceFile"
	"""Replacement of an already-existing original asset."""
	
	LOCALIZE = "Localize"
	"""Localization."""
	
	REPLACE_OBJECT = "ReplaceObject"
	"""Replacement of an already-existing Wwise object."""


class EDataTypes(_StrEnum):
	"""Enumeration of possible data types to capture in the profiler"""
	
	CPU = "cpu"
	
	MEMORY = "memory"
	
	STREAM = "stream"
	
	VOICES = " voices"
	
	LISTENER = "listener"
	
	OBSTRUCTION_OCCLUSION = "obstructionOcclusion"
	
	MARKERS_NOTIFICATION = "markersNotification"
	
	SOUNDBANKS = "soundbanks"
	
	LOADED_MEDIA = "loadedMedia"
	
	PREPARED_EVENTS = "preparedEvents"
	
	PREPARED_GAME_SYNCS = "preparedGameSyncs"
	
	INTERACTIVE_MUSIC = "interactiveMusic"
	
	STREAMING_DEVICE = "streamingDevice"
	
	METER = "meter"
	
	AUXILIARY_SENDS = "auxiliarySends"
	
	API_CALLS = "apiCalls"
	
	SPATIAL_AUDIO = "spatialAudio"
	
	SPATIAL_AUDIO_RAYCASTING = "spatialAudioRaycasting"
	
	VOICE_INSPECTOR = "voiceInspector"
	
	AUDIO_OBJECTS = "audioObjects"
	
	GAME_SYNCS = "gameSyncs "


class EAudioObjectOptions(_StrEnum):
	"""Enumeration of defined members for an audio object return structure."""
	
	BUS_NAME = "busName"
	"""Name of the bus instance."""
	
	EFFECT_PLUGIN_NAME = "effectPluginName"
	"""Name of the effect plug-in after which the Audio Object was captured."""
	
	AUDIO_OBJECT_ID = "audioObjectID"
	"""The ID of the Audio Object."""
	
	BUS_PIPELINE_ID = "busPipelineID"
	"""The Pipeline ID of the Bus instance."""
	
	GAME_OBJECT_ID = "gameObjectID"
	"""The Game Object ID of the Bus instance."""
	
	GAME_OBJECT_NAME = "gameObjectName"
	"""The name of the Game Object of the Bus Instance."""
	
	AUDIO_OBJECT_NAME = "audioObjectName"
	"""The name of the Audio Object. Can be empty."""
	
	INSTIGATOR_PIPELINE_ID = "instigatorPipelineID"
	"""The pipeline ID of the instigator from which the Audio Object originates. Can be either a Bus instance or a
	Voice."""
	
	BUS_ID = "busID"
	"""The short ID of the Bus."""
	
	BUS_GUID = "busGUID"
	"""The GUID of the Bus."""
	
	SPATIALIZATION_MODE = "spatializationMode"
	"""The spatialization mode. Use Ak3DSpatializationMode to interpret the value."""
	
	X = "x"
	"""The X value of the Audio Object position."""
	
	Y = "y"
	"""The Y value of the Audio Object position."""
	
	Z = "z"
	"""The Z value of the Audio Object position."""
	
	SPREAD = "spread"
	"""The spread value (normalized) of the Audio Object."""
	
	FOCUS = "focus"
	"""The focus value (normalized) of the Audio Object."""
	
	CHANNEL_CONFIG = "channelConfig"
	"""The channel configuration of the Audio Object. Use AK::AkChannelConfig::Deserialize to deserialize the value."""
	
	EFFECT_CLASS_ID = "effectClassID"
	"""The Class ID of the effect after which the Audio Object was captured. Usage of AK_INVALID_UNIQUE_ID constant
	means that this Audio Object was captured before applying the first effect."""
	
	EFFECT_INDEX = "effectIndex"
	"""The index of the effect after which the Audio Object was captured."""
	
	METADATA = "metadata"
	"""Array of objects containing metadata of the Audio Object."""
	
	RMS_METER = "rmsMeter"
	"""Array of volume values (one per channel) for the RMS meter."""
	
	PEAK_METER = "peakMeter"
	"""Array of volume values (one per channel) for the Peak meter."""


class ETimeCursor(_StrEnum):
	"""Enum to identify one of the global profiler cursors"""
	
	USER = "user"
	"""The User Time Cursor is the one that can be manipulated by the user"""
	
	CAPTURE = "capture"
	"""Capture Time Cursor represents the latest time of the current capture"""


class EBusOptions(_StrEnum):
	"""Enumeration of defined members for a bus pipeline return structure. """
	
	PIPELINE_ID = "pipelineID"
	"""Pipeline ID of the bus."""
	
	MIX_BUS_ID = "mixBusID"
	"""Unique ID assigned to a mixing bus."""
	
	OBJECT_GUID = "objectGUID"
	"""Object GUID corresponding to the bus."""
	
	OBJECT_NAME = "objectName"
	"""Object Name corresponding to the bus."""
	
	GAME_OBJECT_ID = "gameObjectID"
	"""Game Object ID corresponding to the voice."""
	
	GAME_OBJECT_NAME = "gameObjectName"
	"""Game Object Name corresponding to the voice."""
	
	DEVICE_ID = "deviceID"
	"""Audio Output device ID."""
	
	VOLUME = "volume"
	"""Gain of the bus in dB."""
	
	DOWNSTREAM_GAIN = "downstreamGain"
	"""Gain from current bus down to output in dB."""
	
	VOICE_COUNT = "voiceCount"
	"""Number of voices routed to the bus."""
	
	EFFECT_COUNT = "effectCount"
	"""Number of effects on the bus."""
	
	DEPTH = "depth"
	"""Depth level of the bus in the pipeline."""


class ECPUStatisticsMembers(_StrEnum):
	"""Enumeration of defined members for a CPUStatisticInfo return structure."""
	
	ELEMENT_NAME = "elementName"
	"""The name of the element on which we calculate CPU usage."""
	
	ID = "id"
	"""Class ID of the element."""
	
	INSTANCES = "instances"
	"""An estimation of the number of instances of the element."""
	
	TYPE = "type"
	"""The type of element. For example, Codec, Source, Effect, Mixer or Sink."""
	
	PERCENT_INCLUSIVE = "percentInclusive"
	"""The percentage of CPU time spent in the execution of the element and those that it uses (calls)."""
	
	PERCENT_EXCLUSIVE = "percentExclusive"
	"""The percentage of CPU time spent only in the execution of the element itself."""
	
	MILLISECONDS_INCLUSIVE = "millisecondsInclusive"
	"""The milliseconds of CPU time spent in the execution of the element and those that it uses (calls)."""
	
	MILLISECONDS_EXCLUSIVE = "millisecondsExclusive"
	"""The milliseconds of CPU time spent only in the execution of the element itself."""


class EGameObjectRegistrationDataMembers(_StrEnum):
	"""Enumeration of defined members for a GameObjectRegistrationData return structure. """
	
	ID = "id"
	"""The ID of the game object."""
	
	NAME = "name"
	"""The name of the game object."""
	
	REGISTRATION_TIME = "registrationTime"
	"""The time at which the game object was registered."""
	
	UNREGISTRATION_TIME = "unregistrationTime"
	"""The time at which the game object was unregistered."""


class ELoadedMediaMembers(_StrEnum):
	"""Enumeration of defined members for a LoadedMedia return structure. """
	
	MEDIA_ID = "mediaId"
	"""The short ID of the media file"""
	
	FILE_NAME = "fileName"
	"""The name of the media file."""
	
	FORMAT = "format"
	"""The audio format of the media file."""
	
	SIZE = "size"
	"""The size (in bytes) of the media file."""
	
	SOUND_BANK = "soundBank"
	"""The name of the SoundBank that contains the media file."""


class EPerformanceMonitorMembers(_StrEnum):
	"""Enumeration of defined members for a PerformanceMonitorCounter return structure. """
	
	NAME = "name"
	"""Name of the counter as shown in Wwise Authoring."""
	
	ID = "id"
	"""Unique Id of the counter."""
	
	VALUE = "value"
	"""Value of counter at given time."""


class EActiveRTPCMembers(_StrEnum):
	"""Enumeration of defined members for an ActiveRTPCInfo return structure."""
	
	ID = "id"
	"""The ID (GUID) of the Game Parameter, LFO, Time, Envelope or MIDI Parameter object."""
	
	NAME = "name"
	"""The name of the Game Parameter, LFO, Time, Envelope or MIDI Parameter object. The name of the object."""
	
	GAME_OBJECT_ID = "gameObjectId"
	"""The Game Object associated with the RTPC scope, or AK_INVALID_GAME_OBJECT for global scope RTPCs."""
	
	VALUE = "value"
	"""The value of the Game Parameter, LFO, Time, Envelope or MIDI Parameter at the cursor time."""


class EVoicePipelineReturnOptions(_StrEnum):
	"""Enumeration of defined members for a voice pipeline return structure."""
	
	PIPELINE_ID = "pipelineID"
	"""Pipeline ID of the voice."""
	
	PLAYING_ID = "playingID"
	"""Playing ID of the voice."""
	
	SOUND_ID = "soundID"
	"""Short ID of the sound object corresponding to the voice."""
	
	GAME_OBJECT_ID = "gameObjectID"
	"""Game Object ID corresponding to the voice."""
	
	GAME_OBJECT_NAME = "gameObjectName"
	"""Game Object Name corresponding to the voice."""
	
	OBJECT_GUID = "objectGUID"
	"""Object GUID corresponding to the voice."""
	
	OBJECT_NAME = "objectName"
	"""Object Name corresponding to the voice."""
	
	PLAY_TARGET_ID = "playTargetID"
	"""Short ID of the play target object corresponding to the voice."""
	
	PLAY_TARGET_GUID = "playTargetGUID"
	"""GUID of the play target object corresponding to the voice."""
	
	PLAY_TARGET_NAME = "playTargetName"
	"""Name of the play target object corresponding to the voice."""
	
	BASE_VOLUME = "baseVolume"
	"""Voice volume in dB, including HDR attenuation."""
	
	GAME_AUX_SEND_VOLUME = "gameAuxSendVolume"
	"""Volume send to the auxiliary bus send in dB."""
	
	ENVELOPE = "envelope"
	"""Current analyzed envelope value in dB. 0 if unavailable."""
	
	NORMALIZATION_GAIN = "normalizationGain"
	"""Loudness normalization and make-up gain in dB."""
	
	LOW_PASS_FILTER = "lowPassFilter"
	"""Low-Pass Filter applied to the voice."""
	
	HIGH_PASS_FILTER = "highPassFilter"
	"""High-Pass Filter applied to the voice."""
	
	PRIORITY = "priority"
	"""Priority given to the voice."""
	
	IS_STARTED = "isStarted"
	"""If the voice has started."""
	
	IS_VIRTUAL = "isVirtual"
	"""If the voice is virtual."""
	
	IS_FORCED_VIRTUAL = "isForcedVirtual"
	"""If the voice was forced virtual."""


class ECaseStyle(_StrEnum):
	"""Enumeration of common case styles."""
	
	CAMEL = r"^[a-z]+[A-Za-z]*$"
	"""Tokens separated by capitalization, first word NOT capitalized (e.g. 'camelCase')."""
	
	KEBAB = r"^[a-z]+(-[a-z]+)*$"
	"""Tokens separated by hyphens (`-`; e.g. 'kebab-case')."""
	
	PASCAL = r"^[A-Z][a-zA-Z]+$"
	"""Tokens separated by capitalization, first word capitalized (e.g. 'PascalCase')."""
	
	SNAKE = r"^_?[a-z]+(_[a-z]+)*$"
	"""Tokens separated by underscores (`_`; 'snake_case' or '_snake_case'), all lower-case."""
	
	UPPER = r"^_?[A-Z]+(_[A-Z]+)*$"
	"""Tokens separated by underscores (`_`; 'UPPER_CASE' or '_UPPER_CASE'), all upper-case."""


class ELogChannel(_StrEnum):
	"""An enumeration of Wwise log channels."""
	
	SOUNDBANK_GENERATE = "soundbankGenerate"
	"""Log channel for messages related to the generation of SoundBanks."""
	
	CONVERSION = "conversion"
	"""Log channel for messages related to conversions."""
	
	COPY_PLATFORM_SETTINGS = "copyPlatformSettings"
	"""Log channel for messages related to platform settings."""
	
	WAAPI = "waapi"
	"""Log channel for messages related to the Wwise Authoring API."""
	
	PROJECT_LOAD = "projectLoad"
	"""Log channel for messages related to project data."""
	
	GENERAL = "general"
	"""Log channel for general messages."""
	
	SOURCE_CONTROL = "sourceControl"
	"""Log channel for messaged related to source control."""
	
	LUA = "lua"
	"""Log channel for messages related to Lua scripts."""


class ETransportExecuteActions(_StrEnum):
	"""An enumeration of possible transport execute actions."""
	
	PLAY = "play"
	"""Play"""
	
	STOP = "stop"
	"""Stop"""
	
	PAUSE = "pause"
	"""Pause"""
	
	PLAY_STOP = "playStop"
	"""Play stop"""
	
	PLAY_DIRECTLY = "playDirectly"
	"""Play directly"""


class ETransportState(_StrEnum):
	"""An enumeration of the available transport object states."""
	
	PLAYING = "playing"
	"""Transport object is playing."""
	
	STOPPED = "stopped"
	"""Transport object is stopped."""
	
	PAUSED = "paused"
	"""Transport object is paused."""
	
	NONE = "none"
	"""Transport object return is null."""


class ELogSeverity(_StrEnum):
	"""An enumeration of log item severity levels."""
	
	MESSAGE = "Message"
	"""Does not affect the integrity of the current operation."""
	
	WARNING = "Warning"
	"""Might affect the integrity of the current operation."""
	
	ERROR = "Error"
	"""Affects the integrity of the current operation."""
	
	FATAL_ERROR = "FatalError"
	"""Prevents the completion of the current operation."""


class ECaptureLogItemType(_StrEnum):
	"""An enumeration of capture log item types."""
	
	ERROR = "Error"
	"""Error capture log item."""
	
	WARNING = "Warning"
	"""Warning capture log item."""
	
	NOTIFICATION = "Notification"
	"""Notification capture log item type."""
	
	INTERACTIVE_MUSIC = "InteractiveMusic"
	"""InteractiveMusic capture log item type."""
	
	MIDI = "Midi"
	"""Midi capture log item type."""
	
	EXTERNAL_SOURCE = "ExternalSource"
	"""ExternalSource capture log item type."""
	
	MARKER = "Marker"
	"""Marker capture log item type."""
	
	STATE = "State"
	"""State capture log item type."""
	
	SWITCH = "Switch"
	"""Switch capture log item type."""
	
	SET_PARAMETER = "SetParameter"
	"""SetParameter capture log item type."""
	
	PARAMETER_CHANGED = "ParameterChanged"
	"""ParameterChanged capture log item type."""
	
	BANK = "Bank"
	"""Bank capture log item type."""
	
	PREPARE = "Prepare"
	"""Prepare capture log item type."""
	
	EVENT = "Event"
	"""Event capture log item type."""
	
	DIALOGUE_EVENT_RESOLVED = "DialogueEventResolved"
	"""DialogueEventResolved capture log item type."""
	
	ACTION_TRIGGERED = "ActionTriggered"
	"""ActionTriggered capture log item type."""
	
	ACTION_DELAYED = "ActionDelayed"
	"""ActionDelayed capture log item type."""
	
	MESSAGE = "Message"
	"""Message capture log item type."""
	
	API_CALL = "APICall"
	"""APICall capture log item type."""
	
	GAME_OBJECT_REGISTRATION = "GameObjectRegistration"
	"""GameObjectRegistration capture log item type."""


class ECaptureLogSeverity(_StrEnum):
	"""An enumeration of capture log item types."""
	
	NORMAL = "Normal"
	"""Normal execution."""
	
	MESSAGE = "Message"
	"""Shown in yellow in the capture log."""
	
	ERROR = "Error"
	"""Shown in red in the capture log."""


class EAttenuationCurveType(_StrEnum):
	"""An enumeration of curve types."""
	
	VOLUME_DRY_USAGE = "VolumeDryUsage"
	"""Volume"""
	
	VOLUME_WET_GAME_USAGE = "VolumeWetGameUsage"
	"""Aux Send (Game-Defined)"""
	
	VOLUME_WET_USER_USAGE = "VolumeWetUserUsage"
	"""Aux Send (User-Defined)"""
	
	LOW_PASS_FILTER_USAGE = "LowPassFilterUsage"
	"""Low-Pass Filter"""
	
	HIGH_PASS_FILTER_USAGE = "HighPassFilterUsage"
	"""High-Pass Filter"""
	
	SPREAD_USAGE = "SpreadUsage"
	"""Spread"""
	
	FOCUS_USAGE = "FocusUsage"
	"""Focus"""


class EInclusionOperation(_StrEnum):
	"""An enumeration of inclusion operations. Useful when getting/setting inclusions in SoundBanks."""
	
	ADD = "add"
	"""`Add` operation."""
	
	REMOVE = "remove"
	"""`Remove` operation."""
	
	REPLACE = "replace"
	"""`Replace` operation."""


class EInclusionFilter(_StrEnum):
	"""An enumeration of inclusion filters. Useful when getting/setting inclusions in SoundBanks."""
	
	EVENTS = "events"
	"""Inclusion filter for events."""
	
	STRUCTURES = "structures"
	"""Inclusion filter for structures (e.g. the hierarchy and assignments of a Switch Container)."""
	
	MEDIA = "media"
	"""Inclusion filter for media (the actual WAV/WEM files that are played at runtime)."""


class ENameConflictStrategy(_StrEnum):
	"""An enumeration of possible strategies for when dealing with name conflicts."""
	
	RENAME = "rename"
	"""Rename on conflict. This behaviour can be customized in Wwise."""
	
	REPLACE = "replace"
	"""Replace the name/object that already exists."""
	
	FAIL = "fail"
	"""Prevent the operation that caused the name conflict."""


class ESourceControlSearchFilter(_StrEnum):
	"""An enumeration of source control search filters."""
	
	ALL = "all"
	"""Displays all files in the Originals folder (default)."""
	
	USED = "used"
	"""Only displays files that are used in the project."""
	
	UNUSED = "unused"
	"""Only displays files that are not used in the project"""


class ESourceFileReturnOptions(_StrEnum):
	"""An enumeration of return options for source file operations."""
	
	IS_USED = "isUsed"
	"""Indicates if the file is used by a Wwise object."""
	
	USAGE = "usage"
	"""List the Wwise objects that use this file."""
	
	IS_MISSING = "isMissing"
	"""Indicates if the file is absent in the source manager"""
	
	FILE = "file"
	"""The files are in the list."""
	
	FOLDER = "folder"
	"""The folders are in the list."""


class EWaqlSelectExpression(_StrEnum):
	"""An enumeration of `select` expressions."""
	
	CHILDREN = "children"
	"""Returns the direct children of the object."""
	
	DESCENDANTS = "descendants"
	"""Returns all descendants of the object in a single sequence. The descendants include all children recursively."""
	
	THIS = "this"
	"""Returns the current object."""
	
	PARENT = "parent"
	"""Returns the direct parent of the object. Returns no object if the object does not have a parent."""
	
	ANCESTORS = "ancestors"
	"""Returns all ancestors of the object in a single sequence. The descendants include all parents recursively."""
	
	REFERENCES_TO = "referencesTo"
	"""Returns all objects having a reference to the current object."""
	
	OWNER = "owner"
	"""Returns the owner of the object. The owner is only set for "Custom" objects defined inside other objects."""
	
	WORK_UNIT = "workunit"
	"""Returns the Work Unit object used to persist with the current object."""
	
	MAX_DURATION_SOURCE = "maxDurationSource"
	"""Returns a JSON object containing the id of the Audio Source object that has the maximum playback duration
	(in seconds) for all descendants of the current object. The JSON object also includes the maximum duration value
	itself."""
	
	MAX_DURATION_SOURCE_OBJECT = "maxDurationSourceObject"
	"""Returns the Audio Source object that has the maximum playback duration (in seconds) for all descendants of the
	current object."""
	
	MAX_RADIUS_ATTENUATION = "maxRadiusAttenuation"
	"""Returns a JSON object containing the id of the attenuation object that has the maximum radius distance in all
	descendants of the current objects. The JSON object also contains the maximum radius distance value itself."""
	
	MAX_RADIUS_ATTENUATION_OBJECT = "maxRadiusAttenuationObject"
	"""Returns the attenuation object that has the maximum radius distance in all descendants of the current objects."""
	
	AUDIO_SOURCE_LANGUAGE = "audioSourceLanguage"
	"""Returns the language object that is used for the current Audio Source."""
	
	SWITCH_CONTAINER_CHILD_CONTEXT = "switchContainerChildContext"
	"""Returns the Switch Container context object associated with the current Switch Container object. The Switch
	Container context objects hold settings about the Switch Container associations."""


class EAttenuationCurveUsage(_StrEnum):
	"""An enumeration of different "usage states" for an attenuation curve."""
	
	NONE = "None"
	"""Curve is not used. More specifically, the curve has no points."""
	
	CUSTOM = "Custom"
	"""Curve is custom, meaning it has its own set of points."""
	
	USE_VOLUME_DRY = "UseVolumeDry"
	"""Curve uses the points from the 'VolumeDryUsage' curve."""


class EPropertyPasteMode(_StrEnum):
	"""An enumeration of paste modes for when pasting properties (e.g. Volume)."""
	
	REPLACE_ENTIRE = "replaceEntire"
	"""All elements in the lists of a target object are removed and all selected elements from the source's lists are
	copied."""
	
	ADD_REPLACE = "addReplace"
	"""For elements which are common to the source and a target, this mode will copy the one from the source, replacing
	the target's element."""
	
	ADD_KEEP = "addKeep"
	"""For elements which are common to the source and a target, this mode will retain the element in the target"""


class ERtpcMode(_StrEnum):
	"""An enumeration of RTPC modes."""
	
	NONE = "None"
	"""No RTPC or RTPC not supported."""
	
	ADDITIVE = "Additive"
	"""RTPCs are supported. Multiple RTPCs are combined via addition."""
	
	EXCLUSIVE = "Exclusive"
	"""Only a single RTPC is supported."""
	
	MULTIPLICATIVE = "Multiplicative"
	"""RTPCs are supported. Multiple RTPCs are combined via multiplication."""


class EWwiseBuildPlatform(_StrEnum):
	"""An enumeration of all platforms on which Wwise can be built."""
	
	X64 = "x64"
	"""Windows (64-bit architecture)."""
	
	WIN32 = "win32"
	"""Windows (32-bit architecture)."""
	
	MACOSX = "macosx"
	"""Mac OS X."""
	
	LINUX = "linux"
	"""Any linux-based distribution."""


class EMultiPositionType(_IntEnum):
	"""An enumeration of multi-position types."""
	
	SINGLE_SOURCE = 0,
	"""Used for normal sounds, not expected to pass to AK::SoundEngine::SetMultiplePosition() (if done, only the first
	position will be used)."""
	
	MULTI_SOURCES = 1,
	"""Simulate multiple sources in one sound playing, adding volumes. For instance, all the torches on your level
	emitting using only one sound."""
	
	MULTI_DIRECTIONS = 2
	"""Simulate one sound coming from multiple directions. Useful for repositionning sounds based on wall openings or
	to simulate areas like forest or rivers (in combination with spreading in the attenuation of the sounds)."""
