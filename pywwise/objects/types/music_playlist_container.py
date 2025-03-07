# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from typing import Union as _Union

from pywwise.descriptors import WwiseProperty
from pywwise.enums import (E3DPosition, E3DSpatialization, EColour, EDiscardBehaviour, ELoudnessNormalizationType,
                           EMidiTempoSource, EMusicalDuration, EMusicalGridFrequency, EOverLimitBehaviour, EScope,
                           ESpeakerPanning, ETimeSignature, EVirtualVoiceBehaviour, EVirtualVoiceQueueBehaviour)
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.attenuation import Attenuation
from pywwise.objects.types.aux_bus import AuxBus
from pywwise.objects.types.blend_container import BlendContainer
from pywwise.objects.types.bus import Bus
from pywwise.objects.types.conversion import Conversion
from pywwise.objects.types.effect_slot import EffectSlot
from pywwise.objects.types.music_playlist_item import MusicPlaylistItem
from pywwise.objects.types.music_stinger import MusicStinger
from pywwise.objects.types.random_sequence_container import RandomSequenceContainer
from pywwise.objects.types.rtpc import Rtpc
from pywwise.objects.types.sound import Sound
from pywwise.objects.types.switch_container import SwitchContainer
from pywwise.primitives import GUID

_MidiTarget = _Union[RandomSequenceContainer, SwitchContainer, BlendContainer, Sound]

_MidiTargetTuple = (RandomSequenceContainer, SwitchContainer, BlendContainer, Sound)


class MusicPlaylistContainer(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_musicplaylistcontainer.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_PLAYLIST_CONTAINER`.
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
    effects = WwiseProperty[tuple[EffectSlot, ...]]("Effects", tuple)
    enable_attenuation = WwiseProperty[bool]("EnableAttenuation", bool)
    enable_diffraction = WwiseProperty[bool]("EnableDiffraction", bool)
    enable_loudness_normalization = WwiseProperty[bool]("EnableLoudnessNormalization", bool)
    game_aux_send_hpf = WwiseProperty[int]("GameAuxSendHPF", int)
    game_aux_send_lpf = WwiseProperty[int]("GameAuxSendLPF", int)
    game_aux_send_volume = WwiseProperty[float]("GameAuxSendVolume", float)
    grid_frequency_preset = WwiseProperty[EMusicalGridFrequency]("GridFrequencyPreset", EMusicalGridFrequency)
    grid_offset_custom = WwiseProperty[float]("GridOffsetCustom", float)
    grid_offset_preset = WwiseProperty[EMusicalDuration]("GridOffsetPreset", EMusicalDuration)
    hdr_active_range = WwiseProperty[float]("HdrActiveRange", float)
    hdr_enable_envelope = WwiseProperty[bool]("HdrEnableEnvelope", bool)
    hdr_envelope_sensitivity = WwiseProperty[float]("HdrEnvelopeSensitivity", float)
    highpass = WwiseProperty[int]("Highpass", int)
    hold_emitter_position_orientation = WwiseProperty[bool]("HoldEmitterPositionOrientation", bool)
    hold_listener_orientation = WwiseProperty[bool]("HoldListenerOrientation", bool)
    ignore_parent_max_sound_instance = WwiseProperty[bool]("IgnoreParentMaxSoundInstance", bool)
    inclusion = WwiseProperty[bool]("Inclusion", bool)
    initial_delay = WwiseProperty[float]("InitialDelay", float)
    is_global_limit = WwiseProperty[EScope]("IsGlobalLimit", EScope)
    listener_relative_routing = WwiseProperty[bool]("ListenerRelativeRouting", bool)
    loop_count = WwiseProperty[int]("LoopCount", int)
    loudness_normalization_target = WwiseProperty[float]("LoudnessNormalizationTarget", float)
    loudness_normalization_type = WwiseProperty[ELoudnessNormalizationType](
        "LoudnessNormalizationType", ELoudnessNormalizationType)
    lowpass = WwiseProperty[int]("Lowpass", int)
    make_up_gain = WwiseProperty[float]("MakeUpGain", float)
    max_reached_behaviour = WwiseProperty[EDiscardBehaviour]("MaxReachedBehavior", EDiscardBehaviour)
    max_sound_per_instance = WwiseProperty[int]("MaxSoundPerInstance", int)
    metadata = WwiseProperty[GUID]("Metadata", GUID)
    midi_target = WwiseProperty[_MidiTarget]("MidiTarget", _MidiTargetTuple)
    midi_tempo_source = WwiseProperty[EMidiTempoSource]("MidiTempoSource", EMidiTempoSource)
    output_bus = WwiseProperty[Bus]("OutputBus", Bus)
    output_bus_highpass = WwiseProperty[int]("OutputBusHighpass", int)
    output_bus_lowpass = WwiseProperty[int]("OutputBusLowpass", int)
    output_bus_volume = WwiseProperty[float]("OutputBusVolume", float)
    over_limit_behaviour = WwiseProperty[EOverLimitBehaviour]("OverLimitBehavior", EOverLimitBehaviour)
    override_analysis = WwiseProperty[bool]("OverrideAnalysis", bool)
    override_clock_settings = WwiseProperty[bool]("OverrideClockSettings", bool)
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
    playback_speed = WwiseProperty[float]("PlaybackSpeed", float)
    playlist_root = WwiseProperty[MusicPlaylistItem]("PlaylistRoot", MusicPlaylistItem)
    priority = WwiseProperty[int]("Priority", int)
    priority_distance_factor = WwiseProperty[bool]("PriorityDistanceFactor", bool)
    priority_distance_offset = WwiseProperty[int]("PriorityDistanceOffset", int)
    rtpc = WwiseProperty[tuple[Rtpc, ...]]("RTPC", tuple)
    reflections_aux_send = WwiseProperty[AuxBus]("ReflectionsAuxSend", AuxBus)
    reflections_volume = WwiseProperty[float]("ReflectionsVolume", float)
    speaker_panning = WwiseProperty[ESpeakerPanning]("SpeakerPanning", ESpeakerPanning)
    speaker_panning_3d_spatialization_mix = WwiseProperty[int]("SpeakerPanning3DSpatializationMix", int)
    stingers = WwiseProperty[tuple[MusicStinger, ...]]("Stingers", tuple)
    tempo = WwiseProperty[float]("Tempo", float)
    time_signature_lower = WwiseProperty[ETimeSignature]("TimeSignatureLower", ETimeSignature)
    timer_signature_upper = WwiseProperty[int]("TimeSignatureUpper", int)
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
    
    
# Injections - defined in __init__.py
# transition_root
