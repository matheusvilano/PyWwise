# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import TYPE_CHECKING, Union as _Union

if TYPE_CHECKING:
    from pywwise.objects.types.music_transition import MusicTransition

from pywwise.descriptors import WwiseProperty
from pywwise.enums import (E3DPosition, E3DSpatialization, EColour, EDiscardBehaviour, ELoudnessNormalizationType,
                           EMidiTempoSource, EMusicTrackType, EOverLimitBehaviour, EScope, ESpeakerPanning,
                           ESwitchOrState, ESyncGroupType, EVirtualVoiceBehaviour, EVirtualVoiceQueueBehaviour)
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.attenuation import Attenuation
from pywwise.objects.types.aux_bus import AuxBus
from pywwise.objects.types.blend_container import BlendContainer
from pywwise.objects.types.bus import Bus
from pywwise.objects.types.conversion import Conversion
from pywwise.objects.types.effect_slot import EffectSlot
from pywwise.objects.types.music_track_sequence import MusicTrackSequence
from pywwise.objects.types.random_sequence_container import RandomSequenceContainer
from pywwise.objects.types.rtpc import Rtpc
from pywwise.objects.types.sound import Sound
from pywwise.objects.types.switch_container import SwitchContainer
from pywwise.primitives import GUID

_MidiTargetType = _Union[RandomSequenceContainer, SwitchContainer, BlendContainer, Sound]

_MidiTargetTypeTuple = (RandomSequenceContainer, SwitchContainer, BlendContainer, Sound)


class MusicTrack(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_musictrack.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_TRACK`.
    """
    position_3d = WwiseProperty[E3DPosition]("3DPosition", E3DPosition)
    spatialization_3d = WwiseProperty[E3DSpatialization]("3DSpatialization", E3DSpatialization)
    attenuation = WwiseProperty[Attenuation]("Attenuation", Attenuation)
    attenuation_distance_scaling = WwiseProperty[float]("AttenuationDistanceScaling", float)
    below_threshold_behaviour = WwiseProperty[EVirtualVoiceBehaviour]("BelowThresholdBehavior", EVirtualVoiceBehaviour)
    bypass_effect = WwiseProperty[bool]("BypassEffect", bool)
    centre_percentage = WwiseProperty[float]("CenterPercentage", float)
    colour = WwiseProperty[EColour]("Color", EColour)
    conversion = WwiseProperty[Conversion]("Conversion", Conversion)
    default_switch_or_state = WwiseProperty[ESwitchOrState]("DefaultSwitchOrState", ESwitchOrState)
    effects = WwiseProperty[tuple[EffectSlot, ...]]("Effects", tuple)
    enable_attenuation = WwiseProperty[bool]("EnableAttenuation", bool)
    enable_diffraction = WwiseProperty[bool]("EnableDiffraction", bool)
    enable_loudness_normalization = WwiseProperty[bool]("EnableLoudnessNormalization", bool)
    game_aux_send_hpf = WwiseProperty[int]("GameAuxSendHPF", int)
    game_aux_send_lpf = WwiseProperty[int]("GameAuxSendLPF", int)
    game_aux_send_volume = WwiseProperty[float]("GameAuxSendVolume", float)
    hdr_active_range = WwiseProperty[float]("HdrActiveRange", float)
    hdr_enable_envelope = WwiseProperty[bool]("HdrEnableEnvelope", bool)
    hdr_envelope_sensitivity = WwiseProperty[float]("HdrEnvelopeSensitivity", float)
    highpass = WwiseProperty[int]("Highpass", int)
    hold_emitter_position_orientation = WwiseProperty[bool]("HoldEmitterPositionOrientation", bool)
    hold_listener_orientation = WwiseProperty[bool]("HoldListenerOrientation", bool)
    ignore_parent_max_sound_instance = WwiseProperty[bool]("IgnoreParentMaxSoundInstance", bool)
    inclusion = WwiseProperty[bool]("Inclusion", bool)
    is_global_limit = WwiseProperty[EScope]("IsGlobalLimit", EScope)
    is_non_cachable = WwiseProperty[bool]("IsNonCachable", bool)
    is_streaming_enabled = WwiseProperty[bool]("IsStreamingEnabled", bool)
    is_zero_latency = WwiseProperty[bool]("IsZeroLatency", bool)
    listener_relative_routing = WwiseProperty[bool]("ListenerRelativeRouting", bool)
    look_ahead_time = WwiseProperty[int]("LookAheadTime", int)
    loudness_normalization_target = WwiseProperty[float]("LoudnessNormalizationTarget", float)
    loudness_normalization_type = WwiseProperty[ELoudnessNormalizationType](
        "LoudnessNormalizationType", ELoudnessNormalizationType)
    lowpass = WwiseProperty[int]("Lowpass", int)
    make_up_gain = WwiseProperty[float]("MakeUpGain", float)
    max_reached_behaviour = WwiseProperty[EDiscardBehaviour]("MaxReachedBehavior", EDiscardBehaviour)
    max_sound_per_instance = WwiseProperty[int]("MaxSoundPerInstance", int)
    metadata = WwiseProperty[GUID]("Metadata", GUID)
    midi_target = WwiseProperty[_MidiTargetType]("MidiTarget", _MidiTargetTypeTuple)
    midi_tempo_source = WwiseProperty[EMidiTempoSource]("MidiTempoSource", EMidiTempoSource)
    music_track_type = WwiseProperty[EMusicTrackType]("MusicTrackType", EMusicTrackType)
    output_bus = WwiseProperty[Bus]("OutputBus", Bus)
    output_bus_highpass = WwiseProperty[int]("OutputBusHighpass", int)
    output_bus_lowpass = WwiseProperty[int]("OutputBusLowpass", int)
    output_bus_volume = WwiseProperty[float]("OutputBusVolume", float)
    over_limit_behaviour = WwiseProperty[EOverLimitBehaviour]("OverLimitBehavior", EOverLimitBehaviour)
    override_analysis = WwiseProperty[bool]("OverrideAnalysis", bool)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    override_conversion = WwiseProperty[bool]("OverrideConversion", bool)
    override_early_reflections = WwiseProperty[bool]("OverrideEarlyReflections", bool)
    override_effect = WwiseProperty[bool]("OverrideEffect", bool)
    override_game_aux_sends = WwiseProperty[bool]("OverrideGameAuxSends", bool)
    override_hdr_envelope = WwiseProperty[bool]("OverrideHdrEnvelope", bool)
    override_metadata = WwiseProperty[bool]("OverrideMetadata", bool)
    override_midi_target = WwiseProperty[bool]("OverrideMidiTarget", bool)
    override_midi_tempo = WwiseProperty[bool]("OverrideMidiTempo", bool)
    override_output = WwiseProperty[bool]("OverrideOutput", bool)
    override_positioning = WwiseProperty[bool]("OverridePositioning", bool)
    override_priority = WwiseProperty[bool]("OverridePriority", bool)
    override_user_aux_sends = WwiseProperty[bool]("OverrideUserAuxSends", bool)
    override_virtual_voice = WwiseProperty[bool]("OverrideVirtualVoice", bool)
    pro_fetch_length = WwiseProperty[int]("ProFetchLength", int)
    priority = WwiseProperty[int]("Priority", int)
    priority_distance_factor = WwiseProperty[bool]("PriorityDistanceFactor", bool)
    priority_distance_offset = WwiseProperty[int]("PriorityDistanceOffset", int)
    rtpc = WwiseProperty[tuple[Rtpc, ...]]("RTPC", tuple)
    reflections_aux_send = WwiseProperty[AuxBus]("ReflectionsAuxSend", AuxBus)
    reflections_volume = WwiseProperty[float]("ReflectionsVolume", float)
    sequences = WwiseProperty[tuple[MusicTrackSequence, ...]]("Sequences", tuple)
    speaker_panning = WwiseProperty[ESpeakerPanning]("SpeakerPanning", ESpeakerPanning)
    speaker_panning_3d_spatialization_mix = WwiseProperty[int]("SpeakerPanning3DSpatializationMix", int)
    switch_or_state_group = WwiseProperty[ESyncGroupType]("SwitchOrStateGroup", ESyncGroupType)
    transition_root: WwiseProperty[MusicTransition]  # Injected via __init__
    use_game_aux_sends = WwiseProperty[bool]("UseGameAuxSends", bool)
    use_max_sound_per_instance = WwiseProperty[bool]("UseMaxSoundPerInstance", bool)
    user_aux_send_0 = WwiseProperty[AuxBus]("UserAuxSend0", AuxBus)
    user_aux_send_1 = WwiseProperty[AuxBus]("UserAuxSend1", AuxBus)
    user_aux_send_2 = WwiseProperty[AuxBus]("UserAuxSend2", AuxBus)
    user_aux_send_3 = WwiseProperty[AuxBus]("UserAuxSend3", AuxBus)
    user_aux_send_hpf_0 = WwiseProperty[int]("UserAuxSendHPF0", int)
    user_aux_send_hpf_1 = WwiseProperty[int]("UserAuxSendHPF1", int)
    user_aux_send_hpf_2 = WwiseProperty[int]("UserAuxSendHPF2", int)
    user_aux_send_hpf_3 = WwiseProperty[int]("UserAuxSendHPF3", int)
    user_aux_send_lpf_0 = WwiseProperty[int]("UserAuxSendLPF0", int)
    user_aux_send_lpf_1 = WwiseProperty[int]("UserAuxSendLPF1", int)
    user_aux_send_lpf_2 = WwiseProperty[int]("UserAuxSendLPF2", int)
    user_aux_send_lpf_3 = WwiseProperty[int]("UserAuxSendLPF3", int)
    user_aux_send_volume_0 = WwiseProperty[float]("UserAuxSendVolume0", float)
    user_aux_send_volume_1 = WwiseProperty[float]("UserAuxSendVolume1", float)
    user_aux_send_volume_2 = WwiseProperty[float]("UserAuxSendVolume2", float)
    user_aux_send_volume_3 = WwiseProperty[float]("UserAuxSendVolume3", float)
    virtual_voice_queue_behaviour = WwiseProperty[EVirtualVoiceQueueBehaviour](
        "VirtualVoiceQueueBehavior", EVirtualVoiceQueueBehaviour)
    volume = WwiseProperty[float]("Volume", float)
