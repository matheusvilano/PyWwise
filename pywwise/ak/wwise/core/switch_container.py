from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient
from pywwise.structs import SwitchContainerAssignment
from pywwise.types import GUID, ProjectPath


class SwitchContainer:
	"""ak.wwise.core.switchContainer"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
		
		# TODO: implement topics
		self.assignment_added: _RefEvent
		self.assignment_removed: _RefEvent
	
	def add_assignment(self, child: GUID | ProjectPath, state_or_switch: GUID | ProjectPath) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_switchcontainer_addassignment.html \n
		Assigns a Switch Container's child to a State or Switch. This is the equivalent of doing a drag-and-drop of
		the child to a state or switch in the Assigned Objects view. The child is always added at the end for each
		state.
		:param child: The GUID or project path of the object to assign to a State or Switch. This object must be a
					  child of a Switch Container.
		:param state_or_switch: The GUID or path of the State or Switch with which to assign. Must be the child of the
								Switch Group or State Group that is currently set for the Switch Container.
		:return: Whether the call succeeded. Will return `False` if the assignment already exists.
		"""
		args = {"child": child, "stateOrSwitch": state_or_switch}
		return self._client.call("ak.wwise.core.switchContainer.addAssignment", args) is not None
	
	def get_assignments(self, switch_container: GUID | ProjectPath) -> tuple[SwitchContainerAssignment, ...]:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_switchcontainer_getassignments.html \n
		Returns the list of assignments between a Switch Container's children and states.
		:param switch_container: The GUID or project path of the Switch Container from which to get assignments.
		:return: A tuple of `SwitchContainerAssignment` instances. May be empty (if there are no valid assignments or
				 if the call failed).
		"""
		results = self._client.call("ak.wwise.core.switchContainer.getAssignments", {"id": switch_container})
		if results is None:
			return ()
		results = results.get("return", ())
		return tuple(SwitchContainerAssignment(result["child"], result["stateOrSwitch"]) for result in results)
	
	def remove_assignment(self, child: GUID | ProjectPath, state_or_switch: GUID | ProjectPath) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_switchcontainer_removeassignment.html \n
		Removes an assignment between a Switch Container's child and a State or Switch.
		:param child: The GUID or project path of the object assigned to State or Switch. This object must be a child
					  of a Switch Container.
		:param state_or_switch: The GUID or path of the State or Switch in the assignment. Must be the child of the
								Switch Group or State Group that is currently set for the Switch Container.
		:return: Whether the call succeeded. Will return `False` if the assignment does not exist.
		"""
		args = {"child": child, "stateOrSwitch": state_or_switch}
		return self._client.call("ak.wwise.core.switchContainer.removeAssignment", args) is not None
