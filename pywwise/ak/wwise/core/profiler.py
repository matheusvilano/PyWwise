from dataclasses import fields
from typing import Any

from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient
from pywwise.ak.wwise.core.capture_log import CaptureLog as _CaptureLog
from pywwise.enums import EActiveRTPCMembers, EBusOptions, ECPUStatisticsMembers, EDataTypes, EAudioObjectOptions, \
	EGameObjectRegistrationDataMembers, \
	ELoadedMediaMembers, EPerformanceMonitorMembers, ETimeCursor
from pywwise.structs import ActiveRTPCInfo, AudioObjectInfo, AudioObjectMetadata, BusPipelineInfo, CPUStatisticsInfo, \
	GameObjectRegistrationData, LoadedMediaInfo, PerformanceMonitorCounterInfo, StreamObjectInfo, \
	VoiceContributionsReturnInfo
from pywwise.types import GUID, Name, ShortID


# from typing import List


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
		:param time: Time in milliseconds to query for a bus pipeline, or a Time Cursor from which to acquire the time.
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
	
	def get_cpu_usage(self, time: ETimeCursor | int) -> tuple[CPUStatisticsInfo, ...]:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_getcpuusage.html \n
		Retrieves CPU usage statistics at a specific profiler capture time. This data can also be found
		in the Advanced Profiler, under the CPU tab. To ensure the CPU data is received,
		refer to `ak.wwise.core.profiler.enable_profiler_data`. The returned data includes "Inclusive" and
		"Exclusive" values, where "Inclusive" refers to the time spent in the element plus the time spent
		in any called elements, and "Exclusive" values pertain to execution only within the element
		itself.
		:param time: Time in milliseconds to query for cpu data, or a Time Cursor from which to acquire the time.
					 This parameter can have 2 possible values: int or ETimeCursor. The int is the time to query.
					 The ETimeCursor can have two values: user or capture. The User Time Cursor is the one that can
					 be manipulated by the user, while the Capture Time Cursor represents the latest time of the current
					 capture.
		:return: For each element profiled, a CPUStatisticsInfo struct containing information about the amount of CPU
				 percentage used by each element is returned. When accessing the values in the dictionary, use the
				 ECPUStatisticsMembers enum as the keys. If this function call fails, an empty tuple is returned.
		"""
		if time is None:
			return tuple()
		
		args = {"time": time}
		
		results = self._client.call("ak.wwise.core.profiler.getCpuUsage", args)
		results = results.get("return")
		
		if results is None:
			return tuple()
		
		objects = list[CPUStatisticsInfo]()
		
		for result in results:
			info = CPUStatisticsInfo({k: v for k, v in result.items() if k not in ECPUStatisticsMembers})
			objects.append(info)
		
		return tuple(objects)
	
	def get_cursor_time(self, time: ETimeCursor) -> int:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_getcursortime.html \n
		Returns the current time of the specified profiler cursor, in milliseconds.
		:param time: Time Cursor from which to acquire the time.
		:return: The current position of the specified Time Cursor, in ms. If function fails, it returns -1.
		"""
		if time is None:
			return -1
		
		args = {"time": time}
		
		result = self._client.call("ak.wwise.core.profiler.getCursorTime ", args)
		result = result.get("return")
		
		if result is None or result < 0:
			return -1
		
		return result
	
	def get_game_objects(self, time: ETimeCursor | int) -> tuple[GameObjectRegistrationData, ...]:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_getgameobjects.html \n
		Retrieves the game objects at a specific profiler capture time.
		:param time: The time in milliseconds to query for game objects. This parameter can have 2 possible values: int
					 or ETimeCursor. The int is the time to query. The ETimeCursor can have two values: user or capture.
					 The User Time Cursor is the one that can be manipulated by the user, while the Capture Time Cursor
					 represents the latest time of the current capture.
		:return: A tuple of objects containing game object registration data. When accessing the values in the
				 dictionary, use the EGameObjectRegistrationDataMembers enum as the keys. If this function call fails,
				 an empty tuple is returned.
		"""
		
		if time is None:
			return tuple()
		
		args = {"time": time}
		
		results = self._client.call("ak.wwise.core.profiler.getGameObjects", args)
		results = results.get("return")
		
		if results is None:
			return tuple()
		
		objects = list[GameObjectRegistrationData]()
		
		for result in results:
			info = GameObjectRegistrationData(
				{k: v for k, v in result.items() if k not in EGameObjectRegistrationDataMembers})
			objects.append(info)
		
		return tuple(objects)
	
	def get_loaded_media(self, time: ETimeCursor | int) -> tuple[LoadedMediaInfo, ...]:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_getloadedmedia.html \n
		Retrieves the loaded media at a specific profiler capture time. This data can also be found in
		the Advanced Profiler, under the Loaded Media tab. To ensure the Loaded Media data is received,
		refer to `ak.wwise.core.profiler.enable_profiler_data`.
		:param time: Time in milliseconds to query for media, or a Time Cursor from which to acquire the time.
					 This parameter can have 2 possible values: int or ETimeCursor. The int is the time to query. The
					 ETimeCursor can have two values: user or capture. The User Time Cursor is the one that can be
					 manipulated by the user, while the Capture Time Cursor represents the latest time of the current
					 capture.
		:return: A tuple of loaded media information. When accessing the values in the dictionary, use the
				 ELoadedMediaMembers enum as the keys. If this function call fails, an empty tuple is returned.
		"""
		if time is None:
			return tuple()
		
		args = {"time": time}
		
		results = self._client.call("ak.wwise.core.profiler.getLoadedMedia", args)
		results = results.get("return")
		
		if results is None:
			return tuple()
		
		loaded_media = list[LoadedMediaInfo]()
		
		for result in results:
			info = LoadedMediaInfo({k: v for k, v in result.items() if k not in ELoadedMediaMembers})
			loaded_media.append(info)
		
		return tuple(loaded_media)
	
	def get_performance_monitor(self, time: ETimeCursor | int) -> tuple[PerformanceMonitorCounterInfo, ...]:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_getperformancemonitor.html \n
		Retrieves the Performance Monitor statistics at a specific profiler capture time. Refer to Wwise
		Authoring Performance Monitor Counter Identifiers for the available counters.
		:param time: Time in milliseconds to query for media, or a Time Cursor from which to acquire the time.
					 This parameter can have 2 possible values: int or ETimeCursor. The int is the time to query. The
					 ETimeCursor can have two values: user or capture. The User Time Cursor is the one that can be
					 manipulated by the user, while the Capture Time Cursor represents the latest time of the current
					 capture.
		:return: A tuple of performance monitor counter information. When accessing the values in the dictionary use the
				 EPerformanceMonitorMembers enum as the keys. If this function call fails, an empty tuple is returned.
		"""
		
		if time is None:
			return tuple()
		
		args = {"time": time}
		
		results = self._client.call("ak.wwise.core.profiler.getPerformanceMonitor", args)
		results = results.get("return")
		
		if results is None:
			return tuple()
		
		performance_monitor_counter = list[PerformanceMonitorCounterInfo]()
		
		for result in results:
			info = PerformanceMonitorCounterInfo(
				{k: v for k, v in result.items() if k not in EPerformanceMonitorMembers})
			performance_monitor_counter.append(info)
		
		return tuple(performance_monitor_counter)
	
	def get_rtpcs(self, time: ETimeCursor | int) -> tuple[ActiveRTPCInfo, ...]:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_getrtpcs.html \n
		Retrieves active RTPCs at a specific profiler capture time.
		:param time: Time in milliseconds to query for RTPCs, or a Time Cursor from which to acquire the time.
					 This parameter can have 2 possible values: int or ETimeCursor. The int is the time to query. The
					 ETimeCursor can have two values: user or capture. The User Time Cursor is the one that can be
					 manipulated by the user, while the Capture Time Cursor represents the latest time of the current
					 capture.
		:return: A tuple of RTPCs associated with a playing voice. When accessing the values in the dictionary use the
				 EActiveRTPCMembers enum as the keys. If this function call fails, an empty tuple is returned.
		"""
		
		if time is None:
			return tuple()
		
		args = {"time": time}
		
		results = self._client.call("ak.wwise.core.profiler.getRTPCs ", args)
		results = results.get("return")
		
		if results is None:
			return tuple()
		
		active_rtpcs = list[ActiveRTPCInfo]()
		
		for result in results:
			info = ActiveRTPCInfo(
				{k: v for k, v in result.items() if k not in EActiveRTPCMembers})
			active_rtpcs.append(info)
		
		return tuple(active_rtpcs)
	
	def get_streamed_media(self, time: ETimeCursor | int) -> tuple[StreamObjectInfo, ...]:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_getstreamedmedia.html \n
		Retrieves the streaming media at a specific profiler capture time. This data can also be found in
		the Advanced Profiler, under the Streams tab. To ensure the Streams data is received,
		refer to `ak.wwise.core.profiler.enable_profiler_data`.
		:param time: Time in milliseconds to query for RTPCs, or a Time Cursor from which to acquire the time.
					 This parameter can have 2 possible values: int or ETimeCursor. The int is the time to query. The
					 ETimeCursor can have two values: user or capture. The User Time Cursor is the one that can be
					 manipulated by the user, while the Capture Time Cursor represents the latest time of the current
					 capture.
		:return: Array of StreamObjectInfo, containing all data about how each of the streams is managed by the Wwise
		sound engine.
		"""
		
		if time is None:
			return tuple()
		
		args = {"time": time}
		
		results = self._client.call("ak.wwise.core.profiler.getStreamedMedia ", args)
		results = results.get("return")
		
		if results is None:
			return tuple()
		
		streams: list[StreamObjectInfo] = [StreamObjectInfo(
			device_name=result.get("deviceName"),
			stream_name=result.get("streamName"),
			file_size=result.get("fileSize"),
			file_position=result.get("filePosition"),
			priority=result.get("priority"),
			bandwidth_total=result.get("bandwidthTotal"),
			bandwidth_low_level=result.get("bandwidthLowLevel"),
			referenced_memory=result.get("referencedMemory"),
			estimated_throughput=result.get("estimatedThroughput"),
			active=result.get("active"),
			target_buffer_size=result.get("targetBufferSize"),
			buffer_status_buffered=result.get("bufferStatusBuffered"),
		) for result in results]
		
		return tuple(streams)
	
	def get_voice_contributions(self, time: ETimeCursor | int, voice_pipeline_id: float,
	                            busses_pipeline_id: tuple = None) -> tuple[VoiceContributionsReturnInfo, ...]:
		"""
		https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_getvoicecontributions.html \n
		Retrieves all parameters affecting voice volume, highpass and lowpass for a voice path,
		resolved from pipeline IDs.
		:param time: Time in milliseconds to query for RTPCs, or a Time Cursor from which to acquire the time.
					 This parameter can have 2 possible values: int or ETimeCursor. The int is the time to query. The
					 ETimeCursor can have two values: user or capture. The User Time Cursor is the one that can be
					 manipulated by the user, while the Capture Time Cursor represents the latest time of the current
					 capture.
		:param voice_pipeline_id: The pipeline ID of the voice to get contributions from. Identifies a playing voice
		instance ID
		:param busses_pipeline_id: The pipeline IDs of busses belonging to a common voice path. An empty array defaults
		to the dry path. Identifies a playing voice instance ID
		:return The hierarchy of objects with parameters contributing to the voice, ordered from top-level parent to
		the voice object
		"""
		
		if time is None or voice_pipeline_id is None:
			return tuple()
		
		args = {"time": time, "voicePipelineID": voice_pipeline_id}
		
		if busses_pipeline_id is not None:
			args["bussesPipelineID"] = busses_pipeline_id
			
		results = self._client.call("ak.wwise.core.profiler.getVoiceContributions", args)
		
		if results is None:
			return ()
		
		hierarchy = VoiceContributionHierarchy(results.get("volume", 0.0),
		                                       results.get("LPF", 0.0),
		                                       results.get("HPF", 0.0))
		
		def get_children(parent: VoiceContributionHierarchy | VoiceInspectorContribution, children: list[dict]):
			for child in children:
				inspector = VoiceInspectorContribution(child["name"], child["volume"], child["LPF"], child["HPF"])
				for param in child["parameters"]:
					parameter = VoiceContributionParameter(param["propertyType"], param["reason"], param["driver"],
					                                       param["driverValue"], param["value"])
					inspector.parameters.append(parameter)
				match parent:
					case VoiceContributionHierarchy():
						parent.objects.append(inspector)
					case VoiceInspectorContribution():
						parent.children.append(inspector)
				if len(child.get("children", ())) > 0:
					get_children(inspector, child["children"])
		
		get_children(hierarchy, results.get("objects", list[dict]()))
		
		if results is None:
			return tuple()
		
		# Add code for the proper 3 indented dictionaries
	
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
