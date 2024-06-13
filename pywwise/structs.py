import dataclasses
from pywwise.types import Name as _Name, GUID as _GUID, ShortID as _ShortID, GameObjectID as _GameObjectID


@dataclasses.dataclass
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


@dataclasses.dataclass
class AuxSendValue:
	"""Data-only aux send value."""
	
	listener: _GameObjectID
	"""The ID of the associated listener."""
	
	aux_bus: _GUID | _Name | _ShortID
	"""The GUID, name, or short ID of the Aux Bus."""
	
	control_value: float
	"""The intended value."""
