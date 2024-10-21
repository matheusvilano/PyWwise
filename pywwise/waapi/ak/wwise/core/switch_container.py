# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient

from pywwise.decorators import callback
from pywwise.enums import EReturnOptions
from pywwise.primitives import GUID, ProjectPath
from pywwise.structs import SwitchContainerAssignment, WwiseObjectInfo


class SwitchContainer:
    """ak.wwise.core.switchContainer"""
    
    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
        
        assignment_args = {"return": [EReturnOptions.GUID, EReturnOptions.NAME,
                                      EReturnOptions.TYPE, EReturnOptions.PATH]}
        
        self.assignment_added = _RefEvent(WwiseObjectInfo, WwiseObjectInfo, WwiseObjectInfo)
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_switchcontainer_assignmentadded.html
        \nSent when an assignment is added to a Switch Container.
        \n**Event Data**:
        \n- A WwiseObjectInfo instance representing the Switch Container where a new assignment was added.
        \n- A WwiseObjectInfo instance representing the child object that was assigned.
        \n- A WwiseObjectInfo instance representing the State or Switch to which the child object was assigned.
        """
        
        self._assignment_added = self._client.subscribe("ak.wwise.core.switchContainer.assignmentAdded",
                                                        self._on_assignment_added, assignment_args)
        
        self.assignment_removed = _RefEvent(WwiseObjectInfo, WwiseObjectInfo, WwiseObjectInfo)
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_switchcontainer_assignmentadded.html
        \nSent when an assignment is removed from a Switch Container.
        \n**Event Data**:
        \n- A WwiseObjectInfo instance representing the Switch Container where an assignment was removed.
        \n- A WwiseObjectInfo instance representing the child object that was part of the removed assignment.
        \n- A WwiseObjectInfo instance representing the State or Switch to which the child object was assigned.
        """
        
        self._assignment_added = self._client.subscribe("ak.wwise.core.switchContainer.assignmentRemoved",
                                                        self._on_assignment_removed, assignment_args)
    
    @callback
    def _on_assignment_added(self, event: _RefEvent, **kwargs):
        """
        Callback function for the `assignmentAdded` event.
        :param event: The event to broadcast.
        :param kwargs: The event data.
        """
        event(*self._on_assignment_changed(**kwargs))
    
    @callback
    def _on_assignment_removed(self, event: _RefEvent, **kwargs):
        """
        Callback function for the `assignmentRemoved` event.
        :param event: The event to broadcast.
        :param kwargs: The event data.
        """
        event(*self._on_assignment_changed(**kwargs))
    
    @staticmethod
    def _on_assignment_changed(**kwargs) -> tuple[WwiseObjectInfo, WwiseObjectInfo, WwiseObjectInfo]:
        """
        Utility function for the `assignmentAdded` and `assignmentRemoved` events.
        :param kwargs: The event data.
        :return: The event data, processed.
        """
        container = WwiseObjectInfo.from_dict(kwargs["switchContainer"])
        child = WwiseObjectInfo.from_dict(kwargs["child"])
        sync = WwiseObjectInfo.from_dict(kwargs["stateOrSwitch"])
        return container, child, sync
    
    def add_assignment(self, child: GUID | ProjectPath, state_or_switch: GUID | ProjectPath) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_switchcontainer_addassignment.html \n
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
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_switchcontainer_getassignments.html \n
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
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_switchcontainer_removeassignment.html \n
        Removes an assignment between a Switch Container's child and a State or Switch.
        :param child: The GUID or project path of the object assigned to State or Switch. This object must be a child
                      of a Switch Container.
        :param state_or_switch: The GUID or path of the State or Switch in the assignment. Must be the child of the
                                Switch Group or State Group that is currently set for the Switch Container.
        :return: Whether the call succeeded. Will return `False` if the assignment does not exist.
        """
        args = {"child": child, "stateOrSwitch": state_or_switch}
        return self._client.call("ak.wwise.core.switchContainer.removeAssignment", args) is not None
