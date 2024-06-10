import dataclasses
from pywwise.types import Name as _Name, GUID as _GUID, ShortID as _ShortID, GameObjectID as _GameObjectID


@dataclasses.dataclass
class AuxSendValue:

	listener: _GameObjectID
	aux_bus: _GUID | _Name | _ShortID
	control_value: float
