from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient
from pywwise.ak.wwise.core.capture_log import CaptureLog as _CaptureLog
from pywwise.decorators import callback
from pywwise.enums import EReturnOptions
from pywwise.structs import WwiseObjectInfo
from pywwise.types import GameObjectID, Name


class Profiler:
	"""ak.wwise.core.profiler"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
		self.capture_log = _CaptureLog(client)
		
		self.game_object_registered = _RefEvent(int, GameObjectID, Name)
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_gameobjectregistered.html
		\nSent when a game object has been registered.
		\n**Event Data**:
		\n- Time of registration. Elapsed time in milliseconds since the initialization of the soundengine.
		\n- The game object ID for the entry.
		\n- The game object name for the entry.
		"""
		
		self._game_object_registered = self._client.subscribe("ak.wwise.core.profiler.gameObjectRegistered",
		                                                      self._on_game_object_registered)
		
		self.game_object_reset = _RefEvent()
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_gameobjectreset.html
		\nSent when the game objects have been reset, such as closing a connection to a game while profiling.
		"""
		
		self._game_object_reset = self._client.subscribe("ak.wwise.core.profiler.gameObjectReset",
		                                                 self._on_game_object_reset)
		
		self.game_object_unregistered = _RefEvent(int, GameObjectID, Name)
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_gameobjectunregistered.html
		\nSent when a game object has been unregistered.
		\n**Event Data**:
		\n- Time of un-registration. Elapsed time in milliseconds since the initialization of the soundengine.
		\n- The game object ID for the entry.
		\n- The game object name for the entry.
		"""
		
		self._game_object_unregistered = self._client.subscribe("ak.wwise.core.profiler.gameObjectUnregistered",
		                                                        self._on_game_object_unregistered)
		
		# The return options below are needed so we can retrieve information about Switch and States, plus their Groups.
		change_args = {"return": [EReturnOptions.GUID, EReturnOptions.NAME, EReturnOptions.TYPE, EReturnOptions.PATH]}
		
		self.state_changed = _RefEvent(WwiseObjectInfo, WwiseObjectInfo)
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_statechanged.html
		\nSent when a state group state has been changed. Does not require the profiler capture log to be started.
		\n**Event Data**:
		\n-A WwiseObjectInfo instance containing information about the State Group where the change happened.
		\n-A WwiseObjectInfo instance containing information about the new active State.
		"""
		
		self._state_changed = self._client.call("ak.wwise.core.profiler.stateChanged",
		                                        self._on_state_changed, change_args)
		
		self.switch_changed = _RefEvent(WwiseObjectInfo, WwiseObjectInfo, GameObjectID)
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_switchchanged.html
		\nSent when a switch group state has been changed. Does not require the profiler capture log to be started.
		\n**Event Data**:
		\n-A WwiseObjectInfo instance containing information about the Switch Group where the change happened.
		\n-A WwiseObjectInfo instance containing information about the new active Switch.
		\n-The ID of the game object on which the change happened.
		"""
		
		self._switch_changed = self._client.call("ak.wwise.core.profiler.switchChanged",
		                                         self._on_switch_changed, change_args)
	
	@callback
	def _on_game_object_registered(self, event: _RefEvent, **kwargs):
		"""
		Callback function for the `gameObjectRegistered` event.
		:param event: The event to broadcast.
		:param kwargs: The event data.
		"""
		event(kwargs["time"], GameObjectID(kwargs["gameObjectId"]), Name(kwargs["gameObjectName"]))
	
	@callback
	def _on_game_object_reset(self, event: _RefEvent):
		"""
		Callback function for the `gameObjectReset` event.
		:param event: The event to broadcast.
		"""
		event()
	
	@callback
	def _on_game_object_unregistered(self, event: _RefEvent, **kwargs):
		"""
		Callback function for the `gameObjectUnregistered` event.
		:param event: The event to broadcast.
		:param kwargs: The event data.
		"""
		event(kwargs["time"], GameObjectID(kwargs["gameObjectId"]), Name(kwargs["gameObjectName"]))
	
	@callback
	def _on_state_changed(self, event: _RefEvent, **kwargs):
		"""
		Callback function for the `stateChanged` event.
		:param event: The event to broadcast.
		:param kwargs: The event data.
		"""
		group = kwargs["stateGroup"]
		group = WwiseObjectInfo(group["id"], group["name"], group["type"], group["path"])
		value = kwargs["state"]
		value = WwiseObjectInfo(value["id"], value["name"], value["type"], value["path"])
		event(group, value)
	
	@callback
	def _on_switch_changed(self, event: _RefEvent, **kwargs):
		"""
		Callback function for the `switchChanged` event.
		:param event: The event to broadcast.
		:param kwargs: The event data.
		"""
		group = kwargs["switchGroup"]
		group = WwiseObjectInfo(group["id"], group["name"], group["type"], group["path"])
		value = kwargs["switch"]
		value = WwiseObjectInfo(value["id"], value["name"], value["type"], value["path"])
		event(group, value, kwargs["gameObjectID"])
	
	def enable_profiler_data(self):
		"""
		Specifies the type of data you want to capture. Overrides the user's profiler settings.
		"""
	
	def get_audio_objects(self):
		"""
		Retrieves the Audio Objects at a specific profiler capture time.
		"""
	
	def get_busses(self):
		"""
		Retrieves the busses at a specific profiler capture time.
		"""
	
	def get_cpu_usage(self):
		"""
		Retrieves CPU usage statistics at a specific profiler capture time. This data can also be found
		in the Advanced Profiler, under the CPU tab. To ensure the CPU data is received,
		refer to `ak.wwise.core.profiler.enable_profiler_data`. The returned data includes "Inclusive" and
		"Exclusive" values, where "Inclusive" refers to the time spent in the element plus the time spent
		in any called elements, and "Exclusive" values pertain to execution only within the element
		itself.
		"""
	
	def get_cursor_time(self):
		"""
		Returns the current time of the specified profiler cursor, in milliseconds.
		"""
	
	def get_game_objects(self):
		"""
		Retrieves the game objects at a specific profiler capture time.
		"""
	
	def get_loaded_media(self):
		"""
		Retrieves the loaded media at a specific profiler capture time. This data can also be found in
		the Advanced Profiler, under the Loaded Media tab. To ensure the Loaded Media data is received,
		refer to `ak.wwise.core.profiler.enable_profiler_data`.
		"""
	
	def get_performance_monitor(self):
		"""
		Retrieves the Performance Monitor statistics at a specific profiler capture time. Refer to Wwise
		Authoring Performance Monitor Counter Identifiers for the available counters.
		"""
	
	def get_rtpcs(self):
		"""
		Retrieves active RTPCs at a specific profiler capture time.
		"""
	
	def get_streamed_media(self):
		"""
		Retrieves the streaming media at a specific profiler capture time. This data can also be found in
		the Advanced Profiler, under the Streams tab. To ensure the Streams data is received,
		refer to `ak.wwise.core.profiler.enable_profiler_data`.
		"""
	
	def get_voice_contributions(self):
		"""
		Retrieves all parameters affecting voice volume, highpass and lowpass for a voice path,
		resolved from pipeline IDs.
		"""
	
	def get_voices(self):
		"""
		Retrieves the voices at a specific profiler capture time.
		"""
	
	def save_capture(self):
		"""
		Saves profiler as a .prof file according to the given file path.
		"""
	
	def start_capture(self):
		"""
		Starts the profiler capture and returns the time at the beginning of the capture, in milliseconds.
		"""
	
	def stop_capture(self):
		"""
		Stops the profiler capture and returns the time at the end of the capture, in milliseconds.
		"""
