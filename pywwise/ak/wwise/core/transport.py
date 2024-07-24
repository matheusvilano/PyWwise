from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient
from pywwise.enums import ETransportExecuteActions
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

    def get_list(self) -> list():
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_transport_getlist.html \n
        Returns the list of transport objects.
        :return: A list of transport objects.
        """
    
    def get_state(self):
        """
        Gets the state of the given transport object.
        """
    
    def prepare(self):
        """
        Prepare the object and its dependencies for playback. Use this function before calling
        `PostEventSync` or `PostMIDIOnEventSync` from `IAkGlobalPluginContext`.
        """
    
    def use_originals(self):
        """
        Sets the Original/Converted transport toggle globally. This allows playing the original or the
        converted sound files.
        """
    