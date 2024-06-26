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


class ECurveInterpolation(_IntEnum):
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
	"""The class ID (e.g. the ClassID of AuxBus is 3997712). Refer to the Wwise Objects Reference for more information."""
	
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
	"""Whether the object is included. Not being included means it will not be converted or included in SoundBanks or other data."""
	
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
	"""The type of Work Unit (e.g. actual Work Unit vs Physical Folder). This assumes the object in question is a Work Unit."""

	def __hash__(self) -> int:
		""":return: The enum value, hashed."""
		return self.value.__hash__()


class EObjectType(tuple[int, int, str], _Enum):
	"""An enumeration of class IDs for all different Wwise objects."""

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
	OBJECT_SETTING_ASSOC = 24, 1572880, "ObjectSettingAssoc"
	PANNER = 42, 2752528, "Panner"
	PATH_2D = 11, 720912, "Path2d"
	PLATFORM = 69, 4522000, "Platform"
	PLUGIN_DATA_SOURCE = 54, 3538960, "PluginDataSource"
	POSITION = 12, 786448, "Position"
	PROJECT = 3, 196624, "Project"
	QUERY = 32, 2097168, "Query"
	RANDOM_SEQUENCE_CONTAINER = 9, 589840, "RandomSequenceContainer"
	RTPC = 22, 1441808, "Rtpc"
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
		for member in cls:
			if member.get_plugin_id() == plugin_id:
				return member
		raise ValueError(f"No {cls.__name__} member with plugin_id={plugin_id}")

	@classmethod
	def from_class_id(cls, class_id: int):
		for member in cls:
			if member.get_class_id() == class_id:
				return member
		raise ValueError(f"No {cls.__name__} member with class_id={class_id}")

	@classmethod
	def from_type_name(cls, type_name: str):
		for member in cls:
			if member.get_type_name() == type_name:
				return member
		raise ValueError(f"No {cls.__name__} member with type_name={type_name}")

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

	MULTIPLE_SELECTION_SINGLE_PROCESS_SPACE_SEPARATED = "MultipleSelectionSingleProcess"
	"""MultipleSelectionSingleProcessSpaceSeparated: program is started once with variables expanded to space separated 
	arguments, each enclosed in double-quotes."""

	MULTIPLE_SELECTION_MULTIPLE_PROCESSES = "MultipleSelectionMultipleProcesses"
	"""MultipleSelectionMultipleProcesses: program is started once per selected item, in parallel. Each running instance 
	receives one selected item."""

	def __hash__(self) -> int:
		""":return: The enum value, hashed."""
		return self.value.__hash__()