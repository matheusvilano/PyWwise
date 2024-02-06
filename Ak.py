import waapi
import typing

WaapiClient: typing.TypeAlias = waapi.WaapiClient


def _waapimethod(function: typing.Callable):
    """
    Decorates a method as a WAAPI method, adding WaapiClient-related capabilities to it.
    :param function: The function to decorate.
    :return: The wrapper function; essentially, the decoration.
    """

    def wrapper(cls, *args, **kwargs):
        if kwargs.get("client") is None:  # Instantiate a local WaapiClient if client is None
            kwargs["client"] = WaapiClient()
        return function(cls, *args, **kwargs)

    return wrapper


class SoundEngine:
    """ak.soundengine"""

    @classmethod
    @_waapimethod
    def execute_action_on_event(cls, *, client: WaapiClient = None, event: str | int, action_type: int,
                                game_object: int, transition_duration: int, fade_curve: int) -> None:
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_executeactiononevent.html
        \nExecutes an action on all nodes that are referenced in the specified event in a Play action.
        """
        args = {"event": event, "actionType": action_type, "gameObject": game_object,
                "transitionDuration": transition_duration, "fadeCurve": fade_curve}
        client.call("ak.soundengine.executeActionOnEvent", args)

    @classmethod
    @_waapimethod
    def get_state(cls, *, client: WaapiClient = None, state_group: str):
        """
        https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_soundengine_getstate.html
        \nGets the current state of a State Group. When using setState just prior to getState, allow a brief delay
        (no more than 10ms) for the information to update in the sound engine.
        """
        args = {"stateGroup": state_group}
        client.call("ak.soundengine.getState", args)

    @classmethod
    @_waapimethod
    def get_switch(cls, *, client: WaapiClient = None, switch_group: str, game_object: int):
        """
        Gets the current state of a Switch Group for a given Game Object.
        """
        args = {"switchGroup": switch_group, "gameObject": game_object}
        client.call("ak.soundengine.getSwitch", args)

    @classmethod
    @_waapimethod
    def load_bank(cls, *, client: WaapiClient = None):
        """
        Load a SoundBank. See `AK::SoundEngine::LoadBank`.
        """

    @classmethod
    @_waapimethod
    def post_event(cls, *, client: WaapiClient = None):
        """
        Asynchronously post an Event to the sound engine (by event ID). See `AK::SoundEngine::PostEvent`.
        """

    @classmethod
    @_waapimethod
    def post_msg_monitor(cls, *, client: WaapiClient = None):
        """
        Display a message in the Profiler's Capture Log view.
        """

    @classmethod
    @_waapimethod
    def post_trigger(cls, *, client: WaapiClient = None):
        """
        Posts the specified Trigger. See `AK::SoundEngine::PostTrigger`.
        """

    @classmethod
    @_waapimethod
    def register_game_obj(cls, *, client: WaapiClient = None):
        """
        Register a game object. Registering a game object twice does nothing. Unregistering it once unregisters
        it no matter how many times it has been registered. See `AK::SoundEngine::RegisterGameObj`.
        """

    @classmethod
    @_waapimethod
    def reset_rtpc_value(cls, *, client: WaapiClient = None):
        """
        Resets the value of a real-time parameter control to its default value, as specified in the Wwise
        project. See `AK::SoundEngine::ResetRTPCValue`.
        """

    @classmethod
    @_waapimethod
    def seek_on_event(cls, *, client: WaapiClient = None):
        """
        Seeks inside all playing objects that are referenced in Play Actions of the specified Event. See
        `AK::SoundEngine::SeekOnEvent`.
        """

    @classmethod
    @_waapimethod
    def set_default_listeners(cls, *, client: WaapiClient = None):
        """
        Sets the default active listeners for all subsequent game objects that are registered. See
        `AK::SoundEngine::SetDefaultListeners`.
        """

    @classmethod
    @_waapimethod
    def set_game_object_aux_send_values(cls, *, client: WaapiClient = None):
        """
        Sets the Auxiliary Busses to route the specified game object. See
        `AK::SoundEngine::SetGameObjectAuxSendValues`.
        """

    @classmethod
    @_waapimethod
    def set_game_object_output_bus_volume(cls, *, client: WaapiClient = None):
        """
        Sets the Auxiliary Buses to route the specified game object. See
        `AK::SoundEngine::SetGameObjectAuxSendValues`.
        """

    @classmethod
    @_waapimethod
    def set_listeners(cls, *, client: WaapiClient = None):
        """
        Sets a single game object's active listeners. By default, all new game objects have no listeners active,
        but this behavior can be overridden with `SetDefaultListeners()`. Inactive listeners are not computed. See
        `AK::SoundEngine::SetListeners`.
        """

    @classmethod
    @_waapimethod
    def set_listener_spatialization(cls, *, client: WaapiClient = None):
        """
        Sets a listener's spatialization parameters. This lets you define listener-specific volume offsets for
        each audio channel. See `AK::SoundEngine::SetListenerSpatialization`.
        """

    @classmethod
    @_waapimethod
    def set_multiple_positions(cls, *, client: WaapiClient = None):
        """
        Sets multiple positions for a single game object. Setting multiple positions for a single game object is
        a way to simulate multiple emission sources while using the resources of only one voice. This can be used
        to simulate wall openings, area sounds, or multiple objects emitting the same sound in the same area. See
        `AK::SoundEngine::SetMultiplePositions`.
        """

    @classmethod
    @_waapimethod
    def set_object_obstruction_and_occlusion(cls, *, client: WaapiClient = None):
        """
        Set a game object's obstruction and occlusion levels. This function is used to affect how an object
        should be heard by a specific listener. See `AK::SoundEngine::SetObjectObstructionAndOcclusion`.
        """

    @classmethod
    @_waapimethod
    def set_position(cls, *, client: WaapiClient = None):
        """
        Sets the position of a game object. See `AK::SoundEngine::SetPosition`.
        """

    @classmethod
    @_waapimethod
    def set_rtpc_value(cls, *, client: WaapiClient = None):
        """
        Sets the value of a real-time parameter control. See `AK::SoundEngine::SetRTPCValue`.
        """

    @classmethod
    @_waapimethod
    def set_scaling_factor(cls, *, client: WaapiClient = None):
        """
        Sets the scaling factor of a game object. You can modify the attenuation computations on this game object
        to simulate sounds with a larger or smaller affected areas. See `AK::SoundEngine::SetScalingFactor`.
        """

    @classmethod
    @_waapimethod
    def set_state(cls, *, client: WaapiClient = None):
        """
        Sets the State of a State Group. See `AK::SoundEngine::SetState`.
        """

    @classmethod
    @_waapimethod
    def set_switch(cls, *, client: WaapiClient = None):
        """
        Sets the State of a Switch Group. See `AK::SoundEngine::SetSwitch`.
        """

    @classmethod
    @_waapimethod
    def stop_all(cls, *, client: WaapiClient = None):
        """
        Stop playing the current content associated to the specified game object ID. If no game object is
        specified, all sounds are stopped. See `AK::SoundEngine::StopAll`.
        """

    @classmethod
    @_waapimethod
    def stop_playing_id(cls, *, client: WaapiClient = None):
        """
        Stops the current content, associated to the specified playing ID, from playing. See
        `AK::SoundEngine::StopPlayingID`.
        """

    @classmethod
    @_waapimethod
    def unload_bank(cls, *, client: WaapiClient = None):
        """
        Unload a SoundBank. See `AK::SoundEngine::UnloadBank`.
        """

    @classmethod
    @_waapimethod
    def unregister_game_obj(cls, *, client: WaapiClient = None):
        """
        Unregisters a game object. Registering a game object twice does nothing. Unregistering it once
        unregisters it no matter how many times it has been registered. Unregistering a game object while it is
        in use is allowed, but the control over the parameters of this game object is lost. For example,
        say a sound associated with this game object is a 3D moving sound. It stops moving when the game object
        is unregistered, and there is no way to regain control over the game object. See
        `AK::SoundEngine::UnregisterGameObj`.
        """


class Wwise:
    """ak.wwise"""

    class Console:
        """ak.wwise.console"""

        class Project:
            """ak.wwise.console.project"""

            @classmethod
            @_waapimethod
            def close(cls, *, client: WaapiClient = None):
                """
                Closes the current project. This operation is synchronous.
                """

            @classmethod
            @_waapimethod
            def create(cls, *, client: WaapiClient = None):
                """
                Creates, saves and opens new empty project, specified by path and platform. The project has no
                factory setting WorkUnit. This operation is synchronous.
                """

            @classmethod
            @_waapimethod
            def open(cls, *, client: WaapiClient = None):
                """
                Opens a project, specified by path. This operation is synchronous.
                """

    class Core:
        """ak.wwise.core"""

        class Audio:
            """ak.wwise.core.audio"""

            @classmethod
            @_waapimethod
            def import_files(cls, *, client: WaapiClient = None):
                """
                Creates Wwise objects and imports audio files. This function does not return an error when
                something fails during the import process, please refer to the log for the result of each import
                command. This function uses the same importation processor available through the Tab Delimited
                import in the Audio File Importer. The function returns an array of all objects created,
                replaced or re-used. Use the options to specify how the objects are returned. For more
                information, refer to Importing Audio Files and Creating Structures.
                """
                # "import" is a reserved keyword, so function name does not match WAAPI

            @classmethod
            @_waapimethod
            def import_tab_delimited(cls, *, client: WaapiClient = None):
                """
                Scripted object creation and audio file import from a tab-delimited file.
                """

            @classmethod
            @_waapimethod
            def mute(cls, *, client: WaapiClient = None):
                """
                Mutes an object.
                """

            @classmethod
            @_waapimethod
            def reset_mute(cls, *, client: WaapiClient = None):
                """
                Unmute all muted objects.
                """

            @classmethod
            @_waapimethod
            def reset_solo(cls, *, client: WaapiClient = None):
                """
                Unsolo all soloed objects.
                """

            @classmethod
            @_waapimethod
            def solo(cls, *, client: WaapiClient = None):
                """
                Solos an object.
                """

        class AudioSourcePeaks:
            """ak.wwise.core.audioSourcePeaks"""

            @classmethod
            @_waapimethod
            def get_min_max_peaks_in_region(cls, *, client: WaapiClient = None):
                """
                Gets the min/max peak pairs, in the given region of an audio source, as a collection of binary
                strings (one per channel). The strings are base-64 encoded, 16-bit signed int arrays,
                with min and max values being interleaved. If getCrossChannelPeaks is true, only one binary
                string represents the peaks across all channels globally.
                """

            @classmethod
            @_waapimethod
            def get_min_max_peaks_in_trimmed_region(cls, *, client: WaapiClient = None):
                """
                Gets the min/max peak pairs in the entire trimmed region of an audio source, for each channel,
                as an array of binary strings (one per channel). The strings are base-64 encoded, 16-bit signed
                int arrays, with min and max values being interleaved. If getCrossChannelPeaks is true,
                there is only one binary string representing peaks across all channels globally.
                """

        @classmethod
        @_waapimethod
        def execute_lua_script(cls, *, client: WaapiClient = None):
            """
            Execute a Lua script. Optionally, specify additional Lua search paths, additional modules,
            and additional Lua scripts to load prior to the main script. The script can return a value. All
            arguments will be passed to the Lua script in the "wa_args" global variable.
            """

        @classmethod
        @_waapimethod
        def get_info(cls, *, client: WaapiClient = None):
            """
            Retrieve global Wwise information.
            """

        @classmethod
        @_waapimethod
        def get_project_info(cls, *, client: WaapiClient = None):
            """
            https://www.audiokinetic.com/en/library/edge/?source=SDK&id=ak_wwise_core_getprojectinfo.html
            \nRetrieve information about the current project opened, including platforms, languages and project
            directories.
            """
            return client.call("ak.wwise.core.getProjectInfo")

        class Log:
            """ak.wwise.core.log"""

            @classmethod
            @_waapimethod
            def add_tem(cls, *, client: WaapiClient = None):
                """
                Adds a new item to the logs on the specified channel.
                """

            @classmethod
            @_waapimethod
            def clear(cls, *, client: WaapiClient = None):
                """
                Clears the logs on the specified channel.
                """

            @classmethod
            @_waapimethod
            def get(cls, *, client: WaapiClient = None):
                """
                Retrieves the latest log for a specific channel. Refer to `ak.wwise.core.log.item_added` to be
                notified when an item is added to the log. The log is empty when used in WwiseConsole.
                """

        class Object:
            """ak.wwise.core.object"""

            @classmethod
            @_waapimethod
            def copy(cls, *, client: WaapiClient = None):
                """
                Copies an object to the given parent. Note that if a Work Unit is copied, the operation cannot be
                undone and the project will be saved.
                """

            @classmethod
            @_waapimethod
            def create(cls, *, client: WaapiClient = None):
                """
                Creates an object of type 'type', as a child of 'parent'. Refer to Importing Audio Files and
                Creating Structures for more information about creating objects. Also refer to
                `ak.wwise.core.audio.import_files` to import audio files to Wwise. To create Effect or Source
                plug-ins, use `ak.wwise.core.object.set`, and refer to Wwise Objects Reference for the classId.
                """

            @classmethod
            @_waapimethod
            def delete(cls, *, client: WaapiClient = None):
                """
                Deletes the specified object. Note that if a Work Unit is deleted, the operation cannot be undone
                and the project will be saved.
                """

            @classmethod
            @_waapimethod
            def diff(cls, *, client: WaapiClient = None):
                """
                Compares properties and lists of the source object with those in the target object.
                """

            @classmethod
            @_waapimethod
            def get(cls, *, client: WaapiClient = None):
                """
                Performs a query and returns the data, as specified in the options, for each object in the query
                result. The query can specify either a 'waql' argument or a 'from' argument with an optional
                'transform' argument. Refer to Using the Wwise Authoring Query Language (WAQL) or Querying the
                Wwise Project for more information. Refer to Return Options to learn about options.
                """

            @classmethod
            @_waapimethod
            def get_attenuation_curve(cls, *, client: WaapiClient = None):
                """
                Gets the specified attenuation curve for a given attenuation object.
                """

            @classmethod
            @_waapimethod
            def get_property_and_reference_names(cls, *, client: WaapiClient = None):
                """
                Retrieves the list of property and reference names for an object.
                """

            @classmethod
            @_waapimethod
            def get_property_info(cls, *, client: WaapiClient = None):
                """
                Retrieves information about an object property. Note that this function does not return the value
                of a property. To retrieve the value of a property, refer to `ak.wwise.core.object.get` and Return
                Options.
                """

            @classmethod
            @_waapimethod
            def get_types(cls, *, client: WaapiClient = None):
                """
                Retrieves the list of all object types registered in Wwise's object model. This function returns
                the equivalent of Wwise Objects Reference.
                """

            @classmethod
            @_waapimethod
            def is_linked(cls, *, client: WaapiClient = None):
                """
                Indicates whether a property, reference, or object list is bound to a particular platform or to
                all platforms.
                """

            @classmethod
            @_waapimethod
            def is_property_enabled(cls, *, client: WaapiClient = None):
                """
                Returns true if a property is enabled based on the values of the properties it depends on.
                """

            @classmethod
            @_waapimethod
            def move(cls, *, client: WaapiClient = None):
                """
                Moves an object to the given parent. Returns the moved object.
                """

            @classmethod
            @_waapimethod
            def paste_properties(cls, *, client: WaapiClient = None):
                """
                Pastes properties, references and lists from one object to any number of target objects. Only
                those properties, references and lists which differ between source and target are pasted. Refer
                to Wwise Objects Reference for more information on the properties, references and lists available
                on each object type.
                """

            @classmethod
            @_waapimethod
            def set(cls, *, client: WaapiClient = None):
                """
                Allows for batch processing of the following operations: Object creation in a child hierarchy,
                Object creation in a list, Setting name, notes, properties and references. Refer to Importing
                Audio Files and Creating Structures for more information about creating objects. Also refer to
                `ak.wwise.core.audio.import_files` to import audio files to Wwise.
                """

            @classmethod
            @_waapimethod
            def set_attenuation_curve(cls, *, client: WaapiClient = None):
                """
                Sets the specified attenuation curve for a given attenuation object.
                """

            @classmethod
            @_waapimethod
            def set_linked(cls, *, client: WaapiClient = None):
                """
                Link or unlink a property/reference or object list to a particular platform.
                """

            @classmethod
            @_waapimethod
            def set_name(cls, *, client: WaapiClient = None):
                """
                Renames an object.
                """

            @classmethod
            @_waapimethod
            def set_notes(cls, *, client: WaapiClient = None):
                """
                Sets the object's notes.
                """

            @classmethod
            @_waapimethod
            def set_property(cls, *, client: WaapiClient = None):
                """
                Sets a property value of an object for a specific platform. Refer to Wwise Objects Reference for
                more information on the properties available on each object type. Refer to
                `ak.wwise.core.object.set_reference` to set a reference to an object. Refer to
                `ak.wwise.core.object.get` to obtain the value of a property for an object.
                """

            @classmethod
            @_waapimethod
            def set_randomizer(cls, *, client: WaapiClient = None):
                """
                Sets the randomizer values of a property of an object for a specific platform. Refer to Wwise
                Objects Reference for more information on the properties available on each object type.
                """

            @classmethod
            @_waapimethod
            def set_reference(cls, *, client: WaapiClient = None):
                """
                Sets an object's reference value. Refer to Wwise Objects Reference for more information on the
                references available on each object type.
                """

            @classmethod
            @_waapimethod
            def set_state_groups(cls, *, client: WaapiClient = None):
                """
                Sets the State Group objects associated with an object. Note, this will remove any previously
                associated State Group.
                """

            @classmethod
            @_waapimethod
            def set_state_properties(cls, *, client: WaapiClient = None):
                """
                Set the state properties of an object. Note, this will remove any previous state property,
                including the default ones.
                """

        class Profiler:
            """ak.wwise.core.profiler"""

            @classmethod
            @_waapimethod
            def enable_profiler_data(cls, *, client: WaapiClient = None):
                """
                Specifies the type of data you want to capture. Overrides the user's profiler settings.
                """

            @classmethod
            @_waapimethod
            def get_audio_objects(cls, *, client: WaapiClient = None):
                """
                Retrieves the Audio Objects at a specific profiler capture time.
                """

            @classmethod
            @_waapimethod
            def get_busses(cls, *, client: WaapiClient = None):
                """
                Retrieves the busses at a specific profiler capture time.
                """

            @classmethod
            @_waapimethod
            def get_cpu_usage(cls, *, client: WaapiClient = None):
                """
                Retrieves CPU usage statistics at a specific profiler capture time. This data can also be found
                in the Advanced Profiler, under the CPU tab. To ensure the CPU data is received,
                refer to `ak.wwise.core.profiler.enable_profiler_data`. The returned data includes "Inclusive" and
                "Exclusive" values, where "Inclusive" refers to the time spent in the element plus the time spent
                in any called elements, and "Exclusive" values pertain to execution only within the element
                itself.
                """

            @classmethod
            @_waapimethod
            def get_cursor_time(cls, *, client: WaapiClient = None):
                """
                Returns the current time of the specified profiler cursor, in milliseconds.
                """

            @classmethod
            @_waapimethod
            def get_game_objects(cls, *, client: WaapiClient = None):
                """
                Retrieves the game objects at a specific profiler capture time.
                """

            @classmethod
            @_waapimethod
            def get_loaded_media(cls, *, client: WaapiClient = None):
                """
                Retrieves the loaded media at a specific profiler capture time. This data can also be found in
                the Advanced Profiler, under the Loaded Media tab. To ensure the Loaded Media data is received,
                refer to `ak.wwise.core.profiler.enable_profiler_data`.
                """

            @classmethod
            @_waapimethod
            def get_performance_monitor(cls, *, client: WaapiClient = None):
                """
                Retrieves the Performance Monitor statistics at a specific profiler capture time. Refer to Wwise
                Authoring Performance Monitor Counter Identifiers for the available counters.
                """

            @classmethod
            @_waapimethod
            def get_rtpcs(cls, *, client: WaapiClient = None):
                """
                Retrieves active RTPCs at a specific profiler capture time.
                """

            @classmethod
            @_waapimethod
            def get_streamed_media(cls, *, client: WaapiClient = None):
                """
                Retrieves the streaming media at a specific profiler capture time. This data can also be found in
                the Advanced Profiler, under the Streams tab. To ensure the Streams data is received,
                refer to `ak.wwise.core.profiler.enable_profiler_data`.
                """

            @classmethod
            @_waapimethod
            def get_voice_contributions(cls, *, client: WaapiClient = None):
                """
                Retrieves all parameters affecting voice volume, highpass and lowpass for a voice path,
                resolved from pipeline IDs.
                """

            @classmethod
            @_waapimethod
            def get_voices(cls, *, client: WaapiClient = None):
                """
                Retrieves the voices at a specific profiler capture time.
                """

            @classmethod
            @_waapimethod
            def save_capture(cls, *, client: WaapiClient = None):
                """
                Saves profiler as a .prof file according to the given file path.
                """

            @classmethod
            @_waapimethod
            def start_capture(cls, *, client: WaapiClient = None):
                """
                Starts the profiler capture and returns the time at the beginning of the capture, in milliseconds.
                """

            @classmethod
            @_waapimethod
            def stop_capture(cls, *, client: WaapiClient = None):
                """
                Stops the profiler capture and returns the time at the end of the capture, in milliseconds.
                """

        class Project:
            """ak.wwise.core.project"""

            @classmethod
            @_waapimethod
            def save(cls, *, client: WaapiClient = None):
                """
                Saves the current project.
                """

        class Remote:
            """ak.wwise.core.remote"""

            @classmethod
            @_waapimethod
            def connect(cls, *, client: WaapiClient = None):
                """
                Connects the Wwise Authoring application to a Wwise Sound Engine running executable or to a saved
                profile file. The host must be running code with communication enabled. If only "host" is
                provided, Wwise connects to the first Sound Engine instance found. To distinguish between
                different instances, you can also provide the name of the application to connect to.
                """

            @classmethod
            @_waapimethod
            def disconnect(cls, *, client: WaapiClient = None):
                """
                Disconnects the Wwise Authoring application from a connected Wwise Sound Engine running executable.
                """

            @classmethod
            @_waapimethod
            def get_available_consoles(cls, *, client: WaapiClient = None):
                """
                Retrieves all consoles available for connecting Wwise Authoring to a Sound Engine instance.
                """

            @classmethod
            @_waapimethod
            def get_connection_status(cls, *, client: WaapiClient = None):
                """
                Retrieves the connection status.
                """

        class Sound:
            """ak.wwise.core.sound"""

            @classmethod
            @_waapimethod
            def get_active_source(cls, *, client: WaapiClient = None):
                """
                Sets which version of the source is being used for the specified sound. Use
                `ak.wwise.core.object.get` with the 'activeSource' return option to get the active source of a
                sound.
                """

        class SoundBank:
            """ak.wwise.core.soundbank"""

            @classmethod
            @_waapimethod
            def convert_external_sources(cls, *, client: WaapiClient = None):
                """
                Converts the external sources files for the project as detailed in the wsources file, and places
                them into either the default folder, or the folder specified by the output argument. External
                Sources are a special type of source that you can put in a Sound object in Wwise. It indicates
                that the real sound data will be provided at run time. While External Source conversion is also
                triggered by SoundBank generation, this operation can be used to process sources not contained in
                the Wwise Project. Please refer to Wwise SDK help page "Integrating External Sources".
                """

            @classmethod
            @_waapimethod
            def generate(cls, *, client: WaapiClient = None):
                """
                Generate a list of SoundBanks with the import definition specified in the WAAPI request. If you
                do not write the SoundBanks to disk, subscribe to `ak.wwise.core.soundbank.generated` to receive
                SoundBank structure info and the bank data as base64. Note: This is a synchronous operation.
                """

            @classmethod
            @_waapimethod
            def get_inclusions(cls, *, client: WaapiClient = None):
                """
                Retrieves a SoundBank's inclusion list.
                """

            @classmethod
            @_waapimethod
            def process_definition_files(cls, *, client: WaapiClient = None):
                """
                Imports SoundBank definitions from the specified file. Multiple files can be specified. See the
                WAAPI log for status messages.
                """

            @classmethod
            @_waapimethod
            def set_inclusions(cls, *, client: WaapiClient = None):
                """
                Modifies a SoundBank's inclusion list. The 'operation' argument determines how the 'inclusions'
                argument modifies the SoundBank's inclusion list; 'inclusions' may be added to / removed from /
                replace the SoundBank's inclusion list.
                """

        class SourceControl:
            """ak.wwise.core.sourceControl"""

            @classmethod
            @_waapimethod
            def add(cls, *, client: WaapiClient = None):
                """
                Add files to source control. Equivalent to Mark for Add for Perforce.
                """

            @classmethod
            @_waapimethod
            def check_out(cls, *, client: WaapiClient = None):
                """
                Check out files from source control. Equivalent to Check Out for Perforce.
                """

            @classmethod
            @_waapimethod
            def commit(cls, *, client: WaapiClient = None):
                """
                Commit files to source control. Equivalent to Submit Changes for Perforce.
                """

            @classmethod
            @_waapimethod
            def delete(cls, *, client: WaapiClient = None):
                """
                Delete files from source control. Equivalent to Mark for Delete for Perforce.
                """

            @classmethod
            @_waapimethod
            def get_source_files(cls, *, client: WaapiClient = None):
                """
                Retrieve all original files.
                """

            @classmethod
            @_waapimethod
            def get_status(cls, *, client: WaapiClient = None):
                """
                Get the source control status of the specified files.
                """

            @classmethod
            @_waapimethod
            def move(cls, *, client: WaapiClient = None):
                """
                Move or rename files in source control. Always pass the same number of elements in files and
                newFiles. Equivalent to Move for Perforce.
                """

            @classmethod
            @_waapimethod
            def revert(cls, *, client: WaapiClient = None):
                """
                Revert changes to files in source control.
                """

            @classmethod
            @_waapimethod
            def set_provider(cls, *, client: WaapiClient = None):
                """
                Change the source control provider and credentials. This is the same setting as the Source
                Control option in the Project Settings dialog in Wwise.
                """

        class SwitchContainer:
            """ak.wwise.core.switchContainer"""

            @classmethod
            @_waapimethod
            def add_assignment(cls, *, client: WaapiClient = None):
                """
                Assigns a Switch Container's child to a Switch. This is the equivalent of doing a drag&drop of
                the child to a state in the Assigned Objects view. The child is always added at the end for each
                state.
                """

            @classmethod
            @_waapimethod
            def get_assignments(cls, *, client: WaapiClient = None):
                """
                Returns the list of assignments between a Switch Container's children and states.
                """

            @classmethod
            @_waapimethod
            def remove_assignment(cls, *, client: WaapiClient = None):
                """
                Removes an assignment between a Switch Container's child and a State.
                """

        class Transport:
            """ak.wwise.core.transport"""

            @classmethod
            @_waapimethod
            def create(cls, *, client: WaapiClient = None):
                """
                Creates a transport object for the given Wwise object. The return transport object can be used to
                play, stop, pause and resume the Wwise object via the other transport functions.
                """

            @classmethod
            @_waapimethod
            def destroy(cls, *, client: WaapiClient = None):
                """
                Destroys the given transport object.
                """

            @classmethod
            @_waapimethod
            def execute_action(cls, *, client: WaapiClient = None):
                """
                Executes an action on the given transport object, or all transport objects if none is specified.
                """

            @classmethod
            @_waapimethod
            def get_list(cls, *, client: WaapiClient = None):
                """
                Returns the list of transport objects.
                """

            @classmethod
            @_waapimethod
            def get_state(cls, *, client: WaapiClient = None):
                """
                Gets the state of the given transport object.
                """

            @classmethod
            @_waapimethod
            def prepare(cls, *, client: WaapiClient = None):
                """
                Prepare the object and its dependencies for playback. Use this function before calling
                `PostEventSync` or `PostMIDIOnEventSync` from `IAkGlobalPluginContext`.
                """

            @classmethod
            @_waapimethod
            def use_originals(cls, *, client: WaapiClient = None):
                """
                Sets the Original/Converted transport toggle globally. This allows playing the original or the
                converted sound files.
                """

        class Undo:
            """ak.wwise.core.undo"""

            @classmethod
            @_waapimethod
            def begin_group(cls, *, client: WaapiClient = None):
                """
                Begins an undo group. Make sure to call ak.wwise.core.undo.endGroup exactly once for every
                ak.wwise.core.beginUndoGroup call you make. Calls to `ak.wwise.core.undo.begin_group` can be nested.
                When closing a WAMP session, a check is made to ensure that all undo groups are closed. If not,
                a cancelGroup is called for each of the groups still open.
                """

            @classmethod
            @_waapimethod
            def cancel_group(cls, *, client: WaapiClient = None):
                """
                Cancels the last undo group.
                """

            @classmethod
            @_waapimethod
            def end_group(cls, *, client: WaapiClient = None):
                """
                Ends the last undo group.
                """

            @classmethod
            @_waapimethod
            def redo(cls, *, client: WaapiClient = None):
                """
                Redoes the last operation in the Undo stack.
                """

            @classmethod
            @_waapimethod
            def undo(cls, *, client: WaapiClient = None):
                """
                Undoes the last operation in the Undo stack.
                """

    class Debug:
        """ak.wwise.debug"""

        @classmethod
        @_waapimethod
        def enable_asserts(cls, *, client: WaapiClient = None):
            """
            Enables debug assertions. Every call to enableAsserts with 'false' increments the ref count. Calling
            with true decrements the ref count. This is only available with Debug builds.
            """

        @classmethod
        @_waapimethod
        def enable_automation_mode(cls, *, client: WaapiClient = None):
            """
            Enables or disables the automation mode for Wwise. This reduces the potential interruptions caused by
            message boxes and dialogs. For instance, enabling the automation mode silently accepts: project
            migration, project load log, EULA acceptance, project licence display and generic message boxes.
            """

        @classmethod
        @_waapimethod
        def generate_tone_wav(cls, *, client: WaapiClient = None):
            """
            Generate a WAV file playing a tone with a simple envelope and save it to the specified location. This
            is provided as a utility to generate test WAV files.
            """

        @classmethod
        @_waapimethod
        def get_wal_tree(cls, *, client: WaapiClient = None):
            """
            Retrieves the WAL tree, which describes the nodes that are synchronized in the Sound Engine. Private
            use only.
            """

        @classmethod
        @_waapimethod
        def restart_waapi_servers(cls, *, client: WaapiClient = None):
            """
            Restart WAAPI servers. For internal use only.
            """

        @classmethod
        @_waapimethod
        def test_assert(cls, *, client: WaapiClient = None):
            """
            Private use only.
            """

        @classmethod
        @_waapimethod
        def test_crash(cls, *, client: WaapiClient = None):
            """
            Private use only.
            """

    class UI:
        """ak.wwise.ui"""

        @classmethod
        @_waapimethod
        def bring_to_foreground(cls, *, client: WaapiClient = None):
            """
            Bring Wwise main window to foreground. Refer to `SetForegroundWindow` and `AllowSetForegroundWindow`
            on MSDN for more information on the restrictions. Refer to `ak.wwise.core.get_info` to obtain the
            Wwise process ID for `AllowSetForegroundWindow`.
            """

        @classmethod
        @_waapimethod
        def capture_screen(cls, *, client: WaapiClient = None):
            """
            Captures a part of the Wwise UI relative to a view.
            """

        class Commands:
            """ak.wwise.ui.commands"""

            @classmethod
            @_waapimethod
            def execute(cls, *, client: WaapiClient = None):
                """
                Executes a command. Some commands can take a list of objects as parameters. Refer to Wwise
                Authoring Command Identifiers for the available commands.
                """

            @classmethod
            @_waapimethod
            def get_commands(cls, *, client: WaapiClient = None):
                """
                Gets the list of commands.
                """

            @classmethod
            @_waapimethod
            def register(cls, *, client: WaapiClient = None):
                """
                Registers an array of add-on commands. Registered commands remain until the Wwise process is
                terminated. Refer to Defining Command Add-ons for more information about registering commands.
                Also refer to `ak.wwise.ui.commands.executed`.
                """

            @classmethod
            @_waapimethod
            def unregister(cls, *, client: WaapiClient = None):
                """
                Unregisters an array of add-on UI commands.
                """

        @classmethod
        @_waapimethod
        def get_selected_objects(cls, *, client: WaapiClient = None):
            """
            Retrieves the list of objects currently selected by the user in the active view.
            """

        class Project:
            """ak.wwise.ui.project"""

            @classmethod
            @_waapimethod
            def close(cls, *, client: WaapiClient = None):
                """
                Closes the current project.
                """

            @classmethod
            @_waapimethod
            def create(cls, *, client: WaapiClient = None):
                """
                Creates, saves and opens new empty project, specified by path and platform. The project has no
                factory setting WorkUnit. Please refer to `ak.wwise.core.project.loaded` for further explanations
                on how to be notified when the operation has completed.
                """

            @classmethod
            @_waapimethod
            def open(cls, *, client: WaapiClient = None):
                """
                Opens a project, specified by path. Please refer to `ak.wwise.core.project.loaded` for further
                explanations on how to be notified when the operation has completed.
                """

        class Waapi:
            """ak.wwise.ui.waapi"""

            @classmethod
            @_waapimethod
            def get_functions(cls, *, client: WaapiClient = None):
                """
                Retrieves the list of functions.
                """

            @classmethod
            @_waapimethod
            def get_schema(cls, *, client: WaapiClient = None):
                """
                Retrieves the JSON schema of a Waapi URI.
                """

            @classmethod
            @_waapimethod
            def get_topics(cls, *, client: WaapiClient = None):
                """
                Retrieves the list of topics to which a client can subscribe.
                """
