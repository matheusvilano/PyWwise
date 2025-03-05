# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from simplevent import RefEvent as _RefEvent
from waapi import WaapiClient as _WaapiClient

from pywwise.aliases import ListOrTuple, SystemPath
from pywwise.decorators import callback
from pywwise.enums import (EAudioObjectOptions, EBusOptions, EDataTypes, EObjectType, EReturnOptions, ETimeCursor,
                           EVoicePipelineReturnOptions)
from pywwise.primitives import GameObjectID, GUID, Name, ProjectPath, ShortID
from pywwise.structs import (ActiveRTPCInfo, AudioObjectInfo, AudioObjectMetadata, BusPipelineInfo, CPUStatisticsInfo,
                             GameObjectRegistrationData, LoadedMediaInfo, PerformanceMonitorCounterInfo,
                             PlayingVoiceProperties, StreamObjectInfo, VoiceContributionHierarchy,
                             VoiceContributionParameter, VoiceInspectorContribution, WwiseObjectInfo)
from pywwise.waapi.ak.wwise.core.capture_log import CaptureLog as _CaptureLog


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
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_gameobjectregistered.html
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
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_gameobjectreset.html
        \nSent when the game objects have been reset, such as closing a connection to a game while profiling.
        """
        
        self._game_object_reset = self._client.subscribe("ak.wwise.core.profiler.gameObjectReset",
                                                         self._on_game_object_reset)
        
        self.game_object_unregistered = _RefEvent(int, GameObjectID, Name)
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_gameobjectunregistered.html
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
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_statechanged.html
        \nSent when a state group state has been changed. Does not require the profiler capture log to be started.
        \n**Event Data**:
        \n-A WwiseObjectInfo instance containing information about the State Group where the change happened.
        \n-A WwiseObjectInfo instance containing information about the new active State.
        """
        
        self._state_changed = self._client.subscribe("ak.wwise.core.profiler.stateChanged",
                                                     self._on_state_changed, change_args)
        
        self.switch_changed = _RefEvent(WwiseObjectInfo, WwiseObjectInfo, GameObjectID)
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_switchchanged.html
        \nSent when a switch group state has been changed. Does not require the profiler capture log to be started.
        \n**Event Data**:
        \n-A WwiseObjectInfo instance containing information about the Switch Group where the change happened.
        \n-A WwiseObjectInfo instance containing information about the new active Switch.
        \n-The ID of the game object on which the change happened.
        """
        
        self._switch_changed = self._client.subscribe("ak.wwise.core.profiler.switchChanged",
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
        group = WwiseObjectInfo.from_dict(kwargs["stateGroup"])
        value = WwiseObjectInfo.from_dict(kwargs["state"])
        event(group, value)
    
    @callback
    def _on_switch_changed(self, event: _RefEvent, **kwargs):
        """
        Callback function for the `switchChanged` event.
        :param event: The event to broadcast.
        :param kwargs: The event data.
        """
        group = WwiseObjectInfo.from_dict(kwargs["switchGroup"])
        value = WwiseObjectInfo.from_dict(kwargs["switch"])
        event(group, value, kwargs["gameObjectID"])
    
    def enable_profiler_data(self, data_types: ListOrTuple[tuple[EDataTypes, bool]]) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_enableprofilerdata.html \n
        Specifies the type of data you want to capture. Overrides the user's profiler settings.
        :param data_types: An array of tuples. Each tuple contains the data type you want to capture via an enum and
                           if profiler capture will be enabled for said data type (Defaults to true).
        :return: It returns a bool indicating whether the call was successful or not.
        """
        data_types = list(dict.fromkeys(data_types))
        args = {"dataTypes": list()}
        
        for data_type in data_types:
            args["dataTypes"].append({"dataType": data_type[0], "enabled": data_type[1]})
        
        return self._client.call("ak.wwise.core.profiler.enableProfilerData", args) is not None
    
    def get_audio_objects(self, time: ETimeCursor | int, bus_pipeline_id: int = None,
                          returns: ListOrTuple[EAudioObjectOptions] = None) -> tuple[AudioObjectInfo, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_getaudioobjects.html \n
        Retrieves the Audio Objects at a specific profiler capture time.
        :param time: Time in milliseconds to query for Audio Objects, or a Time Cursor from which to acquire the time.
                     This parameter can have 2 possible values: int or ETimeCursor. The int is the time to query.
                     The ETimeCursor can have two values: user or capture. The User Time Cursor is the one that can
                     be manipulated by the user, while the Capture Time Cursor represents the latest time of the current
                     capture.
        :param bus_pipeline_id: Unsigned Integer 32-bit. Range: [0,4294967295] The pipeline ID of a Bus instance to get.
        :param returns: Members to return for each Audio Object. Defaults to Audio Object ID, Bus Pipeline ID,
                        Instigator Pipeline ID and Effect Class ID.
        :return: For each profiled audio object, an AudioObjectInfo containing an object's ID, pipeline ID,
                 instigator pipeline ID, effect class ID and a dictionary containing additional information
                 (requested via `return_options`). When accessing the values in the dictionary, use the
                 EAudioObjectOptions enum as the keys. If this function call fails, an empty tuple is returned.
        """
        args = {"time": time}
        
        if bus_pipeline_id is not None:
            args["busPipelineId"] = bus_pipeline_id
        
        returns = list(returns) if returns is not None else list[EAudioObjectOptions]()
        returns.extend((EAudioObjectOptions.AUDIO_OBJECT_ID, EAudioObjectOptions.BUS_PIPELINE_ID,
                        EAudioObjectOptions.INSTIGATOR_PIPELINE_ID, EAudioObjectOptions.EFFECT_CLASS_ID,))
        options = {"return": list(dict.fromkeys(returns))}  # Remove duplicates
        
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
                                        meta.get("sourceShortID", ShortID.get_null()),
                                        meta.get("metadataName", Name.get_null()),
                                        meta.get("sourceID", GUID.get_null()),
                                        meta.get("sourceName", Name.get_null())))
            objects.append(info)
        
        return tuple(objects)
    
    def get_busses(self, time: ETimeCursor | int, bus_pipeline_id: int = None,
                   returns: ListOrTuple[EBusOptions] = None) -> tuple[BusPipelineInfo, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_getbusses.html \n
        Retrieves the busses at a specific profiler capture time.
        :param time: Time in milliseconds to query for a bus pipeline, or a Time Cursor from which to acquire the time.
                     This parameter can have 2 possible values: int or ETimeCursor. The int is the time to query.
                     The ETimeCursor can have two values: user or capture. The User Time Cursor is the one that can
                     be manipulated by the user, while the Capture Time Cursor represents the latest time of the current
                     capture.
        :param bus_pipeline_id: Unsigned Integer 32-bit. Range: [0,4294967295] The pipeline ID of a single bus instance
                                to get.
        :param returns: Members to return for each bus. If `None` the default returns are used: Pipeline ID, GameObject
                        ID, and Object GUID.
        :return: For each profiled bus pipeline, a BusPipelineInfo containing a Pipeline ID, GameObject ID,
                 Object GUID and a dictionary containing additional information
                 (requested via `return_options`). When accessing the values in the dictionary, use the
                 EBusOptions enum as the keys. If this function call fails, an empty tuple is returned.
        """
        args = {"time": time}
        
        if bus_pipeline_id is not None:
            args["busPipelineId"] = bus_pipeline_id
        
        returns = list(returns) if returns is not None else list[EBusOptions]()
        returns.extend([EBusOptions.PIPELINE_ID, EBusOptions.GAME_OBJECT_ID, EBusOptions.OBJECT_GUID])
        options = {"return": list(dict.fromkeys(returns))}  # Remove duplicates
        
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
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_getcpuusage.html \n
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
        :return: A tuple of CPUStatisticsInfo instances containing information about the amount of CPU percentage used
                 by each element.
        """
        args = {"time": time}
        
        results: dict[str, list[dict[str, int | float | str]]] = self._client.call("ak.wwise.core.profiler.getCpuUsage",
                                                                                   args)
        
        if results is None:
            return tuple[CPUStatisticsInfo, ...]()
        
        results: list[dict[str, int | float | str]] = results.get("return")  # Simplifying data structure.
        
        if not results:  # Empty.
            return tuple[CPUStatisticsInfo, ...]()
        
        stats = list[CPUStatisticsInfo]()
        
        for result in results:
            element_name = result.get("elementName", "")
            class_id = result.get("id", -1)
            instances = result.get("instances", -1)
            etype = result.get("type", "")
            percent_inclusive = result.get("percentInclusive", -1.0)
            percent_exclusive = result.get("percentExclusive", -1.0)
            ms_inclusive = result.get("millisecondsInclusive", -1.0)
            ms_exclusive = result.get("millisecondsExclusive", -1.0)
            stats.append(CPUStatisticsInfo(element_name, class_id, instances, etype, percent_inclusive,
                                           percent_exclusive, ms_inclusive, ms_exclusive))
        
        return tuple(stats)
    
    def get_cursor_time(self, time: ETimeCursor) -> int:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_getcursortime.html \n
        Returns the current time of the specified profiler cursor, in milliseconds.
        :param time: Time Cursor from which to acquire the time.
        :return: The current position of the specified Time Cursor, in ms. If function fails, it returns -1.
        """
        args = {"time": time}
        
        result = self._client.call("ak.wwise.core.profiler.getCursorTime", args)
        result = result.get("return")
        
        if result is None or result < 0:
            return -1
        
        return result
    
    def get_game_objects(self, time: ETimeCursor | int) -> tuple[GameObjectRegistrationData, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_getgameobjects.html \n
        Retrieves the game objects at a specific profiler capture time.
        :param time: The time in milliseconds to query for game objects. This parameter can have 2 possible values: int
                     or ETimeCursor. The int is the time to query. The ETimeCursor can have two values: user or capture.
                     The User Time Cursor is the one that can be manipulated by the user, while the Capture Time Cursor
                     represents the latest time of the current capture.
        :return: A tuple of objects containing game object registration data. When accessing the values in the
                 dictionary, use the EGameObjectRegistrationDataMembers enum as the keys. If this function call fails,
                 an empty tuple is returned.
        """
        args = {"time": time}
        
        results = self._client.call("ak.wwise.core.profiler.getGameObjects", args)
        
        if results is None:
            return tuple[GameObjectRegistrationData, ...]()
        
        results = results.get("return")
        
        if not results:  # Empty.
            return tuple[GameObjectRegistrationData, ...]()
        
        objects = list[GameObjectRegistrationData]()
        
        for result in results:
            ak_id = GameObjectID(result.get("id", GameObjectID.get_null()))
            name = result.get("name", "")
            register_time = result.get("registerTime", -1)
            unregister_time = result.get("unregisterTime", -1)
            objects.append(GameObjectRegistrationData(ak_id, name, register_time, unregister_time))
        
        return tuple(objects)
    
    def get_loaded_media(self, time: ETimeCursor | int) -> tuple[LoadedMediaInfo, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_getloadedmedia.html \n
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
        args = {"time": time}
        
        results = self._client.call("ak.wwise.core.profiler.getLoadedMedia", args)
        results = results.get("return")
        
        if results is None:
            return tuple[LoadedMediaInfo, ...]()
        
        loaded_media = list[LoadedMediaInfo]()
        
        for result in results:
            media_id = ShortID(result.get("mediaId", ShortID.get_null()))
            file_name = Name(result.get("fileName", Name.get_null()))
            audio_format = result.get("format", "")
            size = result.get("size", -1)
            sound_bank = Name(result.get("soundBank", Name.get_null()))
            loaded_media.append(LoadedMediaInfo(media_id, file_name, audio_format, size, sound_bank))
        
        return tuple[LoadedMediaInfo, ...](loaded_media)
    
    def get_meters(self, time: ETimeCursor | int, returns: ListOrTuple[EReturnOptions] = None, platform: str = None,
                   language: str = None) -> tuple[WwiseObjectInfo, ...]:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_getmeters.html \n
        Retrieves the Meter data for all registered buses, aux buses and devices. Only the master audio bus is
        registered by default. Use `ak.wwise.core.profiler.registerMeter` for other buses, before retrieval of the
        meter data.
        :param time: Time in milliseconds to query for media, or a Time Cursor from which to acquire the time.
                     This parameter can have 2 possible values: int or ETimeCursor. The int is the time to query. The
                     ETimeCursor can have two values: user or capture. The User Time Cursor is the one that can be
                     manipulated by the user, while the Capture Time Cursor represents the latest time of the current
                     capture.
        :param returns: The additional return options. By default, this function returns only the GUID and Name
                        of the selected objects. Duplicates are ignored.
        :param platform: If specified, this function will get information from the specified platform instead of the
                         current platform.
        :param language: If specified, this function will get information from the specified language instead of the
                         current language.
        :returns: For each selected object, a WwiseObjectInfo containing an object's GUID, name, path, type, and a
                  dictionary containing additional information (requested via `return_options`). When accessing the
                  values in the dictionary, use the EReturnOptions enum as the keys. If this function call fails, an
                  empty tuple is returned.
        """
        args = {"time": time}
        
        returns = list(dict.fromkeys(returns)) if returns is not None else list[EReturnOptions]()
        returns.extend(EReturnOptions.get_defaults())
        
        options = {"return": returns}
        
        if platform is not None:
            options["platform"] = platform
        if language is not None:
            options["language"] = language
        
        results = self._client.call("ak.wwise.core.profiler.getMeters", args, options=options)
        results = results.get("objects") if results is not None else None
        if results is None:
            return ()
        
        objects = list[WwiseObjectInfo]()
        
        for result in results:
            guid = GUID(result[EReturnOptions.GUID])
            name = Name(result[EReturnOptions.NAME])
            typename = EObjectType.from_type_name(result[EReturnOptions.TYPE])
            path = ProjectPath(result[EReturnOptions.PATH])
            other = {key: value for key, value in result.items() if key not in EReturnOptions.get_defaults()}
            objects.append(WwiseObjectInfo(guid, name, typename, path, other))
        
        return tuple(objects)
    
    def get_performance_monitor(self, time: ETimeCursor | int) -> tuple[PerformanceMonitorCounterInfo, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_getperformancemonitor.html \n
        Retrieves the Performance Monitor statistics at a specific profiler capture time. Refer to Wwise Authoring
        Performance Monitor Counter Identifiers for the available counters.
        :param time: Time in milliseconds to query for media, or a Time Cursor from which to acquire the time.
                     This parameter can have 2 possible values: int or ETimeCursor. The int is the time to query. The
                     ETimeCursor can have two values: user or capture. The User Time Cursor is the one that can be
                     manipulated by the user, while the Capture Time Cursor represents the latest time of the current
                     capture.
        :return: A tuple of performance monitor counter information. When accessing the values in the dictionary use the
                 EPerformanceMonitorMembers enum as the keys. If this function call fails, an empty tuple is returned.
        """
        args = {"time": time}
        
        results = self._client.call("ak.wwise.core.profiler.getPerformanceMonitor", args)
        
        if results is None:
            return tuple[PerformanceMonitorCounterInfo, ...]()
        
        results = results.get("return")
        
        if not results:  # Empty.
            return tuple[PerformanceMonitorCounterInfo, ...]()
        
        entries = list[PerformanceMonitorCounterInfo]()
        
        for result in results:
            name: str = result.get("name", "")
            identifier: str = result.get("id", "")
            value: float = result.get("value", float("-inf"))
            entries.append(PerformanceMonitorCounterInfo(name, identifier, value))
        
        return tuple[PerformanceMonitorCounterInfo, ...](entries)
    
    def get_rtpcs(self, time: ETimeCursor | int) -> tuple[ActiveRTPCInfo, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_getrtpcs.html \n
        Retrieves active RTPCs at a specific profiler capture time.
        :param time: Time in milliseconds to query for RTPCs, or a Time Cursor from which to acquire the time.
                     This parameter can have 2 possible values: int or ETimeCursor. The int is the time to query. The
                     ETimeCursor can have two values: user or capture. The User Time Cursor is the one that can be
                     manipulated by the user, while the Capture Time Cursor represents the latest time of the current
                     capture.
        :return: A tuple of RTPCs associated with a playing voice. When accessing the values in the dictionary use the
                 EActiveRTPCMembers enum as the keys. If this function call fails, an empty tuple is returned.
        """
        args = {"time": time}
        
        results = self._client.call("ak.wwise.core.profiler.getRTPCs", args)
        
        if results is None:
            return tuple[ActiveRTPCInfo, ...]()
        
        results = results.get("return", ())
        
        if not results:  # Empty.
            return tuple[ActiveRTPCInfo, ...]()
        
        rtpcs = list[ActiveRTPCInfo]()
        
        for result in results:
            guid = GUID(result.get("id", GUID.get_null()))
            name = Name(result.get("name", Name.get_null()))
            obj_id = GameObjectID(result.get("gameObjectId", GameObjectID.get_null()))
            value = result.get("value", float("-inf"))
            rtpcs.append(ActiveRTPCInfo(guid, name, obj_id, value))
        
        return tuple[ActiveRTPCInfo, ...](rtpcs)
    
    def get_streamed_media(self, time: ETimeCursor | int) -> tuple[StreamObjectInfo, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_getstreamedmedia.html \n
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
        args = {"time": time}
        
        results = self._client.call("ak.wwise.core.profiler.getStreamedMedia", args)
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
    
    def get_voice_contributions(self, time: ETimeCursor | int, voice_pipeline_id: int,
                                bus_pipeline_ids: ListOrTuple[int] = None) -> VoiceContributionHierarchy | None:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_getvoicecontributions.html \n
        Retrieves all parameters affecting voice volume, highpass and lowpass for a voice path,
        resolved from pipeline IDs.
        :param time: Time in milliseconds to query for RTPCs, or a Time Cursor from which to acquire the time.
                     This parameter can have 2 possible values: int or ETimeCursor. The int is the time to query. The
                     ETimeCursor can have two values: user or capture. The User Time Cursor is the one that can be
                     manipulated by the user, while the Capture Time Cursor represents the latest time of the current
                     capture.
        :param voice_pipeline_id: The pipeline ID of the voice to get contributions from. Identifies a playing voice
                                  instance ID
        :param bus_pipeline_ids: The pipeline IDs of buses belonging to a common voice path. An empty array defaults
                                 to the dry path. Identifies a playing voice instance ID
        :return: The hierarchy of objects with parameters contributing to the voice, ordered from top-level parent to
                 the voice object. If no information was found, `None` is returned.
        """
        args = {"time": time, "voicePipelineID": voice_pipeline_id}
        
        if bus_pipeline_ids is not None:
            args["bussesPipelineID"] = bus_pipeline_ids
        
        results = self._client.call("ak.wwise.core.profiler.getVoiceContributions", args)
        
        if results is None:
            return None
        
        results = results.get("return")
        
        if results is None:
            return None
        
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
                    get_children(inspector, child["children"])  # Recursive call
        
        get_children(hierarchy, results.get("objects", list[dict]()))
        
        if results is not None:
            return hierarchy
    
    def get_voices(self, time: ETimeCursor | int, voice_pipeline_id: int = None,
                   returns: ListOrTuple[EVoicePipelineReturnOptions] = None) -> tuple[PlayingVoiceProperties, ...]:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_getvoices.html \n
        Retrieves the voices at a specific profiler capture time.
        :param time: Time in milliseconds to query for RTPCs, or a Time Cursor from which to acquire the time.
                     This parameter can have 2 possible values: int or ETimeCursor. The int is the time to query. The
                     ETimeCursor can have two values: user or capture. The User Time Cursor is the one that can be
                     manipulated by the user, while the Capture Time Cursor represents the latest time of the current
                     capture.
        :param voice_pipeline_id: The pipeline ID of the voice to get contributions from. Identifies a playing voice
                                  instance ID
        :param returns: The additional return options. By default, this function returns only the Pipeline ID,
                        Game Object ID, and Object GUID.
        :return: An array of playing voices and their properties. Specify additional return options to extract more
                 data.
        """
        args = {"time": time}
        returns = list(returns) if returns is not None else list[EVoicePipelineReturnOptions]()
        returns.extend((EVoicePipelineReturnOptions.PIPELINE_ID,
                        EVoicePipelineReturnOptions.GAME_OBJECT_ID,
                        EVoicePipelineReturnOptions.OBJECT_GUID,))
        options = {"return": list(dict.fromkeys(returns))}  # Remove duplicates
        
        if voice_pipeline_id is not None:
            args["voicePipelineID"] = voice_pipeline_id
        
        results = self._client.call("ak.wwise.core.profiler.getVoices", args, options=options)
        results = results.get("return") if results is not None else None
        
        if results is None:
            return ()
        
        voices = list[PlayingVoiceProperties]()
        
        for voice in results:
            pipeline_id = int(voice[EVoicePipelineReturnOptions.PIPELINE_ID])
            game_object_id = GameObjectID(voice[EVoicePipelineReturnOptions.GAME_OBJECT_ID])
            object_guid = GUID(voice[EVoicePipelineReturnOptions.OBJECT_GUID])
            other = {key: value for key, value in voice.items() if key not in returns}
            voices.append(PlayingVoiceProperties(pipeline_id, game_object_id, object_guid, other))
        
        return tuple(voices)
    
    def register_meter(self, object_to_register: GUID | ProjectPath | str) -> bool:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_registermeter.html \n
        Registers a bus, an aux bus or device to receive meter data. Only the master audio bus is registered by default.
        Use `ak.wwise.core.profiler.getMeters` to retrieve the meter data after registering. Every call to
        `ak.wwise.core.profiler.registerMeter` must have a matching call to `ak.wwise.core.profiler.unregisterMeter`.
        :param object_to_register: The ID (GUID), name, or path of the object to receive meter data. This object must
                                   be a bus, an aux bus or a device. The name of the object qualified by its type or
                                   Short ID in the form of type:name or Global:shortId. Only object types that have
                                   globally-unique names or Short Ids are supported. Ex: Event:Play_Sound_01
        :return: Returns a boolean that indicates if the call was successful.
        """
        result = self._client.call("ak.wwise.core.profiler.registerMeter", {"object": object_to_register})
        return True if result is not None else False
    
    def save_capture(self, file_path: SystemPath) -> bool:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_savecapture.html \n
        Saves profiler as a .prof file according to the given file path.
        :param file_path: The file path to save the profiler to. Make sure to include .prof file extension.
                          E.g. C:\\MyProject\\capture.prof
        :return: True if the profiler was saved, False otherwise.
        """
        if file_path is None:
            return False
        
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        args = {"file": file_path}
        
        return self._client.call("ak.wwise.core.profiler.saveCapture", args) is not None
    
    def start_capture(self) -> int:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_startcapture.html \n
        Starts the profiler capture and returns the time at the beginning of the capture, in milliseconds.
        :return: The time at the beginning of the capture, in milliseconds. If method fails to call, it will return -1.
        """
        result = self._client.call("ak.wwise.core.profiler.startCapture", {})
        
        if result is not None:
            return result.get("return")
        else:
            return -1
    
    def stop_capture(self) -> int:
        """
        https://www.audiokinetic.com/library/edge/?source=SDK&id=ak_wwise_core_profiler_stopcapture.html \n
        Stops the profiler capture and returns the time at the end of the capture, in milliseconds.
        :return: The time at the end of the capture, in milliseconds. If method fails to call, it will return -1.
        """
        result = self._client.call("ak.wwise.core.profiler.stopCapture", {})
        return result.get("return", -1) if result is not None else -1
    
    def unregister_meter(self, object_to_unregister: GUID | ProjectPath | str):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_profiler_unregistermeter.html \n
        Unregisters a bus or device that was registered with `ak.wwise.core.profiler.registerMeter`.
        :param object_to_unregister: The ID (GUID), name, or path of the object to receive meter data. This object must
                                     be a bus, an aux bus or a device. The name of the object qualified by its type or
                                     Short ID in the form of type:name or Global:shortId. Only object types that have
                                     globally-unique names or Short Ids are supported. Ex: Event:Play_Sound_01
        :return: Returns a boolean that indicates if the call was successful.
        """
        return self._client.call("ak.wwise.core.profiler.unregisterMeter",
                                 {"object": object_to_unregister}) is not None
