from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient
from pywwise.enums import ETransportExecuteActions
from pywwise.structs import WwiseTransportObjectInfo
from pywwise.types import GameObjectID, GUID, Name, ProjectPath


class Transport:
    """ak.wwise.core.transport"""
    
    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client
        
        # TODO: implement topics
        self.state_changed: _RefEvent
    
    def create(self, wwise_object: Name | GUID | ProjectPath, game_object: GameObjectID = None) -> int:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_transport_create.html \n
        Creates a transport object for the given Wwise object. The return transport object can be used to
        play, stop, pause and resume the Wwise object via the other transport functions.
        :arg wwise_object: The ID (GUID), name, or project path of the object to control via the transport object.
        :arg game_object: The game object to use for playback.
        :return: Transport object ID to be used with all other ak.wwise.core.transport functions. Returns -1 if function
        call failed.
        """
        
        if wwise_object is None:
            return -1
        
        args = {"object": wwise_object, **({"game_object": game_object} if game_object is not None else {})}
        
        result = self._client.call("ak.wwise.core.transport.create", args)
        
        if result is None:
            return -1
        
        return result.get("transport")
    
    def destroy(self, transport_id: int) -> bool:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_transport_destroy.html \n
        Destroys the given transport object.
        :param transport_id: The transport object ID to be used with all other ak.wwise.core.transport functions. Make
        sure you create a transport object before calling this function.
        :return: True if the transport object was destroyed, False otherwise.
        """
        
        if transport_id is None:
            return False
        
        args = {"transport": transport_id}
        
        return self._client.call("ak.wwise.core.transport.destroy") is not None
    
    def execute_action(self, transport_action: ETransportExecuteActions, transport_id: int = None) -> bool:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_transport_executeaction.html \n
        Executes an action on the given transport object, or all transport objects if none is specified.
        :arg transport_action: The action to execute. Use ETransportExecuteActions to see the available actions.
        :arg transport_id: The transport object ID to be used with all other ak.wwise.core.transport functions. Make
        sure you create a transport object before calling this function.
        :return: True if the action was executed, False otherwise.
        """
        
        if transport_action is None:
            return False
        
        args = {"action": transport_action, **({"transport": transport_id} if transport_id is not None else {})}
        
        return self._client.call("ak.wwise.core.transport.execute", args) is not None

    def get_list(self) -> tuple[WwiseTransportObjectInfo, ...]:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_transport_getlist.html \n
        Returns the list of transport objects.
        :return: A list of transport objects.
        """
        args = {}
        
        results = self._client.call("ak.wwise.core.transport.getList", args)
        results = results.get("list") if results is not None else None
        if results is None:
            return ()
        
        transport_objects = list[WwiseTransportObjectInfo]
        
        for result in results:
            object = GUID(result["object"])
            game_object = int(result["gameObject"])
            transport = int(result["transport"])
            transport_objects.append(WwiseTransportObjectInfo(object, game_object, transport))
        
        return tuple(transport_objects)
    
    def get_state(self, transport_id: int) -> tuple[bool, str]:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_transport_getstate.html \n
        Gets the state of the given transport object.
        :param transport_id: The transport object ID to be used with all other ak.wwise.core.transport functions. Make
        sure you create a transport object before calling this function.
        :return: A tuple made up of a bool and a string message. If the call fails, the bool will be false. If the call
        succeeds, the bool will be true and the string will represent the current state of the transport object. The
        return message can either be: Playing, Stopped, Paused
        """
        
        if transport_id is None:
            return False, "No transport object was given."
        
        args = {"transport": transport_id}
        
        result = self._client.call("ak.wwise.core.transport.getState", args)
        
        if result is None:
            return False, "Function called failed."
        
        message = result.get("state")
        
        return True, message
    
    def prepare(self, object: GUID | ProjectPath | Name) -> bool:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_transport_prepare.html \n
        Prepare the object and its dependencies for playback. Use this function before calling
        `PostEventSync` or `PostMIDIOnEventSync` from `IAkGlobalPluginContext`.
        :param object: The name of the object qualified by its type or Short ID in the form of type:name or
        Global:shortId. Only object types that have globally-unique names or Short Ids are supported.
        Ex: Event:Play_Sound_01, Global:245489792.
        :return: True if the call was successful, False otherwise.
        """
        
        if object is None:
            return False
        
        args = {"object": object}
        
        result = self._client.call("ak.wwise.core.transport.prepare", args)
        
        if result is not None:
            return True
        else:
            return False
    
    def use_originals(self, enable_original_files: bool = False) -> bool:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_transport_useoriginals.html \n
        Sets the Original/Converted transport toggle globally. This allows playing the original or the
        converted sound files.
        :param enable_original_files: True to enable original files, False to use converted files. If no value is
        provided, system will default to using converted files.
        :return: True if the call was successful, False otherwise.
        """
    
        args = {"enable": enable_original_files}
        
        result = self._client.call("ak.wwise.core.transport.useOriginals", args)
        
        if result is not None:
            return True
        else:
            return False
        