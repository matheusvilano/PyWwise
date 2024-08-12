from dataclasses import dataclass as _dataclass, field as _field
from pathlib import Path as _Path
from typing import Any as _Any, Self as _Self
from pywwise.enums import (EAttenuationCurveType, EAttenuationCurveUsage, EBasePlatform, ECaptureLogItemType,
                           ECaptureLogSeverity, EAttenuationCurveShape, ELogSeverity, EObjectType, EReturnOptions,
                           ERtpcMode, EStartMode, EInclusionFilter, EWwiseBuildPlatform)
from pywwise.statics import EnumStatics
from pywwise.types import GameObjectID, GUID, Name, OriginalsPath, PlayingID, ProjectPath, RegexPattern, ShortID, \
	SystemPath


@_dataclass
class Vector2:
	"""A 2-dimensional vector."""
	
	x: float
	"""X axis."""
	
	y: float
	"""Y axis."""
	
	@classmethod
	def get_zero(cls) -> _Self:
		""":return: A Vector3 instance with x, y, and z all set to 0.0."""
		return Vector2(0.0, 0.0)


@_dataclass
class Vector3(Vector2):
	"""A 3-dimensional vector."""
	
	z: float
	"""Z axis."""
	
	@classmethod
	def get_zero(cls) -> _Self:
		""":return: A Vector3 instance with x, y, and z all set to 0.0."""
		return Vector3(0.0, 0.0, 0.0)


@_dataclass
class Rect:
	"""Data-only representation of a rectangle. In some contexts, the position (x, y) can be discarded/ignored."""
	
	x: int
	"""Left position of capture region."""
	
	y: int
	"""Top position of capture region."""
	
	width: int
	"""Width of capture region."""
	
	height: int
	"""Height of capture region."""
	
	@staticmethod
	def get_zero():
		""":return: A CaptureRect instance with x, y, width, and height all set to 0."""
		return Rect(0, 0, 0, 0)


@_dataclass
class AuxSendValue:
	"""Data-only class representing an aux send value."""
	
	listener: GameObjectID
	"""The ID of the associated listener."""
	
	aux_bus: GUID | Name | ShortID
	"""The GUID, name, or short ID of the Aux Bus."""
	
	control_value: float
	"""The intended value."""


@_dataclass
class PlatformInfo:
	"""Structure for storing basic platform info. Useful when creating a new project or adding a new platform to a project."""
	
	name: str
	"""The name of this platform."""
	
	base_platform: EBasePlatform
	"""The base platform."""
	
	guid: GUID = None
	"""The GUID of this platform."""
	
	def __hash__(self):
		""":return: The PlatformInfo hash."""
		return hash(self.name)


@_dataclass
class ExternalSourceInfo:
	"""Data-only class storing information about an external source."""
	
	input: _Path
	"""The path where the external source's WAV file is located."""
	
	platform: Name | GUID
	"""The name or GUID of the platform this external source is associated with."""
	
	output: _Path
	"""The output path of the external source's WEM (after conversions)."""
	
	@property
	def dictionary(self) -> dict[str, str]:
		as_dict = {"input": self.input, "platform": self.platform}
		if self.output is not None:
			as_dict["output"] = self.output
		return as_dict


@_dataclass
class WwiseObjectInfo:
	"""Data-only class storing core information about a Wwise object."""
	
	guid: GUID
	"""The GUID of the wwise object."""
	
	name: Name
	"""The name of the Wwise object. Depending on the type, it may be unique."""
	
	type: EObjectType
	"""The Wwise object type."""
	
	path: ProjectPath
	"""The project path of the Wwise object."""
	
	other: dict[EReturnOptions | str, _Any] = _field(default_factory=dict)
	"""A dictionary containing other information, if any. Keys are always strings, but can be accessed using the enum
	EReturnOptions instead."""
	
	def __hash__(self):
		""":return: The WwiseObjectInfo hash."""
		return hash(self.guid)
	
	@classmethod
	def from_dict(cls, kvpairs: dict[str, _Any]) -> _Self:
		"""
		Uses a dictionary to initialize a new instance.
		:param kvpairs: A dictionary to extract information from.
		:return: A new instance with id, name, type, and path populated. No additional properties.
		"""
		guid = GUID(kvpairs["id"]) if kvpairs.get("id") is not None else GUID.get_null()
		name = Name(kvpairs["name"]) if kvpairs.get("name", "") != "" else Name.get_null()
		etype = EObjectType.from_type_name(kvpairs["type"]) if kvpairs.get("type") is not None else EObjectType.UNKNOWN
		path = ProjectPath(kvpairs["path"]) if kvpairs.get("path", "") != "" else ProjectPath.get_null()
		return cls(guid, name, etype, path)


@_dataclass
class TransportObjectInfo:
	"""Data-only class storing information about a Wwise transport object."""
	
	object: GUID
	"""The ID (GUID) of the object controlled by the transport object."""
	
	game_object: int
	"""The game object used by the transport object. Unsigned integer 64-bit"""
	
	transport: int
	"""Transport object ID. Unsigned Integer 32-bit."""
	
	def __hash__(self):
		""":return: The WwiseTransportObjectInfo hash."""
		return hash(self.object)
	
	@classmethod
	def from_dict(cls, kvpairs: dict[str, _Any]) -> _Self:
		"""
		Uses a dictionary to initialize a new instance.
		:param kvpairs: A dictionary to extract information from.
		:return: A new instance with object GUID, game object, and transport object populated. No additional properties.
		"""
		obj = GUID(kvpairs["object"]) if kvpairs.get("object") is not None else GUID.get_null()
		game_object = int(kvpairs["gameObject"]) if kvpairs.get("gameObject") is not None else -1
		transport = int(kvpairs["transport"]) if kvpairs.get("transport") is not None else -1
		return cls(obj, game_object, transport)


@_dataclass
class ContextMenuInfo:
	"""Data-only class storing information about a command's context menu, which is part of an add-on command's
	arguments."""
	
	base_path: str = None
	"""Defines a forward-separated path for the parent sub menus. If empty, the menu is inserted at the first level."""
	
	visible_for: set[EObjectType] = None
	"""Defines a comma-separated list of the object types for which the item is visible. Refer to Wwise Objects 
	Reference for the list of types supported. If empty, any type is allowed."""
	
	enabled_for: set[EObjectType] = None
	"""Defines a comma-separated list of the object types for which the item is enabled. Refer to Wwise Objects 
	Reference for the list of types supported. If empty, any type is allowed."""
	
	def __hash__(self):
		""":return: The ContextMenuInfo hash."""
		return hash(str(self.__dict__))
	
	@property
	def dictionary(self) -> dict[str, str]:
		as_dict = dict()
		if self.base_path is not None:
			as_dict["basePath"] = self.base_path
		if self.visible_for is not None:
			as_dict["visibleFor"] = ",".join([obj.get_type_name() for obj in self.visible_for])
		if self.enabled_for is not None:
			as_dict["enabledFor"] = ",".join([obj.get_type_name() for obj in self.enabled_for])
		return as_dict


@_dataclass
class MainMenuInfo:
	"""Data-only class storing information about a command's main menu, which is part of an add-on command's argument"""
	
	main_menu_base_path: str
	"""Defines a forward-separated path for the parent sub menus. It must at least define one level, which is associated 
	to the top menu."""
	
	def __hash__(self):
		""":return: The ContextMenuInfo hash."""
		return hash(str(self.__dict__))
	
	@property
	def dictionary(self) -> dict[str, str]:
		as_dict = dict()
		as_dict["basePath"] = self.main_menu_base_path
		return as_dict


@_dataclass
class CommandInfo:
	"""Data-only class storing information about an add-on command."""
	
	id: str
	"""Defines a human readable unique ID for the command. To reduce risk of ID conflicts, please use a concatenation of 
	the author name, the product name and the command name (e.g. 'mv.pywwise.do_something)."""
	
	display_name: str
	"""Defines the name displayed in the user interface. (e.g. Do Something)"""
	
	program: str = None
	"""Defines the program or script to run when the command is executed. Arguments are specified in 'args'. Note that 
	common directories variables can be used, such as ${CurrentCommandDirectory}."""
	
	lua_script: str = None
	"""Defines a lua script file path to run inside Wwise process when the command is executed. Arguments are specified 
	in 'args'. Note that common directories variables can be used, such as ${CurrentCommandDirectory}."""
	
	lua_paths: list[str] = None
	"""Defines an array of paths to be used to load additional lua scripts. Here is an example of a lua path 
	C:/path_to_folder/?.lua. Note that common directories variables can be used, such as ${CurrentCommandDirectory}."""
	
	lua_selected_return: list[str] = None
	"""Specifies an array of return expressions for the selected objects in Wwise. This will be available to the script 
	in a lua table array in wa_args.selected. Several values provided for the option."""
	
	start_mode: EStartMode = EStartMode.SINGLE_SELECTION_SINGLE_PROCESS
	"""Specifies how to expand variables in the arguments field in case of multiple selection in the Wwise user 
	interface."""
	
	args: str = None
	"""Defines the arguments. Refer to the documentation for the list of supported built-in variables. Note that in the 
	event of a multiple selection, the variables are expanded based on the startMode field. Note that common directories 
	variables can be used, such as ${CurrentCommandDirectory}."""
	
	cwd: str = None
	"""Defines the current working directory to execute the program. Note that common directories variables can be used, 
	such as ${CurrentCommandDirectory}."""
	
	default_shortcut: str = None
	"""Defines the shortcut to use by default for this command. If the shortcut conflicts, it won't be used. This 
	shortcut can be changed in the Keyboard Shortcut Manager."""
	
	redirect_outputs: bool = False
	"""Defines if the standard output streams of the program (stdout + stderr) should be redirected and logged to Wwise 
	on termination. The value is of boolean type and false by default."""
	
	context_menu: ContextMenuInfo = None
	"""If present, specify how the command is added to Wwise context menus. If empty, no context menu is added."""
	
	main_menu: MainMenuInfo = None
	"""If present, specify how the command is added to Wwise main menus. If empty, no main menu entry is added."""
	
	def __hash__(self):
		""":return: The CommandInfo ID hash."""
		return hash(self.id)
	
	@property
	def dictionary(self) -> dict[str, str | bool | ContextMenuInfo | MainMenuInfo]:
		as_dict = dict()
		as_dict["id"] = self.id
		as_dict["displayName"] = self.display_name
		as_dict["redirectOutputs"] = self.redirect_outputs
		as_dict["startMode"] = self.start_mode.value
		if self.program is not None:
			as_dict["program"] = self.program
		if self.lua_script is not None:
			as_dict["luaScript"] = self.lua_script
		if self.lua_paths is not None:
			as_dict["luaPaths"] = self.lua_paths
		if self.lua_selected_return is not None:
			as_dict["luaSelectedReturn"] = self.lua_selected_return
		if self.args is not None:
			as_dict["args"] = self.args
		if self.cwd is not None:
			as_dict["cwd"] = self.cwd
		if self.default_shortcut is not None:
			as_dict["defaultShortcut"] = self.default_shortcut
		if self.context_menu is not None:
			as_dict["contextMenu"] = self.context_menu.dictionary
		if self.main_menu is not None:
			as_dict["mainMenu"] = self.main_menu.dictionary
		return as_dict


@_dataclass
class SoundBankInfo:
	"""A SoundBank's information."""
	
	name: str
	"""The name of the SoundBank."""
	
	events: list[str] = None
	"""List of events included in this SoundBank."""
	
	aux_busses: list[str] = None
	"""List of AuxBus included in this SoundBank."""
	
	inclusions: list[str] = None
	"""Inclusion type to use for this SoundBank."""
	
	rebuild: bool = False
	"""Force rebuild of this particular SoundBank."""
	
	def __hash__(self) -> int:
		""":return: The SoundBankInfo hash."""
		return hash(self.name)
	
	@property
	def dictionary(self) -> dict[str, bool | str | list[str]]:
		""":return: The instance, represented as a dictionary."""
		as_dict = {"name": self.name, "rebuild": self.rebuild}
		if self.events is not None:
			as_dict["events"] = self.events
		if self.aux_busses is not None:
			as_dict["auxBusses"] = self.aux_busses
		if self.inclusions is not None:
			as_dict["inclusions"] = self.inclusions
		return as_dict


@_dataclass
class SoundBankInclusion:
	"""Represents a SoundBank inclusion row."""
	
	obj: GUID | tuple[EObjectType, Name] | ProjectPath
	"""The GUID, ProjectPath, or Name of the object to add/remove from the SoundBank's inclusion list.
	NOTE: Name is only supported for globally-unique names (e.g. Events, State Groups, etc.)."""
	
	filters: list[EInclusionFilter]
	"""Specifies what relations are being included. Possible Values: events, structures, media"""
	
	def __hash__(self) -> int:
		""":return: The instance, hashed."""
		return hash(self.obj)
	
	@property
	def dictionary(self) -> dict[str, list[str]]:
		""":return: The instance, represented as a dictionary."""
		as_dict = {
			"object": self.obj if not isinstance(self.obj, tuple) else f"{self.obj[0].get_type_name()}:{self.obj[1]}",
			"filter": list(set(self.filters))}
		return as_dict


@_dataclass
class LogItem:
	"""A log item."""
	
	severity: ELogSeverity
	"""The severity of the message."""
	
	time: int
	"""Number of seconds elapsed since midnight (00:00:00), January 1, 1970, Coordinated Universal Time (UTC),
	according to the system clock."""
	
	id: str
	"""The message ID for the log item."""
	
	description: str
	"""The description of the log item."""
	
	@classmethod
	def from_dict(cls, kvpairs: dict[str, _Any]) -> _Self:
		"""
		Uses a dictionary to initialize a new instance.
		:param kvpairs: A dictionary to extract information from.
		:return: A new instance with `severity`, `time`, `id`, and `description`.
		"""
		severity = EnumStatics.from_value(ELogSeverity, kvpairs["severity"])
		time = kvpairs["time"]
		log_id = kvpairs["messageId"]
		description = kvpairs["message"]
		return cls(severity, time, log_id, description)


@_dataclass
class SwitchContainerAssignment:
	"""Represents a switch container assigned (the relationship between a child object and a state/switch)."""
	
	child: GUID
	"""The child object of a Switch Container, which is linked (assigned) to a State or Switch value."""
	
	state_or_switch: GUID
	"""The State or Switch value to switch the child object is linked (assigned) to."""


@_dataclass
class CaptureLogItem:
	"""A console log item."""
	
	type: ECaptureLogItemType
	"""The type of the capture log item."""
	
	time: int
	"""Number of seconds elapsed since midnight (00:00:00), January 1, 1970, Coordinated Universal Time (UTC),
	according to the system clock."""
	
	description: str
	"""The description of the log item."""
	
	severity: ECaptureLogSeverity
	"""The severity of the message."""
	
	wwise_object_id: GUID = GUID.get_null()
	"""The GUID of the object for the entry."""
	
	wwise_object_name: Name = Name.get_null()
	"""The name of the object for the entry."""
	
	wwise_object_short: ShortID = ShortID.get_null()
	"""The short ID of the object for the entry."""
	
	game_object_id: GameObjectID = GameObjectID.get_null()
	"""The game object ID for the entry."""
	
	game_object_name: Name = Name.get_null()
	"""The game object name for the entry."""
	
	playing_id: PlayingID = PlayingID.get_null()
	"""The playing ID for the entry."""
	
	error_code_name: str = ""
	"""The error code name for the entry (e.g. `ErrorCode_VoiceStarting`)."""


@_dataclass
class SoundBankData:
	"""A dataclass that represents a SoundBank (the actual data)."""
	
	b64data: str
	"""Data of the SoundBank encoded in base64."""
	
	size: int
	"""Size of the SoundBank data when decoded."""


@_dataclass
class SoundBankGenerationInfo:
	"""Contains information about a SoundBank's generation."""
	
	sound_bank: WwiseObjectInfo
	"""The generated SoundBank."""
	
	platform: Name
	"""The name of the platform for which the SoundBank was generated."""
	
	language: Name = Name.get_null()
	"""The name of the language for which the SoundBank was generated. Only present when generating a SoundBank for a
	specific language."""
	
	bank_data: SoundBankData = _field(default=SoundBankData)
	"""SoundBank data object containing the actual data encoded in base64 and the size."""
	
	banks_info: list[dict[str, _Any]] = _field(default_factory=list)
	"""All the info for the generated SoundBank."""
	
	plugins_info: dict[str, str | list[dict[str, str]]] = _field(default_factory=dict)
	"""PluginInfo file info."""
	
	error_message: str = ""
	"""The error message, if an error occurred. Only present if an error occurred."""


@_dataclass
class WwiseObjectWatch:
	"""Represents a watch. Used for setting up the `ak.wwise.core.object.property_changed` event. For the specified
	GUID, changes to any of the specified properties will trigger the event."""
	
	guid: GUID
	"""The GUID of the object to watch."""
	
	properties: tuple[str]
	"""A collection of properties names to watch."""


@_dataclass
class SourceControlStatus:
	"""Represents a file's source control status."""
	
	status: str
	"""A description of the status."""
	
	owner: str
	"""The name of the file's owner."""


@_dataclass
class SourceFileInfo:
	"""Stores source control and project information about a source file."""
	
	path: OriginalsPath
	"""The absolute path of the source file."""
	
	usage: tuple[WwiseObjectInfo, ...]
	"""The Wwise objects that use the source file."""
	
	is_missing: bool
	"""Indicates if the file is absent in the source manager."""
	
	@property
	def is_used(self) -> bool:
		"""
		Whether the source file is currently used in the project.
		:return: `True` if `usage` is not empty; else, `False`.
		"""
		return bool(self.usage)


@_dataclass
class WaqlCondition:
	"""A dataclass representing a WAQL condition (e.g. `Volume = 0.0`)."""
	
	property_name: str
	"""The name of the property to evaluate."""
	
	bool_operator: str
	"""The bool operator to use. Supported operators: `=`, `!=`, `<`, `<=`, `>`, `>=`, `:`, `!`. Common aliases are
	also supported (e.g. `&&`) by PyWwise. Invalid values will not throw runtime errors, but are still logical
	errors."""
	
	value_or_ref_or_regex: bool | int | float | str | tuple[EObjectType, Name] | ProjectPath | GUID | RegexPattern
	"""The value or the reference to use in the evaluation. Regex IS supported, but only when passing a `RegexPattern`
	(or `re.Pattern`) object."""


@_dataclass
class GraphPoint2D:
	"""A dataclass describing a point on a 2D graph."""
	
	position: tuple[Vector2]
	"""The position of the point on the graph."""
	
	shape: EAttenuationCurveShape = EAttenuationCurveShape.LINEAR
	"""The shape formed by the point on the graph."""


@_dataclass
class AttenuationCurve:
	"""A dataclass representing an attenuation curve (e.g. a Low-Pass Filter in an attenuation shareset)."""
	
	points: tuple[GraphPoint2D, ...]
	"""A collection of points on the graph."""
	
	usage: EAttenuationCurveUsage
	"""The attenuation curve usage."""
	
	etype: EAttenuationCurveType
	"""The type of the attenuation curve."""


@_dataclass
class PropertyInfo:
	"""A dataclass representing information about a property."""
	
	name: str
	"""The name of the property."""
	
	display_name: str
	"""The property's display name, as used in the Wwise UI."""
	
	audio_engine_id: int
	"""The audio engine ID of the property."""
	
	default: _Any
	"""The property's default value."""
	
	stype: str
	"""The name of the property's data type."""
	
	rtpc_mode: ERtpcMode
	"""The rtpc mode supported by the property."""
	
	supports_unlinking: bool | None
	"""Whether the property supports unlinking. If this information is unknown, the value is `None` instead."""
	
	supports_randomizer: bool | None
	"""Whether the property supports randomizers. If this information is unknown, the value is `None` instead."""


@_dataclass
class WwiseVersion:
	"""A dataclass representing a Wwise version."""
	
	display_name: str
	"""Wwise version name."""
	
	year: int
	"""Version year. Range: [2000,2100]."""
	
	major: int
	"""Version's major number Range: [0,100]."""
	
	minor: int
	"""Version's minor number. Range: [0,100]."""
	
	build: int
	"""Build number. Range: [1,*]."""
	
	nickname: str
	"""Special name given to a version."""
	
	schema: int
	"""Schema version for the Wwise Project and Work Units. Range: [1,*]."""


@_dataclass
class WwiseDirectories:
	"""A dataclass representing the collection of directories used by Wwise."""
	
	install: SystemPath
	"""The root directory of Wwise. This is the installation directory."""
	
	authoring: SystemPath
	"""The Wwise Authoring root directory."""
	
	bin: SystemPath
	"""The bin directory, where Wwise.exe is located."""
	
	help: SystemPath
	"""The help directory."""
	
	user: SystemPath
	"""The Wwise user data directory root."""


@_dataclass
class GlobalWwiseInfo:
	"""A dataclass representing global information about Wwise."""
	
	session_id: GUID
	"""Wwise session id."""
	
	api_version: float
	"""Version of the Wwise Authoring API. Range: [1,*]."""
	
	display_name: str
	"""Wwise display name."""
	
	branch: str
	"""Branch built."""
	
	copyright: str
	"""Copyright information."""
	
	version: WwiseVersion
	"""Wwise version object."""
	
	is_debug_build: bool
	"""Indicates if the Wwise build is a release build (`False`) or debug build (`True`)."""
	
	build_platform: EWwiseBuildPlatform
	"""The platform on which Wwise was built."""
	
	command_line: bool
	"""Whether Wwise is running in command line."""
	
	process_id: int
	"""The process identifier of Wwise."""
	
	process_path: str
	"""The process path of Wwise."""
	
	directories: WwiseDirectories
	"""Collection of directories used by Wwise."""
