from waapi import WaapiClient as _WaapiClient
from pywwise.structs import AuxSendValue
from pywwise.types import Name, ShortID, GUID, ProjectPath, GameObjectID
from pywwise.enums import EAkActionOnEventType, EAkCurveInterpolation


class SoundEngine:
	"""ak.soundengine"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
	
	def execute_action_on_event(self, event: Name | ShortID | GUID, action_type: EAkActionOnEventType,
	                            game_object: GameObjectID, transition_duration: int = 0,
	                            fade_curve: EAkCurveInterpolation = EAkCurveInterpolation.LINEAR) -> dict:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_executeactiononevent.html \n
		Executes an action on all nodes that are referenced in the specified event in a Play action.
		:param event: The name, short ID, or GUID of the event.
		:param action_type: The type of action (e.g. Play).
		:param game_object: The ID of the game object.
		:param transition_duration: The fade duration in milliseconds.
		:param fade_curve: The curve to use for the fade.
		:return: If the call succeeds, this function will return an empty dictionary.
		"""
		args = {"event": event, "actionType": action_type, "gameObject": game_object,
		        "transitionDuration": transition_duration, "fadeCurve": fade_curve}
		return self._client.call("ak.soundengine.executeActionOnEvent", args)
	
	def get_state(self, state_group: Name | ShortID | GUID | ProjectPath) -> tuple[str, str]:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_getstate.html \n
		Gets the current state of a State Group. When using setState just prior to getState, allow a brief delay (no
		more than 10ms) for the information to update in the sound engine.
		:param state_group: The name, short ID, GUID, or project path of the State Group.
		:return: The name and GUID of the active State value. If invalid, the values will be -1 and "".
		"""
		if isinstance(state_group, Name):
			state_group = f"StateGroup:{state_group}"
		elif isinstance(state_group, ShortID):
			state_group = f"Global:{state_group}"
		args = {"stateGroup": state_group}
		results = self._client.call("ak.soundengine.getState", args).get("return")
		return results.get("name"), results.get("id")
	
	def get_switch(self, switch_group: Name | ShortID | GUID | ProjectPath, game_object: GameObjectID) -> tuple[
		str, str]:
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
		results = self._client.call("ak.soundengine.getSwitch", args).get("return")
		return results.get("name"), results.get("id")
	
	def load_bank(self, sound_bank: Name | ShortID | GUID) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_loadbank.html \n
		Load a SoundBank. See `AK::SoundEngine::LoadBank`.
		:param sound_bank: The name or short ID of the bank.
		:return: Whether the operation worked. True does not mean the bank was not loaded prior.
		"""
		args = {"soundBank": sound_bank}
		return self._client.call("ak.soundengine.loadBank", args) is not None
	
	def post_event(self, event: Name | ShortID | GUID, game_object: GameObjectID = GameObjectID.get_transport()) -> int:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_postevent.html \n
		Asynchronously post an Event to the sound engine (by event ID). See `AK::SoundEngine::PostEvent`.
		:param event: The name, short ID, or GUID of the event to post.
		:param game_object: The ID of the game object the event should be posted on.
		:return: The Playing ID of the event. If the call failed, this will be -1.
		"""
		args = {"event": event, "gameObject": game_object}
		results = self._client.call("ak.soundengine.postEvent", args)
		return results.get("return") if results is not None else -1
	
	def post_msg_monitor(self, message: str) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_postmsgmonitor.html \n
		Display a message in the Profiler's Capture Log view.
		:param message: The message to display.
		:return: Whether this operation worked.
		"""
		args = {"message": message}
		return self._client.call("ak.soundengine.postMsgMonitor", args) is not None
	
	def post_trigger(self, trigger: Name | ShortID | GUID, game_object: GameObjectID = None) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_posttrigger.html \n
		Posts the specified Trigger. See `AK::SoundEngine::PostTrigger`.
		:param trigger: The name, short ID, or GUID of the trigger to post.
		:param game_object: The ID of the game object on which the trigger should be posted. If unspecified, the trigger
		will be posted globally.
		:return: Whether this operation worked. True does not mean IDs were all valid.
		"""
		args = {"trigger": trigger}
		if game_object is not None:
			args["gameObject"] = game_object
		return self._client.call("ak.soundengine.postTrigger", args) is not None
	
	def register_game_obj(self, obj_id: GameObjectID, obj_name: Name) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_registergameobj.html \n
		Register a game object. Registering a game object twice does nothing. Unregistering it once unregisters
		it no matter how many times it has been registered. See `AK::SoundEngine::RegisterGameObj`.
		:param obj_id: The ID of the game object to register.
		:param obj_name: The name of the game object to register. This is for monitoring purposes only.
		:return: Whether the call succeeded.
		"""
		args = {"gameObject": obj_id, "name": obj_name}
		return self._client.call("ak.soundengine.registerGameObj", args) is not None
	
	def reset_rtpc_value(self, rtpc: Name | GUID | ShortID, game_object: GameObjectID) -> bool:
		"""
		https://www.audiokinetic.com/en/library/2023.1.4_8496/?source=SDK&id=ak_soundengine_resetrtpcvalue.html \n
		Resets the value of a real-time parameter control to its default value, as specified in the Wwise
		project. See `AK::SoundEngine::ResetRTPCValue`. For a global operation, use GameObjectID.get_global().
		:param rtpc: The name, GUID, or short ID of the RTPC that should be reset to its default value.
		:param game_object: The game object ID (integer).
		:return: Whether the call succeeded. True does not mean a valid RTPC was necessarily reset.
		"""
		args = {"rtpc": rtpc, "gameObject": game_object}
		return self._client.call("ak.soundengine.resetRTPCValue", args) is not None
	
	def seek_on_event(self, event: Name | GUID | ShortID, game_object: GameObjectID, position: int | float,
	                  seek_to_nearest_marker: bool = False, playing_id: int = 0) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_seekonevent.html \n
		Seeks inside all playing objects that are referenced in Play Actions of the specified Event. See
		`AK::SoundEngine::SeekOnEvent`.
		:param event: The name, GUID, or short ID of the event to seek on.
		:param game_object: The ID of the GameObject that owns (encapsulates) the event. Note: this API uses uint32; this
		type has a maximum valid value is `4294967295`, therefore the default Transport and Global IDs are NOT supported.
		:param position: The position where to seek. Note: `int` implies milliseconds; `float` implies percentage.
		:param seek_to_nearest_marker: If true, the final seeking position is made equal to the nearest marker.
		:param playing_id: The playing ID for which the seek if to be applied.
		:return: Whether the call succeeded. True does not mean the Seek action necessarily worked.
		"""
		seek_type = "position" if isinstance(position, int) else "percent"
		args = {"event": event, "gameObject": game_object, seek_type: position,
		        "seekToNearestMarker": seek_to_nearest_marker, "playingId": playing_id}
		return self._client.call("ak.soundengine.seekOnEvent", args) is not None
	
	def set_default_listeners(self, listeners: set[GameObjectID]) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_setdefaultlisteners.html \n
		Sets the default active listeners for all subsequent game objects that are registered. See
		`AK::SoundEngine::SetDefaultListeners`.
		:param listeners: The array of listener game object IDs. Game objects must have been previously registered.
		:return: Whether the call succeeded. True does not mean the informed IDs were all valid.
		"""
		args = {"listeners": list(listeners), "numListeners": len(listeners)}
		return self._client.call("ak.soundengine.setDefaultListeners", args) is not None
	
	def set_game_object_aux_send_values(self, game_obj: GameObjectID,
	                                    aux_send_values: tuple[AuxSendValue, ...]) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_setgameobjectauxsendvalues.html \n
		Sets the Auxiliary Busses to route the specified game object. See `AK::SoundEngine::SetGameObjectAuxSendValues`.
		:param game_obj: The game object ID associated with this operation.
		:param aux_send_values: The aux send values to set.
		:return: Whether the call succeeded. True does not mean the volume necessarily changed (e.g. invalid IDs).
		"""
		args = {"gameObject": game_obj, "auxSendValues": []}
		for aux_send_value in aux_send_values:
			args["auxSendValues"].append({"listener": aux_send_value.listener,
			                              "auxBus": aux_send_value.aux_bus,
			                              "controlValue": aux_send_value.control_value})
		return self._client.call("ak.soundengine.setGameObjectOutputBusVolume", args) is not None
	
	def set_game_object_output_bus_volume(self, emitter: GameObjectID, listener: GameObjectID,
	                                      control_value: float) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_setgameobjectoutputbusvolume.html \n
		Set the output bus volume (direct) to be used for the specified game object. See
		`AK::SoundEngine::SetGameObjectOutputBusVolume`.
		:param emitter: The ID of the emitter game object.
		:param listener: The ID of the listener game object.
		:param control_value: A multiplier where 0 means silence and 1 means no change. Therefore, values between 0 and
		1 attenuate the sound, and values greater than 1 amplify it.
		:return: Whether the call succeeded. True does not mean the volume necessarily changed (e.g. invalid IDs).
		"""
		args = {"emitter": emitter, "listener": listener, "controlValue": control_value}
		return self._client.call("ak.soundengine.setGameObjectAuxSendValues", args) is not None
	
	def set_listeners(self, emitter: GameObjectID, listeners: set[GameObjectID]) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_setlisteners.html \n
		Sets a single game object's active listeners. By default, all new game objects have no listeners active,
		but this behavior can be overridden with `SetDefaultListeners()`. Inactive listeners are not computed. See
		`AK::SoundEngine::SetListeners`.
		:param emitter: The ID of the emitter Game Object to set listeners for.
		:param listeners: The ID of the listeners being set.
		:return: Whether the call succeeded. Note: passing unregistered IDs will cause no change, but the function will
		still return True.
		"""
		args = {"emitter": emitter, "listeners": list(listeners)}
		return self._client.call("ak.soundengine.setListeners", args) is not None
	
	def set_listener_spatialization(self):
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_setlistenerspatialization.html \n
		Sets a listener's spatialization parameters. This lets you define listener-specific volume offsets for
		each audio channel. See `AK::SoundEngine::SetListenerSpatialization`.
		"""
	
	def set_multiple_positions(self):
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_setmultiplepositions.html \n
		Sets multiple positions for a single game object. Setting multiple positions for a single game object is
		a way to simulate multiple emission sources while using the resources of only one voice. This can be used
		to simulate wall openings, area sounds, or multiple objects emitting the same sound in the same area. See
		`AK::SoundEngine::SetMultiplePositions`.
		"""
	
	def set_object_obstruction_and_occlusion(self):
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_setobjectobstructionandocclusion.html \n
		Set a game object's obstruction and occlusion levels. This function is used to affect how an object
		should be heard by a specific listener. See `AK::SoundEngine::SetObjectObstructionAndOcclusion`.
		"""
	
	def set_position(self):
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_setposition.html \n
		Sets the position of a game object. See `AK::SoundEngine::SetPosition`.
		"""
	
	def set_rtpc_value(self):
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_setrtpcvalue.html \n
		Sets the value of a real-time parameter control. See `AK::SoundEngine::SetRTPCValue`.
		"""
	
	def set_scaling_factor(self):
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_setscalingfactor.html \n
		Sets the scaling factor of a game object. You can modify the attenuation computations on this game object
		to simulate sounds with a larger or smaller affected areas. See `AK::SoundEngine::SetScalingFactor`.
		"""
	
	def set_state(self):
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_setstate.html \n
		Sets the State of a State Group. See `AK::SoundEngine::SetState`.
		"""
	
	def set_switch(self):
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_setswitch.html \n
		Sets the State of a Switch Group. See `AK::SoundEngine::SetSwitch`.
		"""
	
	def stop_all(self):
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_stopall.html \n
		Stop playing the current content associated to the specified game object ID. If no game object is
		specified, all sounds are stopped. See `AK::SoundEngine::StopAll`.
		"""
	
	def stop_playing_id(self):
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_stopplayingid.html \n
		Stops the current content, associated to the specified playing ID, from playing. See
		`AK::SoundEngine::StopPlayingID`.
		"""
	
	def unload_bank(self, sound_bank: Name | ShortID | GUID) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_unloadbank.html \n
		Unload a SoundBank. See `AK::SoundEngine::UnloadBank`.
		:param sound_bank: The name, short ID, or GUID of the bank to unload.
		:return: Whether the operation succeeded. True does not mean the bank was previously loaded.
		"""
		args = {"soundBank": sound_bank}
		return self._client.call("ak.soundengine.unloadBank", args) is not None
	
	def unregister_game_obj(self, obj_id: int) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_unregistergameobj.html \n
		Unregisters a game object. Registering a game object twice does nothing. Unregistering it once
		unregisters it no matter how many times it has been registered. Unregistering a game object while it is
		in use is allowed, but the control over the parameters of this game object is lost. For example,
		say a sound associated with this game object is a 3D moving sound. It stops moving when the game object
		is unregistered, and there is no way to regain control over the game object. See
		`AK::SoundEngine::UnregisterGameObj`.
		:param obj_id: The ID of the game object to unregister.
		:return: Whether this operation worked.
		"""
		args = {"gameObject": obj_id}
		return self._client.call("ak.soundengine.unregisterGameObj", args) is not None
