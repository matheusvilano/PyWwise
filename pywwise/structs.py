from dataclasses import dataclass as _dataclass
from pathlib import Path as _Path
from pywwise.types import Name as _Name, GUID as _GUID, ShortID as _ShortID, GameObjectID as _GameObjectID
from pywwise.enums import EBasePlatform as _EBasePlatform


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
class AuxSendValue:
	"""Data-only class representing a aux send value."""
	
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
