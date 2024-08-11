from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient
from pywwise.enums import EObjectType, ETransportExecuteActions, ETransportState
from pywwise.statics import EnumStatics
from pywwise.structs import TransportObjectInfo
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
    
    def create(self, wwise_object: tuple[EObjectType, Name] | GUID | ProjectPath,
               game_object: GameObjectID = None) -> int:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_transport_create.html \n
        Creates a transport object for the given Wwise object. The return transport object can be used to
        play, stop, pause and resume the Wwise object via the other transport functions.
        :arg wwise_object: The ID (GUID), name, or project path of the object to control via the transport object.
        :arg game_object: The game object to use for playback.
        :return: Transport object ID to be used with all other ak.wwise.core.transport functions. Returns -1 if function
                 call failed.
        """
        args = {"object": wwise_object if not
                isinstance(wwise_object, tuple) else f"{wwise_object[0].get_type_name()}_{wwise_object[1]}"}
        
        if game_object is not None:
            args["gameObject"] = game_object
        
        result = self._client.call("ak.wwise.core.transport.create", args)
        
        return -1 if result is None else result.get("transport", -1)
    
    def destroy(self, transport_id: int) -> bool:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_transport_destroy.html \n
        Destroys the given transport object.
        :param transport_id: The transport object ID to be used with all other ak.wwise.core.transport functions. Make
                             sure you create a transport object before calling this function.
        :return: True if the transport object was destroyed, False otherwise.
        """
        args = {"transport": transport_id}
        
        return self._client.call("ak.wwise.core.transport.destroy") is not None
    
    def execute_action(self, transport_action: ETransportExecuteActions, transport_id: int = None) -> bool:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_transport_executeaction.html \n
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
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_transport_getlist.html \n
        Returns the list of transport objects.
        :return: A list of transport objects.
        """
        results = self._client.call("ak.wwise.core.transport.getList", {})
        
        results = results.get("list") if results is not None else None
        
        if results is None:
            return ()
        
        transport_objects = list[TransportObjectInfo]()
        
        for result in results:
            object = GUID(result["object"])
            game_object = int(result["gameObject"])
            transport = int(result["transport"])
            transport_objects.append(TransportObjectInfo(object, game_object, transport))
        
        return tuple(transport_objects)
    
    def get_state(self, transport_id: int) -> ETransportState:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_transport_getstate.html \n
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
        
        message = result.get("state")
        
        return EnumStatics.from_value(ETransportState, result.get("state", "None"))
        # from_value will [attempt to] convert any value to the specified Enum subclass.
    
    def prepare(self, object: GUID | ProjectPath | tuple[EObjectType, Name]) -> bool:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_transport_prepare.html \n
        Prepare the object and its dependencies for playback. Use this function before calling
        `PostEventSync` or `PostMIDIOnEventSync` from `IAkGlobalPluginContext`.
        :param object: The name of the object qualified by its type in the form of type:name.
                       Only object types that have globally-unique names or Short Ids are supported.
                       Ex: Event:Play_Sound_01, Global:245489792.
        :return: True if the call was successful, False otherwise.
        """
        args = {"object": object if not
                isinstance(object, tuple) else f"{object[0]}_{object[1]}"}
        
        return self._client.call("ak.wwise.core.transport.prepare", args) is not None
    
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
        return self._client.call("ak.wwise.core.transport.useOriginals", args) is not None
    