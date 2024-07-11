from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient
from pywwise.ak.wwise.core.capture_log import CaptureLog as _CaptureLog
from pywwise.enums import EBusOptions, EDataTypes, EAudioObjectOptions, ETimeCursor
from pywwise.structs import AudioObjectInfo, AudioObjectMetadata, BusPipelineInfo
from pywwise.types import GUID, Name, ShortID


class Profiler:
	"""ak.wwise.core.profiler"""
	
	def __init__(self, client: _WaapiClient):
		"""
		Constructor.
		:param client: The WAAPI client to use.
		"""
		self._client = client
		self.capture_log = _CaptureLog(client)
		
		# TODO: implement topics
		self.game_object_registered: _RefEvent
		self.game_object_reset: _RefEvent
		self.game_object_unregistered: _RefEvent
		self.state_changed: _RefEvent
		self.switch_changed: _RefEvent
	
	def enable_profiler_data(self, data_types: set[tuple[EDataTypes, bool]] = None) -> bool:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_enableprofilerdata.html \n
		Specifies the type of data you want to capture. Overrides the user's profiler settings.
		:param data_types: Tuple that contains the data type you want to capture via an enum and if profiler capture
		will be enabled for said data type (Defaults to true).
		:return: It returns a bool indicating whether the call was successful or not.
		"""
		if data_types is None:
			return False
		
		args = {"dataTypes": list()}
		
		for data_type in data_types:
			args["dataTypes"].append({"dataType": data_type[0], "enabled": data_type[1]})
		
		return self._client.call("ak.wwise.core.profiler.enableProfilerData", args) is not None
	
	def get_audio_objects(self, time: ETimeCursor | int, bus_pipeline_id: int = None,
	                      return_options: set[EAudioObjectOptions] = None) -> tuple[AudioObjectInfo, ...]:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_getaudioobjects.html \n
		Retrieves the Audio Objects at a specific profiler capture time. \n
		:param time: Time in milliseconds to query for Audio Objects, or a Time Cursor from which to acquire the time.
					 This parameter can have 2 possible values: int or ETimeCursor. The int is the time to query.
					 The ETimeCursor can have two values: user or capture. The User Time Cursor is the one that can
					 be manipulated by the user, while the Capture Time Cursor represents the latest time of the current
					 capture.
		:param bus_pipeline_id: Unsigned Integer 32-bit. Range: [0,4294967295] The pipeline ID of a Bus instance to get.
		:param return_options: Members to return for each Audio Object. Defaults to Audio Object ID, Bus Pipeline ID,
							   Instigator Pipeline ID and Effect Class ID.
		:return: For each profiled audio object, an AudioObjectInfo containing an object's ID, pipeline ID,
				 instigator pipeline ID, effect class ID and a dictionary containing additional information
				 (requested via `return_options`). When accessing the values in the dictionary, use the
				 EAudioObjectOptions enum as the keys. If this function call fails, an empty tuple is returned.
		"""
		if time is None:
			return tuple()
		
		args = {"time": time}
		
		if bus_pipeline_id is not None:
			args["busPipelineId"] = bus_pipeline_id
		
		returns = (EAudioObjectOptions.AUDIO_OBJECT_ID, EAudioObjectOptions.BUS_PIPELINE_ID,
		           EAudioObjectOptions.INSTIGATOR_PIPELINE_ID, EAudioObjectOptions.EFFECT_CLASS_ID)
		options = {"return": list(returns)}
		
		if return_options is not None:
			options["return"].extend(list(return_options))
		
		results = self._client.call("ak.wwise.core.profiler.getAudioObjects", args, options=options)
		results = results.get("return", list[dict]())
		
		objects = list[AudioObjectInfo]()
		
		for result in results:
			info = AudioObjectInfo(result[EAudioObjectOptions.AUDIO_OBJECT_ID],
			                       result[EAudioObjectOptions.BUS_PIPELINE_ID],
			                       result[EAudioObjectOptions.INSTIGATOR_PIPELINE_ID],
			                       result[EAudioObjectOptions.EFFECT_CLASS_ID],
			                       {k: v for k, v in result.items()
			                        if k not in returns and k != EAudioObjectOptions.METADATA})
			if result.get(EAudioObjectOptions.METADATA) is not None:
				info.other[EAudioObjectOptions.METADATA] = list()
			for meta in result.get(EAudioObjectOptions.METADATA, ()):
				info.other[EAudioObjectOptions.METADATA].append(
					AudioObjectMetadata(meta.get("metadataClassID", -1),
					                    meta.get("sourceShortID", ShortID.get_invalid()),
					                    meta.get("metadataName", Name.get_null()),
					                    meta.get("sourceID", GUID.get_zero()),
					                    meta.get("sourceName", Name.get_null())))
			objects.append(info)
		
		return tuple(objects)
		
	def get_busses(self, time: ETimeCursor | int, bus_pipeline_id: int = None,
	               return_options: set[EBusOptions] = None) -> tuple[BusPipelineInfo, ...]:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_getbusses.html \n
		Retrieves the busses at a specific profiler capture time.
		:param time: Time in milliseconds to query for Audio Objects, or a Time Cursor from which to acquire the time.
					 This parameter can have 2 possible values: int or ETimeCursor. The int is the time to query.
					 The ETimeCursor can have two values: user or capture. The User Time Cursor is the one that can
					 be manipulated by the user, while the Capture Time Cursor represents the latest time of the current
					 capture.
		:param bus_pipeline_id: Unsigned Integer 32-bit. Range: [0,4294967295] The pipeline ID of a single bus instance
								to get.
		:param return_options: Members to return for each bus. Defaults to Pipeline ID, GameObject ID, and Object GUID.
		:return: For each profiled bus pipeline, a BusPipelineInfo containing a Pipeline ID, GameObject ID,
				 Object GUID and a dictionary containing additional information
				 (requested via `return_options`). When accessing the values in the dictionary, use the
				 EBusOptions enum as the keys. If this function call fails, an empty tuple is returned.
		"""
		
		if time is None:
			return tuple()
		
		args = {"time": time}
		
		if bus_pipeline_id is not None:
			args["busPipelineId"] = bus_pipeline_id
		
		returns = (EBusOptions.PIPELINE_ID, EBusOptions.GAME_OBJECT_ID, EBusOptions.OBJECT_GUID)
		options = {"return": list(returns)}
		
		if return_options is not None:
			options["return"].extend(list(return_options))
		
		results = self._client.call("ak.wwise.core.profiler.getBusses", args, options=options)
		results = results.get("return")
		
		if results is None:
			return tuple()
		
		objects = list[BusPipelineInfo]()
		
		for result in results:
			info = BusPipelineInfo(result[EBusOptions.PIPELINE_ID],
			                       result[EBusOptions.GAME_OBJECT_ID],
			                       result[EBusOptions.OBJECT_GUID],
			                       {k: v for k, v in result.items()
			                        if k not in returns})
			objects.append(info)
		
		return tuple(objects)
	
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
