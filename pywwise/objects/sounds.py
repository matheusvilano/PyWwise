# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from collections.abc import Sequence as _Sequence

from pywwise.descriptors import WwiseProperty
from pywwise.enums import (E3DPosition, E3DSpatialization, EDiscardBehaviour, ELoudnessNormalizationType,
                           EMidiPlayOnNoteType, EOverLimitBehaviour, EScope, EVirtualVoiceBehaviour,
                           EVirtualVoiceQueueBehaviour)
from pywwise.objects.buses import AuxBus, Bus
from pywwise.objects.effects import EffectSlot
from pywwise.objects.types import Attenuation, Conversion, WwiseObject
from pywwise.primitives import GUID


class AudioSource(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.AUDIO_SOURCE`."""


class ExternalSource(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.EXTERNAL_SOURCE`."""


class ExternalSourceFile(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.EXTERNAL_SOURCE_FILE`."""


class Marker(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MARKER`."""


class PluginDataSource(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.PLUGIN_DATA_SOURCE`."""


class Sound(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_sound.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SOUND`.
    """
    position_3d = WwiseProperty("3DPosition", E3DPosition)
    spatialization_3d = WwiseProperty("3DSpatialization", E3DSpatialization)
    attenuation = WwiseProperty("Attenuation", Attenuation)
    attenuation_distance_scaling = WwiseProperty("AttenuationDistanceScaling", float)
    below_threshold_behaviour = WwiseProperty("BelowThresholdBehavior", EVirtualVoiceBehaviour)
    bypass_effect = WwiseProperty("BypassEffect", bool)
    centre_percentage = WwiseProperty("CenterPercentage", float)
    colour = WwiseProperty("Color", int)
    converion = WwiseProperty("Conversion", Conversion)
    effects = WwiseProperty("Effects", _Sequence[EffectSlot])
    enable_attenuation = WwiseProperty("EnableAttenuation", bool)
    enable_diffraction = WwiseProperty("EnableDiffraction", bool)
    enable_loudness_normalization = WwiseProperty("EnableLoudnessNormalization", bool)
    enable_midi_note_tracking = WwiseProperty("EnableMidiNoteTracking", bool)
    game_aux_send_hpf = WwiseProperty("GameAuxSendHPF", int)
    game_aux_send_lpf = WwiseProperty("GameAuxSendLPF", int)
    game_aux_send_volume = WwiseProperty("GameAuxSendVolume", float)
    hdr_active_range = WwiseProperty("HdrActiveRange", float)
    hdr_enable_envelope = WwiseProperty("HdrEnableEnvelope", bool)
    hdr_envelope_sensitivity = WwiseProperty("HdrEnvelopeSensitivity", float)
    highpass = WwiseProperty("Highpass", int)
    hold_emitter_position_orientation = WwiseProperty("HoldEmitterPositionOrientation", bool)
    hold_listener_orientation = WwiseProperty("HoldListenerOrientation", bool)
    ignore_parent_max_sound_instance = WwiseProperty("IgnoreParentMaxSoundInstance", bool)
    inclusion = WwiseProperty("Inclusion", bool)
    initial_delay = WwiseProperty("InitialDelay", float)
    is_global_limit = WwiseProperty("IsGlobalLimit", EScope)
    is_looping_enabled = WwiseProperty("IsLoopingEnabled", bool)
    is_looping_infinite = WwiseProperty("IsLoopingInfinite", bool)
    is_non_cachable = WwiseProperty("IsNonCachable", bool)
    is_streaming_enabled = WwiseProperty("IsStreamingEnabled", bool)
    is_voice = WwiseProperty("IsVoice", bool)
    is_zero_latency = WwiseProperty("IsZeroLatency", bool)
    listener_relative_routing = WwiseProperty("ListenerRelativeRouting", bool)
    loop_count = WwiseProperty("LoopCount", int)
    loudness_normalization_target = WwiseProperty("LoudnessNormalizationTarget", float)
    loudness_normalization_type = WwiseProperty("LoudnessNormalizationType", ELoudnessNormalizationType)
    lowpass = WwiseProperty("Lowpass", int)
    make_up_gain = WwiseProperty("MakeUpGain", float)
    max_reached_behaviour = WwiseProperty("MaxReachedBehavior", EDiscardBehaviour)
    max_sound_per_instance = WwiseProperty("MaxSoundPerInstance", int)
    metadata = WwiseProperty("Metadata", GUID)
    midi_break_on_note_off = WwiseProperty("MidiBreakOnNoteOff", bool)
    midi_channel_filter = WwiseProperty("MidiChannelFilter", int)
    midi_key_filter_max = WwiseProperty("MidiKeyFilterMax", int)
    midi_key_filter_min = WwiseProperty("MidiKeyFilterMin", int)
    midi_play_on_note_type = WwiseProperty("MidiPlayOnNoteType", EMidiPlayOnNoteType)
    midi_tracking_root_note = WwiseProperty("MidiTrackingRootNote", int)
    midi_transposition = WwiseProperty("MidiTransposition", int)
    midi_velocity_filter_max = WwiseProperty("MidiVelocityFilterMax", int)
    midi_velocity_filter_min = WwiseProperty("MidiVelocityFilterMin", int)
    midi_velocity_offset = WwiseProperty("MidiVelocityOffset", int)
    output_bus = WwiseProperty("OutputBus", Bus)
    output_bus_highpass = WwiseProperty("OutputBusHighpass", int)
    output_bus_lowpass = WwiseProperty("OutputBusLowpass", int)
    output_bus_volume = WwiseProperty("OutputBusVolume", float)
    over_limit_behaviour = WwiseProperty("OverLimitBehavior", EOverLimitBehaviour)
    override_analysis = WwiseProperty("OverrideAnalysis", bool)
    override_colour = WwiseProperty("OverrideColor", bool)
    override_conversion = WwiseProperty("OverrideConversion", bool)
    override_early_reflections = WwiseProperty("OverrideEarlyReflections", bool)
    override_effect = WwiseProperty("OverrideEffect", bool)
    override_game_aux_sends = WwiseProperty("OverrideGameAuxSends", bool)
    override_hdr_envelope = WwiseProperty("OverrideHdrEnvelope", bool)
    override_metadata = WwiseProperty("OverrideMetadata", bool)
    override_midi_events_behaviour = WwiseProperty("OverrideMidiEventsBehavior", bool)
    override_midi_note_tracking = WwiseProperty("OverrideMidiNoteTracking", bool)
    override_output = WwiseProperty("OverrideOutput", bool)
    override_positioning = WwiseProperty("OverridePositioning", bool)
    override_priority = WwiseProperty("OverridePriority", bool)
    override_user_aux_sends = WwiseProperty("OverrideUserAuxSends", bool)
    override_virtual_voice = WwiseProperty("OverrideVirtualVoice", bool)
    pitch = WwiseProperty("Pitch", int)
    pre_fetch_length = WwiseProperty("PreFetchLength", int)
    priority = WwiseProperty("Priority", int)
    priority_distance_factor = WwiseProperty("PriorityDistanceFactor", bool)
    priority_distance_offset = WwiseProperty("PriorityDistanceOffset", int)
    rtpc = WwiseProperty("RTPC", _Sequence[Rtpc])
    reflections_aux_send = WwiseProperty("ReflectionsAuxSend", AuxBus)
    reflections_volume = WwiseProperty("ReflectionsVolume", float)
    speaker_panning = WwiseProperty("SpeakerPanning", int)
    speaker_panning_3d_spatialization_mid = WwiseProperty("SpeakerPanning3DSpatializationMix", int)
    use_game_aux_sends = WwiseProperty("UseGameAuxSends", bool)
    use_max_sound_per_instance = WwiseProperty("UseMaxSoundPerInstance", bool)
    user_aux_send_0 = WwiseProperty("UserAuxSend0", AuxBus)
    user_aux_send_1 = WwiseProperty("UserAuxSend1", AuxBus)
    user_aux_send_2 = WwiseProperty("UserAuxSend2", AuxBus)
    user_aux_send_3 = WwiseProperty("UserAuxSend3", AuxBus)
    user_aux_send_hpf_0 = WwiseProperty("UserAuxSendHPF0", int)
    user_aux_send_hpf_1 = WwiseProperty("UserAuxSendHPF1", int)
    user_aux_send_hpf_2 = WwiseProperty("UserAuxSendHPF2", int)
    user_aux_send_hpf_3 = WwiseProperty("UserAuxSendHPF3", int)
    user_aux_send_lpf_0 = WwiseProperty("UserAuxSendLPF0", int)
    user_aux_send_lpf_1 = WwiseProperty("UserAuxSendLPF1", int)
    user_aux_send_lpf_2 = WwiseProperty("UserAuxSendLPF2", int)
    user_aux_send_lpf_3 = WwiseProperty("UserAuxSendLPF3", int)
    user_aux_send_volume_0 = WwiseProperty("UserAuxSendVolume0", float)
    user_aux_send_volume_1 = WwiseProperty("UserAuxSendVolume1", float)
    user_aux_send_volume_2 = WwiseProperty("UserAuxSendVolume2", float)
    user_aux_send_volume_3 = WwiseProperty("UserAuxSendVolume3", float)
    virtual_voice_queue_behaviour = WwiseProperty("VirtualVoiceQueueBehavior", EVirtualVoiceQueueBehaviour)


class SourcePlugin(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SOURCE_PLUGIN`."""
