# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from simplevent import RefEvent as _RefEvent
from waapi import EventHandler as _EventHandler, WaapiClient as _WaapiClient

from pywwise.decorators import callback
from pywwise.enums import EObjectType, ETransportExecuteActions, ETransportState
from pywwise.primitives import GameObjectID, GUID, Name, ProjectPath
from pywwise.statics import EnumStatics
from pywwise.structs import TransportObjectInfo


class Transport:
    """ak.wwise.core.transport"""
    
    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
        
        self.state_changed = _RefEvent(int, ETransportState, GUID, GameObjectID)
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_transport_statechanged.html
        \nSent when the transport's state has changed. A transport needs to be created first, using `create`.
        \n**Event Data**:
        \n- The ID (unsigned integer 32-bit) of the watched transport.
        \n- A string containing the old name.
        \n- The GUID of the object controlled by the transport object.
        \n- The GameObjectID used by the transport object. An invalid (`-1`) ID just means no game object was used.
        """
        
        self._state_changed = dict[int, _EventHandler]()  # keys are transport IDs; subscriptions are dynamic
    
    @callback
    def _on_state_changed(self, event: _RefEvent, **kwargs):
        """
        Callback function for the `stateChanged` event.
        :param event: The event to broadcast.
        :param kwargs: The event data.
        """
        kwargs["state"] = EnumStatics.from_value(ETransportState, kwargs["state"])
        kwargs["gameObject"] = GameObjectID(kwargs.get("gameObject", -1))  # -1 means the ID is invalid
        event(kwargs["transport"], kwargs["state"], kwargs["object"], kwargs["gameObject"])
    
    def create(self, wwise_obj: GUID | tuple[EObjectType, Name] | ProjectPath,
               game_obj: GameObjectID = None) -> int:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_transport_create.html \n
        Creates a transport object for the given Wwise object. The return transport object can be used to
        play, stop, pause and resume the Wwise object via the other transport functions.
        :param wwise_obj: The ID (GUID), typed name, or project path of the object to control via the transport object.
        :param game_obj: The game object to use for playback.
        :return: Transport object ID to be used with all other ak.wwise.core.transport functions. Returns -1 if function
                 call failed.
        """
        is_typed_name = isinstance(wwise_obj, tuple)
        args = {"object": wwise_obj if not is_typed_name else f"{wwise_obj[0].get_type_name()}:{wwise_obj[1]}"}
        if game_obj is not None:
            args["gameObject"] = game_obj
        
        results = self._client.call("ak.wwise.core.transport.create", args)
        if results is None or results.get("transport") is None:
            return -1
        
        transport_id = results["transport"]
        if self._state_changed.get(transport_id) is None:  # subscription doesn't exist, so we need to set one up
            self._state_changed[transport_id] = self._client.subscribe("ak.wwise.core.transport.stateChanged",
                                                                       {"transport": transport_id})
        
        return -1 if results is None else results.get("transport", -1)
    
    def destroy(self, transport_id: int) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_transport_destroy.html \n
        Destroys the given transport object.
        :param transport_id: The transport object ID to be used with all other ak.wwise.core.transport functions. Make
                             sure you create a transport object before calling this function.
        :return: True if the transport object was destroyed, False otherwise.
        """
        args = {"transport": transport_id}
        
        results = self._client.call("ak.wwise.core.transport.destroy", args)
        if results is None:
            return False
        
        event_handler = self._state_changed.get(transport_id)
        if event_handler is not None:  # unsubscription should only happen if a subscription exists
            self._client.unsubscribe(event_handler)
        
        return True
    
    def execute_action(self, transport_action: ETransportExecuteActions, transport_id: int = None) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_transport_executeaction.html \n
        Executes an action on the given transport object, or all transport objects if none is specified.
        :param transport_action: The action to execute. Use ETransportExecuteActions to see the available actions.
        :param transport_id: The transport object ID to be used with all other ak.wwise.core.transport functions. Make
                             sure you create a transport object before calling this function.
        :return: True if the action was executed, False otherwise.
        """
        args = {"action": transport_action, **({"transport": transport_id} if transport_id is not None else dict())}
        return self._client.call("ak.wwise.core.transport.execute", args) is not None
    
    def get_list(self) -> tuple[TransportObjectInfo, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_transport_getlist.html \n
        Returns the list of transport objects.
        :return: A list of transport objects.
        """
        results = self._client.call("ak.wwise.core.transport.getList", {})
        
        results = results.get("list") if results is not None else None
        
        if results is None:
            return ()
        
        transport_objects = list[TransportObjectInfo]()
        
        for result in results:
            obj = GUID(result["object"])
            game_object = int(result["gameObject"])
            transport = int(result["transport"])
            transport_objects.append(TransportObjectInfo(obj, game_object, transport))
        
        return tuple(transport_objects)
    
    def get_state(self, transport_id: int) -> ETransportState:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_transport_getstate.html \n
        Gets the state of the given transport object.
        :param transport_id: The transport object ID to be used with all other ak.wwise.core.transport functions. Make
                             sure you create a transport object before calling this function.
        :return: An enum value that represents the state of the transport object. Return value can either be: Playing,
                 Stopped, Paused, or None. In case its none, the method call failed.
        """
        args = {"transport": transport_id}
        
        result = self._client.call("ak.wwise.core.transport.getState", args)
        
        if result is None:
            return ETransportState.NONE
        
        # from_value will [attempt to] convert any value to the specified Enum subclass.
        return EnumStatics.from_value(ETransportState, result.get("state", "None"))
    
    def prepare(self, obj: GUID | tuple[EObjectType, Name] | ProjectPath) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_transport_prepare.html \n
        Prepare the object and its dependencies for playback. Use this function before calling
        `PostEventSync` or `PostMIDIOnEventSync` from `IAkGlobalPluginContext`.
        :param obj: The GUID, typed name, or project path of the object to prepare. Only object types that have
                    globally-unique names are supported (e.g. EObjectType.EVENT).
        :return: True if the call was successful, False otherwise.
        """
        is_name = isinstance(obj, tuple)
        args = {"object": obj if not is_name else f"{obj[0].get_type_name()}:{obj[1]}"}
        return self._client.call("ak.wwise.core.transport.prepare", args) is not None
    
    def use_originals(self, flag: bool = False) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_transport_useoriginals.html \n
        Sets the Original/Converted transport toggle globally. This allows playing the original or the
        converted sound files.
        :param flag: True to enable original files, False to use converted files. If no value is provided, system will
                     default to using converted files.
        :return: True if the call was successful, False otherwise.
        """
        args = {"enable": flag}
        return self._client.call("ak.wwise.core.transport.useOriginals", args) is not None
