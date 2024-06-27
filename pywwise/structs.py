from dataclasses import dataclass as _dataclass, field as _field
from pathlib import Path as _Path
from pywwise.types import Name as _Name, GUID as _GUID, ShortID as _ShortID, GameObjectID as _GameObjectID
from pywwise.enums import EBasePlatform as _EBasePlatform, EStartMode as _EStartMode


@_dataclass
class Vector3:
	"""Data-only 3-dimensional vector."""
	
	x: float
	"""X axis."""
	
	y: float
	"""Y axis."""
	
	z: float
	"""Z axis."""
	
	@staticmethod
	def get_zero():
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
		""":return: A captureRect instance with x, y, width, and height all set to 0."""
		return Rect(0, 0, 0, 0)


@_dataclass
class AuxSendValue:
	"""Data-only class representing an aux send value."""
	
	listener: _GameObjectID
	"""The ID of the associated listener."""
	
	aux_bus: _GUID | _Name | _ShortID
	"""The GUID, name, or short ID of the Aux Bus."""
	
	control_value: float
	"""The intended value."""


@_dataclass
class PlatformInfo:
	"""Structure for storing basic platform info. Useful when creating a new project or adding a new platform to a project."""
	
	name: str
	"""The name of this platform."""
	
	base_platform: _EBasePlatform
	"""The base platform."""

	guid: _GUID
	"""The GUID of this platform."""

	def __hash__(self):
		""":return: The PlatformInfo hash."""
		return hash(self.name)


@_dataclass
class ExternalSourceInfo:
	"""Data-only class storing information about an external source."""
	
	input: _Path
	"""The path where the external source's WAV file is located."""
	
	platform: _Name | _GUID
	"""The name or GUID of the platform this external source is associated with."""
	
	output: _Path
	"""The output path of the external source's WEM (after conversions)."""


@_dataclass
class CommandContextMenuInfo:
	"""Data-only class storing information about a command's context menu, which is part of an add-on command's
	arguments."""

	base_path: str
	"""Defines a forward-separated path for the parent sub menus. If empty, the menu is inserted at the first level."""

	visible_for: str
	"""Defines a comma-separated list of the object types for which the item is visible. Refer to Wwise Objects 
	Reference for the list of types supported. If empty, any type is allowed."""

	enabled_for: str
	"""Defines a comma-separated list of the object types for which the item is enabled. Refer to Wwise Objects 
	Reference for the list of types supported. If empty, any type is allowed."""


@_dataclass
class CommandMainMenuInfo:
	"""Data-only class storing information about a command's main menu, which is part of an add-on command's argument"""

	main_menu_base_path: str
	"""Defines a forward-separated path for the parent sub menus. It must at least define one level, which is associated 
	to the top menu."""


@_dataclass
class CommandInfo:
	"""Data-only class storing information about an add-on command."""

	id: str
	"""Defines a human readable unique ID for the command. To reduce risk of ID conflicts, please use a concatenation of 
	the author name, the product name and the command name."""

	display_name: str
	"""Defines the name displayed in the user interface."""

	program: str
	"""Defines the program or script to run when the command is executed. Arguments are specified in 'args'. Note that 
	common directories variables can be used, such as ${CurrentCommandDirectory}."""

	lua_script: str
	"""Defines a lua script file path to run inside Wwise process when the command is executed. Arguments are specified 
	in 'args'. Note that common directories variables can be used, such as ${CurrentCommandDirectory}."""

	lua_paths: list[str]
	"""Defines an array of paths to be used to load additional lua scripts. Here is an example of a lua path 
	C:/path_to_folder/?.lua. Note that common directories variables can be used, such as ${CurrentCommandDirectory}."""

	lua_selected_return: list[str]
	"""Specifies an array of return expressions for the selected objects in Wwise. This will be available to the script 
	in a lua table array in wa_args.selected. Several values provided for the option."""

	start_mode: _EStartMode
	"""Specifies how to expand variables in the arguments field in case of multiple selection in the Wwise user 
	interface."""

	args: str
	"""Defines the arguments. Refer to the documentation for the list of supported built-in variables. Note that in the 
	event of a multiple selection, the variables are expanded based on the startMode field. Note that common directories 
	variables can be used, such as ${CurrentCommandDirectory}."""

	cwd: str
	"""Defines the current working directory to execute the program. Note that common directories variables can be used, 
	such as ${CurrentCommandDirectory}."""

	default_shortcut: str
	"""Defines the shortcut to use by default for this command. If the shortcut conflicts, it won't be used. This 
	shortcut can be changed in the Keyboard Shortcut Manager."""

	redirect_outputs: bool
	"""Defines if the standard output streams of the program (stdout + stderr) should be redirected and logged to Wwise 
	on termination. The value is of boolean type and false by default."""

	context_menu: CommandContextMenuInfo
	"""If present, specify how the command is added to Wwise context menus. If empty, no context menu is added."""

	main_menu: CommandMainMenuInfo
	"""If present, specify how the command is added to Wwise main menus. If empty, no main menu entry is added."""

@_dataclass
class SoundBankInfo:

	name: str
	"""The name of the SoundBank to generate, a temporary SoundBank will be created if the SoundBank doesn't exists."""

	events: list[str] = None
	"""List of events to include in this SoundBank. Not required if the bank already exists."""

	aux_busses: list[str] = None
	"""List of AuxBus to include in this SoundBank."""

	inclusions: list[str] = None
	"""List of inclusion type to use for this SoundBank. Not required if the bank already exists."""

	rebuild: bool = False
	"""Force rebuild of this particular SoundBank. Default value: false."""

	def __hash__(self) -> int:
		""":return: The SoundBankInfo hash."""
		return hash(self.name)
	
	@property
	def dictionary(self) -> dict[str, bool | str | list[str]]:
		dict_repr = {"name": self.name, "rebuild": self.rebuild}
		if self.events is not None:
			dict_repr["events"] = self.events
		if self.aux_busses is not None:
			dict_repr["auxBusses"] = self.aux_busses
		if self.inclusions is not None:
			dict_repr["inclusions"] = self.inclusions
		return dict_repr
