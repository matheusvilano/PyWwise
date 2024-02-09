from waapi import WaapiClient as _WaapiClient
from pywwise.types import Name, ShortID, GUID, ProjectPath
from pywwise.enums import EAkActionOnEventType, EAkCurveInterpolation


class SoundEngine:
    """ak.soundengine"""

    def __init__(self, client: _WaapiClient):
        """
        Constructor.
        :param client: The WAAPI client to use.
        """
        self._client = client

    def execute_action_on_event(self, event: Name | ShortID | GUID, action_type: EAkActionOnEventType, game_object: int,
                                transition_duration: int, fade_curve: EAkCurveInterpolation) -> None:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_executeactiononevent.html \n
        Executes an action on all nodes that are referenced in the specified event in a Play action.
        :param event: The name, short ID, or GUID of the event.
        :param action_type: The type of action (e.g. Play).
        :param game_object: The ID of the game object.
        :param transition_duration: The fade duration in milliseconds.
        :param fade_curve: The curve to use for the fade.
        """
        args = {"event": event, "actionType": action_type, "gameObject": game_object,
                "transitionDuration": transition_duration, "fadeCurve": fade_curve}
        self._client.call("ak.soundengine.executeActionOnEvent", args)

    def get_state(self, state_group: Name | ShortID | GUID | ProjectPath):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_getstate.html \n
        Gets the current state of a State Group. When using setState just prior to getState, allow a brief delay (no
        more than 10ms) for the information to update in the sound engine.
        :param state_group: The name, short ID, or project path of the State Group.
        :return: The name and GUID of the active State value. If invalid, the values will be -1 and "".
        """
        if isinstance(state_group, Name):
            state_group = f"StateGroup:{state_group}"
        elif isinstance(state_group, ShortID):
            state_group = f"Global:{state_group}"
        args = {"stateGroup": state_group}
        return self._client.call("ak.soundengine.getState", args).get("return")

    def get_switch(self, switch_group: Name | ShortID | GUID | ProjectPath, game_object: int):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_getswitch.html \n
        Gets the current state of a Switch Group for a given Game Object.
        :param switch_group: The name, short ID, or GUID of the Switch Group.
        :param game_object: The ID of the game object. Switches are always encapsulated by game objects.
        :return: The name and GUID of the active Switch value.
        """
        if isinstance(switch_group, Name):
            switch_group = f"SwitchGroup:{switch_group}"
        elif isinstance(switch_group, ShortID):
            switch_group = f"Global:{switch_group}"
        args = {"switchGroup": switch_group, "gameObject": game_object}
        return self._client.call("ak.soundengine.getSwitch", args).get("return")

    def load_bank(self, sound_bank: str | int):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_loadbank.html \n
        Load a SoundBank. See `AK::SoundEngine::LoadBank`.
        :param sound_bank: The name or short ID of the bank.
        """
        args = {"soundBank": sound_bank}

    def post_event(self):
        """
        Asynchronously post an Event to the sound engine (by event ID). See `AK::SoundEngine::PostEvent`.
        """

    def post_msg_monitor(self):
        """
        Display a message in the Profiler's Capture Log view.
        """

    def post_trigger(self):
        """
        Posts the specified Trigger. See `AK::SoundEngine::PostTrigger`.
        """

    def register_game_obj(self):
        """
        Register a game object. Registering a game object twice does nothing. Unregistering it once unregisters
        it no matter how many times it has been registered. See `AK::SoundEngine::RegisterGameObj`.
        """

    def reset_rtpc_value(self):
        """
        Resets the value of a real-time parameter control to its default value, as specified in the Wwise
        project. See `AK::SoundEngine::ResetRTPCValue`.
        """

    def seek_on_event(self):
        """
        Seeks inside all playing objects that are referenced in Play Actions of the specified Event. See
        `AK::SoundEngine::SeekOnEvent`.
        """

    def set_default_listeners(self):
        """
        Sets the default active listeners for all subsequent game objects that are registered. See
        `AK::SoundEngine::SetDefaultListeners`.
        """

    def set_game_object_aux_send_values(self):
        """
        Sets the Auxiliary Busses to route the specified game object. See
        `AK::SoundEngine::SetGameObjectAuxSendValues`.
        """

    def set_game_object_output_bus_volume(self):
        """
        Sets the Auxiliary Buses to route the specified game object. See
        `AK::SoundEngine::SetGameObjectAuxSendValues`.
        """

    def set_listeners(self):
        """
        Sets a single game object's active listeners. By default, all new game objects have no listeners active,
        but this behavior can be overridden with `SetDefaultListeners()`. Inactive listeners are not computed. See
        `AK::SoundEngine::SetListeners`.
        """

    def set_listener_spatialization(self):
        """
        Sets a listener's spatialization parameters. This lets you define listener-specific volume offsets for
        each audio channel. See `AK::SoundEngine::SetListenerSpatialization`.
        """

    def set_multiple_positions(self):
        """
        Sets multiple positions for a single game object. Setting multiple positions for a single game object is
        a way to simulate multiple emission sources while using the resources of only one voice. This can be used
        to simulate wall openings, area sounds, or multiple objects emitting the same sound in the same area. See
        `AK::SoundEngine::SetMultiplePositions`.
        """

    def set_object_obstruction_and_occlusion(self):
        """
        Set a game object's obstruction and occlusion levels. This function is used to affect how an object
        should be heard by a specific listener. See `AK::SoundEngine::SetObjectObstructionAndOcclusion`.
        """

    def set_position(self):
        """
        Sets the position of a game object. See `AK::SoundEngine::SetPosition`.
        """

    def set_rtpc_value(self):
        """
        Sets the value of a real-time parameter control. See `AK::SoundEngine::SetRTPCValue`.
        """

    def set_scaling_factor(self):
        """
        Sets the scaling factor of a game object. You can modify the attenuation computations on this game object
        to simulate sounds with a larger or smaller affected areas. See `AK::SoundEngine::SetScalingFactor`.
        """

    def set_state(self):
        """
        Sets the State of a State Group. See `AK::SoundEngine::SetState`.
        """

    def set_switch(self):
        """
        Sets the State of a Switch Group. See `AK::SoundEngine::SetSwitch`.
        """

    def stop_all(self):
        """
        Stop playing the current content associated to the specified game object ID. If no game object is
        specified, all sounds are stopped. See `AK::SoundEngine::StopAll`.
        """

    def stop_playing_id(self):
        """
        Stops the current content, associated to the specified playing ID, from playing. See
        `AK::SoundEngine::StopPlayingID`.
        """

    def unload_bank(self):
        """
        Unload a SoundBank. See `AK::SoundEngine::UnloadBank`.
        """

    def unregister_game_obj(self):
        """
        Unregisters a game object. Registering a game object twice does nothing. Unregistering it once
        unregisters it no matter how many times it has been registered. Unregistering a game object while it is
        in use is allowed, but the control over the parameters of this game object is lost. For example,
        say a sound associated with this game object is a 3D moving sound. It stops moving when the game object
        is unregistered, and there is no way to regain control over the game object. See
        `AK::SoundEngine::UnregisterGameObj`.
        """
