# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass as _dataclass, field as _field
from types import NoneType as _NoneType
from typing import Any, Any as _Any, Self as _Self

from pywwise.aliases import ListOrTuple, RegexPattern, SystemPath
from pywwise.enums import (EAttenuationCurveShape, EAttenuationCurveType, EAttenuationCurveUsage, EAudioObjectOptions,
                           EBasePlatform, EBusOptions, ECaptureLogItemType, ECaptureLogSeverity, EInclusionFilter,
                           ELogSeverity, EObjectType, EReturnOptions, ERtpcMode, EStartMode,
                           EVoicePipelineReturnOptions, EWwiseBuildConfiguration, EWwiseBuildPlatform)
from pywwise.primitives import GameObjectID, GUID, Name, OriginalsPath, PlayingID, ProjectPath, ShortID
from pywwise.statics import EnumStatics


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
    
    name: str | Name
    """The name of this platform."""
    
    base: EBasePlatform
    """The base platform."""
    
    guid: GUID = None
    """The GUID of this platform."""
    
    sound_bank_path: SystemPath = None
    """The path on which the SoundBank files are generated for this platform."""
    
    copied_media_path: SystemPath = None
    """The path on which the SoundBank media files are generated for this platform."""
    
    def __hash__(self):
        """:return: The PlatformInfo hash."""
        return hash(self.name)


@_dataclass
class ExternalSourceInfo:
    """Data-only class storing information about an external source."""
    
    input: SystemPath
    """The path where the external source's WAV file is located."""
    
    platform: Name | GUID
    """The name or GUID of the platform this external source is associated with."""
    
    output: SystemPath
    """The output path of the external source's WEM (after conversions)."""
    
    @property
    def dictionary(self) -> dict[str, str]:
        as_dict = {"input": str(self.input), "platform": str(self.platform)}
        if self.output is not None:
            as_dict["output"] = str(self.output)
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
    
    filters: tuple[EInclusionFilter, ...]
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
class AudioObjectMetadata:
    """ Contains information about the metadata associated with an audio object."""
    
    metadata_class_id: int
    """The class ID of the metadata. Unsigned Integer 32-bit. Range: [0,4294967295]."""
    
    source_short_id: ShortID = _field(default=ShortID.get_null())
    """The short ID of the source object. Unsigned Integer 32-bit. Range: [0,4294967295]."""
    
    metadata_name: Name = _field(default=Name.get_null())
    """The name of the metadata."""
    
    source_id: GUID = _field(default=GUID.get_null())
    """The ID (GUID) of the source object."""
    
    source_name: Name = _field(default=Name.get_null())
    """The name of the source object."""
    
    def __hash__(self):
        """:return: The AudioObjectMetadata hash."""
        return hash(self.source_short_id)


@_dataclass
class AudioObjectInfo:
    """Contains information about an audio object captured in the profiler."""
    
    audio_object_id: int
    """The ID of the Audio Object.Unsigned Integer 64-bit. Range: [0,18446744073709551615]."""
    
    bus_pipeline_id: int
    """The Pipeline ID of the Bus instance. Unsigned Integer 32-bit. Range: [0,4294967295]."""
    
    instigator_pipeline_id: int
    """The pipeline ID of the instigator from which the Audio Object originates. Can be either a Bus instance or a
    Voice. Unsigned Integer 32-bit. Range: [0,4294967295]."""
    
    effect_class_id: int
    """The Class ID of the effect after which the Audio Object was captured. Usage of AK_INVALID_UNIQUE_ID constant
    means that this Audio Object was captured before applying the first effect. Unsigned Integer 32-bit.
    Range: [0,4294967295]"""
    
    other: dict[EAudioObjectOptions | str, _Any] = _field(default_factory=dict)
    """A dictionary containing other information, if any. Keys are always strings, but can be accessed using the enum
    EAudioObjectOptions instead."""
    
    def __hash__(self):
        """:return: The AudioObject hash."""
        return hash(self.audio_object_id)


@_dataclass
class BusPipelineInfo:
    """Contains information about an audio bus captured in the profiler."""
    
    pipeline_id: int
    """Pipeline ID of the bus. Unsigned Integer 32-bit. Range: [0,4294967295]"""
    
    game_object_id: GameObjectID
    """Game Object ID corresponding to the voice. Unsigned Integer 64-bit. Range: [0,18446744073709551615]"""
    
    object_guid: GUID
    """Object GUID corresponding to the bus. An object GUID of the form: {aabbcc00-1122-3344-5566-77889900aabb}."""
    
    other: dict[EBusOptions | str, _Any] = _field(default_factory=dict)
    """A dictionary containing other information, if any. Keys are always strings, but can be accessed using the enum
    EBusOptions instead."""
    
    def __hash__(self):
        """:return: The BusPipelineInfo hash."""
        return hash(self.pipeline_id)


@_dataclass
class CPUStatisticsInfo:
    """Information about the amount of CPU percentage used by each element."""
    
    element_name: str
    """The name of the element on which we calculate CPU usage."""
    
    class_id: int
    """Class ID of the element."""
    
    instances: int
    """An estimation of the number of instances of the element."""
    
    type: str
    """The type of element. Examples: Codec, Source, Effect, Mixer, Sink, etc."""
    
    percent_inclusive: float
    """The percentage of CPU time spent in the execution of the element and those that it uses (calls)."""
    
    percent_exclusive: float
    """The percentage of CPU time spent only in the execution of the element itself."""
    
    milliseconds_inclusive: float
    """The milliseconds of CPU time spent in the execution of the element and those that it uses (calls)."""
    
    milliseconds_exclusive: float
    """The milliseconds of CPU time spent only in the execution of the element itself."""


@_dataclass
class GameObjectRegistrationData:
    """Data of a profiled game object and its registration data."""
    
    id: GameObjectID
    """The ID of the game object. Unsigned Integer 64-bit. Range: [0,18446744073709551615]."""
    
    name: str
    """The name of the game object."""
    
    registration_time: int
    """The time at which the game object was registered. Integer 32-bit. Range: [-2147483648,2147483647]."""
    
    unregistration_time: int
    """The time at which the game object was unregistered. Integer 32-bit. Range: [-2147483648,2147483647]."""


@_dataclass
class LoadedMediaInfo:
    """Information about a media file loaded into memory as a result of the PrepareEvent() and PrepareGameSyncs()
    functions."""
    
    media_id: ShortID
    """The short ID of the media file."""
    
    file_name: Name
    """The name of the media file."""
    
    audio_format: str
    """The audio format of the media file."""
    
    size: int
    """The size (in bytes) of the media file."""
    
    sound_bank: Name
    """The name of the SoundBank that contains the media file."""


@_dataclass
class PerformanceMonitorCounterInfo:
    """Information about a performance monitor counter and its value."""
    
    name: str
    """Name of the counter as shown in Wwise Authoring."""
    
    identifier: str
    """Unique identifier of the counter."""
    
    value: float
    """Value of counter at given time. If invalid, value will be equivalent to `float("-inf")`."""


@_dataclass
class ActiveRTPCInfo:
    """Information about an active RTCP associated with a playing voice."""
    
    guid: GUID
    """The ID (GUID) of the Game Parameter, LFO, Time, Envelope or MIDI Parameter object. An object GUID of the form:
    {aabbcc00-1122-3344-5566-77889900aabb}."""
    
    name: Name
    """The name of the Game Parameter, LFO, Time, Envelope or MIDI Parameter object. The name of the object."""
    
    game_object_id: GameObjectID
    """The Game Object associated with the RTPC scope, or AK_INVALID_GAME_OBJECT for global scope RTPCs. A game object
    ID, unsigned integer 64-bit. Range: [0,18446744073709551615]."""
    
    value: float
    """The value of the Game Parameter, LFO, Time, Envelope or MIDI Parameter at the cursor time. If invalid, the value
    will be equivalent to `float("-inf")`."""


@_dataclass
class StreamObjectInfo:
    """Data-only class storing information about how each of the streams is managed by the Wwise sound engine."""
    
    device_name: Name
    """The name of the device from which the stream emanates."""
    
    stream_name: Name
    """The name given to the stream."""
    
    file_size: int
    """The size of the file being streamed."""
    
    file_position: float
    """The position of the stream within the file, given as a percentage."""
    
    priority: int
    """The priority of the stream."""
    
    bandwidth_total: int
    """The rate at which the file was streamed in the last profiling frame. This value takes all transfers into account,
    including transfers that occurred from the Stream Manager's cache."""
    
    bandwidth_low_level: int
    """The rate at which the file was streamed in the last profiling frame. Unlike the Total Bandwidth field, this field
    value considers transfers that occurred from within the low-level device."""
    
    referenced_memory: int
    """The amount of memory that is referenced by the stream. This excludes memory used for I/O transfers. It can be
    seen as a measure of how much data the stream may grant to the sound engine at any given time."""
    
    estimated_throughput: int
    """The estimated throughput of the stream. The sound engine estimates the rate at which it consumes data from a
    stream according to its encoding format and number of channels."""
    
    active: bool
    """Indicates True if the stream was active at least once during the last profiling frame."""
    
    target_buffer_size: int
    """The streaming device's target buffer length."""
    
    buffer_status_buffered: float
    """The portion of requested data that is buffered, given as a percentage of the target buffer size."""
    
    def __hash__(self):
        """:return: The WwiseObjectInfo hash."""
        return hash(self.device_name)
    
    @property
    def dictionary(self) -> dict[str, str | bool | int | Name]:
        """:return: The instance represented as a dictionary."""
        as_dict = dict()
        if self.device_name is not None:
            as_dict["deviceName"] = self.device_name
        if self.stream_name is not None:
            as_dict["streamName"] = self.stream_name
        if self.file_size is not None:
            as_dict["fileSize"] = self.file_size
        if self.file_position is not None:
            as_dict["filePosition"] = self.file_position
        if self.priority is not None:
            as_dict["priority"] = self.priority
        if self.bandwidth_total is not None:
            as_dict["bandwidthTotal"] = self.bandwidth_total
        if self.bandwidth_low_level is not None:
            as_dict["bandwidthLowLevel"] = self.bandwidth_low_level
        if self.referenced_memory is not None:
            as_dict["referencedMemory"] = self.referenced_memory
        if self.estimated_throughput is not None:
            as_dict["estimatedThroughput"] = self.estimated_throughput
        if self.target_buffer_size is not None:
            as_dict["targetBufferSize"] = self.target_buffer_size
        if self.buffer_status_buffered is not None:
            as_dict["bufferStatusBuffered"] = self.buffer_status_buffered
        return as_dict


@_dataclass
class VoiceContributionParameter:
    """Data class containing the information relating to contribution parameters associated to the voice inspector
    object."""
    
    property_type: str
    """The object property affecting the voice."""
    
    reason: str
    """The reason for the parameter to affect the voice."""
    
    driver: GUID | str
    """Can either be: The driving object GUID or the driving reason when a parameter is not driven by an object."""
    
    driver_value: float | GUID
    """Can either be: The value of the driver affecting the parameter or an object GUID."""
    
    value: float
    """Contribution value."""
    
    def __hash__(self):
        """:return: The VoiceInspectorContributionObjectProperties hash."""
        return hash(str(self.__dict__))
    
    @property
    def dictionary(self) -> dict[str, float | str | GUID]:
        """:return: The instance represented as a dictionary."""
        as_dict = dict()
        as_dict["propertyType"] = self.property_type
        as_dict["reason"] = self.reason
        as_dict["driver"] = self.driver
        as_dict["driverValue"] = self.driver_value
        as_dict["value"] = self.value
        return as_dict


@_dataclass
class VoiceInspectorContribution:
    """Data class containing information from a single voice inspector contribution object."""
    
    name: str
    """The name of the contribution."""
    
    volume: float
    """The volume difference applied."""
    
    lpf: float
    """The LPF difference applied."""
    
    hpf: float
    """The HPF difference applied."""
    
    parameters: list[VoiceContributionParameter] = _field(default_factory=list)
    """Contribution parameters associated to the object."""
    
    children: list[_Self] = _field(default_factory=list)
    """An array of child voice contribution objects associated to the object."""
    
    def __hash__(self):
        """:return: The instance's hash."""
        return hash(str(self.__dict__))
    
    @property
    def dictionary(self) -> dict[str, str | float | dict]:
        """:return: The instance represented as a dictionary."""
        as_dict = dict()
        as_dict["name"] = self.name
        as_dict["volume"] = self.volume
        as_dict["lpf"] = self.lpf
        as_dict["hpf"] = self.hpf
        as_dict["children"] = self.children
        as_dict["parameters"] = self.parameters
        return as_dict


@_dataclass
class VoiceContributionHierarchy:
    """Data class containing relevant to the return schema used to store the information of all parameters affecting
    a voice pipeline ID."""
    
    volume: float
    """The volume difference applied as a contribution."""
    
    lpf: float
    """The LPF difference applied as a contribution."""
    
    hpf: float
    """The HPF difference applied as a contribution."""
    
    objects: list[VoiceInspectorContribution] = _field(default_factory=list)
    """A dictionary of `VoiceInspectorContribution` objects."""
    
    def __hash__(self):
        """:return: The instance's hash."""
        return hash(str(self.__dict__))
    
    @property
    def dictionary(self) -> dict[str, str | float | dict]:
        """:return: The instance represented as a dictionary."""
        as_dict = dict()
        as_dict["volume"] = self.volume
        as_dict["lpf"] = self.lpf
        as_dict["hpf"] = self.hpf
        as_dict["objects"] = self.objects
        return as_dict


@_dataclass
class PlayingVoiceProperties:
    """Data class containing information about the properties of a playing voice."""
    
    pipeline_id: int
    """Pipeline ID of the voice."""
    
    game_object_id: GameObjectID
    """Game Object ID corresponding to the voice."""
    
    object_guid: GUID
    """Object GUID corresponding to the voice."""
    
    other: dict[EVoicePipelineReturnOptions | str, _Any] = _field(default_factory=dict)
    """A dictionary containing other information, if any. Keys are always strings, but can be accessed using the enum
    EVoicePipelineReturnOptions instead."""
    
    def __hash__(self):
        """:return: The WwiseObjectInfo hash."""
        return hash(self.object_guid)


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
    
    position: Vector2
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
class WwiseVersionInfo:
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
class RemoteConsoleInformation:
    """A dataclass representing the information of an available console capable of connecting Wwise authoring to
    a Sound Engine instance."""
    
    name: str
    """Name of the remote console as returned by the executable."""
    
    platform: str
    """Platform of the remote console as returned by the executable."""
    
    custom_platform: str
    """Platform, as defined in the project platforms of the remote console as returned by the executable."""
    
    host: str
    """The IPv4 of the connected host. This can also be a file path if Wwise is connected to a local file
    (profiler session). For using WAAPI on Mac, please refer to Using WAAPI on Mac."""
    
    app_name: str
    """The name of the connected application as returned by the executable. Must be used when connecting to a specific
     Sound Engine instance."""
    
    command_port: int
    """The command port. Can be used when connecting to a specific Sound Engine instance."""
    
    def __hash__(self):
        """:return: The instance's hash."""
        return hash(str(self.__dict__))
    
    @property
    def dictionary(self) -> dict[str, str | int]:
        """:return: The instance represented as a dictionary."""
        as_dict = dict()
        as_dict["name"] = self.name
        as_dict["platform"] = self.platform
        as_dict["customPlatform"] = self.custom_platform
        as_dict["host"] = self.host
        as_dict["appName"] = self.app_name
        as_dict["commandPort"] = self.command_port
        return as_dict


@_dataclass
class ConnectionStatusInfo:
    """A dataclass containing information about the current connection."""
    
    is_connected: bool
    """Indicates if the Wwise Authoring application is connected to a Wwise Sound Engine process."""
    
    status: str
    """The current connection status in text."""
    
    console: RemoteConsoleInformation
    """Remote console associated with the connection."""
    
    def __hash__(self):
        """:return: The instance's hash."""
        return hash(str(self.__dict__))
    
    @property
    def dictionary(self) -> dict[str, str | int]:
        """:return: The instance represented as a dictionary."""
        as_dict = dict()
        as_dict["isConnected"] = self.is_connected
        as_dict["status"] = self.status
        as_dict["console"] = self.console
        return as_dict


@_dataclass
class AudioImportEntry:
    """Dataclass representing a single entry for an audio import operation."""
    
    object_path: ProjectPath
    """The project path of the Wwise object to create, including the name of the object to create. Example:
    "/Actor-Mixer Hierarchy/Default Work Unit/<Random Container>MyContainer/<Sound SFX>MySound" will create a
    `RandomSequenceContainer` (with `RandomOrSequence=1`) called "MyContainer" and a `Sound` called "MySound"."""
    
    root_path: GUID | tuple[EObjectType, Name] | ProjectPath = None
    """Object ID (GUID), name, or path used as root relative object paths. The name of the object qualified by its type
    or Short ID in the form of type:name or Global:shortId. Only object types that have globally-unique names or Short
    Ids are supported. Ex: Event:Play_Sound_01, Global:245489792 string A project path to a Wwise object, including the
    category and the work-unit. For example: /Actor-Mixer Hierarchy/Default Work Unit/New Sound SFX."""
    
    audio_file_path: SystemPath = None
    """Path to media file to import. This path must be accessible from Wwise. For using WAAPI on Mac, please refer to
    Using WAAPI on Mac ."""
    
    audio_file_base64: bytes = None
    """Base64 encoded WAV audio file data to import with its target file path relative to the Originals folder,
    separated by a vertical bar. E.g. 'MySound.wav|UklGRu...'."""
    
    originals_path: OriginalsPath = None
    """Specifies the 'originals' sub-folder in which to place the imported audio file. This folder is relative to the
    'originals' folder in which the file would normally be imported. Example: if importing an SFX, the audio file
    is imported to the folder "/Originals/SFX/{originals_path}"."""
    
    object_type: EObjectType = None
    """Specifies the type of object to create when importing an audio file. This type can also be specified directly in
    the objectPath. Refer to Wwise Objects Reference for the available types."""
    
    object_notes: str = ""
    """The "Notes" field of the created object."""
    
    source_notes: str = ""
    """The "Notes" field of the created audio source object."""
    
    event: ProjectPath = None
    """Defines the path and name of an Event to be created for the imported object.
    Example: "/Events/Default Work Unit/MyEvent"."""
    
    dialogue_event: ProjectPath = None
    """Defines the path and name of a Dialogue Event to be created for the imported object.
    Example: "/Dynamic Dialogue/Default Work Unit/MyEvent"."""
    
    language: GUID | Name = None
    """Imports the language for the audio file import (taken from the project's defined languages, found in the WPROJ
    file LanguageList)."""
    
    properties: ListOrTuple[tuple[str, _NoneType | bool | int | float | str]] = ()
    """A collection of key-value pairs, where keys are property names prefixed by either `@` (a reference to the
    associated object) or `@@` (a reference to the source of override)."""
    
    @property
    def dictionary(self) -> dict[str, str | int | float | bool | Any | None]:
        """:return: The instance represented as a dictionary"""
        return {**({"objectPath": self.object_path} if self.object_path is not None else {}),
                **({"importLocation": self.root_path} if self.root_path is not None else {}),
                **({"audioFile": str(self.audio_file_path)} if self.audio_file_path is not None else {}),
                **({"audioFileBase64": self.audio_file_base64} if self.audio_file_base64 is not None else {}),
                **({"originalsSubFolder": self.originals_path} if self.originals_path is not None else {}),
                **({"objectType": self.object_type.get_type_name()} if self.object_type is not None else {}),
                **({"notes": self.object_notes} if self.object_notes is not None else {}),
                **({"audioSourceNotes": self.source_notes} if self.source_notes is not None else {}),
                **({"event": self.event} if self.event is not None else {}),
                **({"dialogueEvent": self.dialogue_event} if self.dialogue_event is not None else {}),
                **({"importLanguage": self.language} if self.language is not None else {}),
                **dict(self.properties)}


@_dataclass
class ConversionLogItem:
    """Dataclass representing a log item related to conversions."""
    
    severity: ELogSeverity
    """Severity of the logged message."""
    
    message: str
    """Message logged by the system."""


@_dataclass
class WwiseGlobalDirectories:
    """A dataclass containing paths to standard Wwise directories."""
    
    install: SystemPath
    """The root directory of Wwise. This is the installation directory."""
    
    authoring: SystemPath
    """The Wwise Authoring root directory."""
    
    binaries: SystemPath
    """The bin directory, where Wwise.exe is located."""
    
    helper: SystemPath
    """The help directory."""
    
    user: SystemPath
    """The Wwise user data directory root."""


@_dataclass
class WwiseGlobalInfo:
    """Global information about Wwise."""
    
    session_id: GUID
    """Wwise session ID."""
    
    api_version: float
    """Version of the Wwise Authoring API. Range: [1, *]"""
    
    display_name: str
    """Wwise display name."""
    
    branch: str
    """Branch built."""
    
    version: WwiseVersionInfo
    """Wwise version information."""
    
    configuration: EWwiseBuildConfiguration
    """Indicates the build configuration type (e.g. release)."""
    
    platform: EWwiseBuildPlatform
    """Indicates the platform on which Wwise was built (e.g. win32)."""
    
    is_command_line: bool
    """Whether Wwise is running in command line."""
    
    process_id: int
    """The process identifier of Wwise."""
    
    process_path: str
    """The process path of Wwise."""
    
    directories: WwiseGlobalDirectories
    """Collection or directories used by Wwise."""
    
    copyright_info: str
    """Copyright information."""


@_dataclass
class LanguageInfo:
    """Language information."""
    
    guid: GUID
    """Language identifier."""
    
    name: Name
    """Language name."""
    
    short_id: ShortID
    """Language short (32-bit) identifier."""


@_dataclass
class WwiseProjectDirectories:
    """Dataclass with information about the Wwise project directories."""
    
    root: SystemPath
    """The root directory of the Wwise project."""
    
    cache: SystemPath
    """The cache directory of the Wwise project, as specified in the Project Settings. Contains generated media files
    in the WEM format."""
    
    originals: SystemPath
    """The Originals directory of the Wwise project, as specified in the Project Settings. Contains original media files
    in the WAV format."""
    
    sound_bank_output_root: SystemPath
    """The SoundBank output root directory of the project, as specified in the Project Settings. This is where BNK, TXT
    H, XML, and JSON files are placed after a SoundBank generation."""
    
    commands: SystemPath
    """The Commands directory of the project, as specified in the Project Settings. This is where JSON files that
    specify add-on commands are stored."""
    
    properties: SystemPath
    """The Properties directory of the project. This is usually the root Wwise project directory."""


@_dataclass
class WwiseProjectInfo:
    """Information about a Wwise project."""
    
    name: Name
    """The name of the Wwise project as stored in the XML data in the WPROJ file. This is NOT the name of the WPROJ
    file."""
    
    title: str
    """The complete text from the Wwise titlebar."""
    
    path: SystemPath
    """The absolute path of the WPROJ file."""
    
    guid: GUID
    """Project identifier."""
    
    is_dirty: bool
    """True if the Project or any of the Work Units have unsaved changes."""
    
    current_language_guid: GUID
    """The current Language set in the user interface."""
    
    reference_language_guid: GUID
    """The reference Language set in the Language settings."""
    
    current_platform_guid: GUID
    """The current Platform set in the user interface."""
    
    languages: tuple[LanguageInfo, ...]
    """The languages defined in the project."""
    
    platforms: tuple[PlatformInfo, ...]
    """The platforms defined in the project."""
    
    default_conversion: WwiseObjectInfo
    """The default Conversion Settings object."""
