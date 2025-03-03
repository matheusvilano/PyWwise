# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from typing import Self as _Self

from pywwise.descriptors import WwiseProperty
from pywwise.enums import (E3DPosition, E3DSpatialization, EBusChannelConfiguration, EColour)
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.attenuation import Attenuation
from pywwise.objects.types.effect_slot import EffectSlot
from pywwise.objects.types.rtpc import Rtpc
from pywwise.primitives import GUID


class AuxBus(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_auxbus.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.AUX_BUS`.
    """
    position_3d = WwiseProperty[E3DPosition]("3DPosition", E3DPosition)
    spatialization_3d = WwiseProperty[E3DSpatialization]("3DSpatialization", E3DSpatialization)
    attenuation = WwiseProperty[Attenuation]("Attenuation", Attenuation)
    attenuation_distance_scaling = WwiseProperty[float]("AttenuationDistanceScaling", float)
    bus_channel_config = WwiseProperty[EBusChannelConfiguration]("BusChannelConfig", EBusChannelConfiguration)
    bus_volume = WwiseProperty[float]("BusVolume", float)
    bypass_all_effects = WwiseProperty[bool]("BypassEffect", bool)
    centre_percentage = WwiseProperty[float]("CenterPercentage", float)
    colour = WwiseProperty[EColour]("Color", EColour)
    effects = WwiseProperty[tuple[EffectSlot, ...]]("Effects", tuple)
    enable_attenuation = WwiseProperty[bool]("EnableAttenuation", bool)
    enable_diffraction = WwiseProperty[bool]("EnableDiffraction", bool)
    game_aux_send_hpf = WwiseProperty[int]("GameAuxSendHPF", int)
    game_aux_send_lpf = WwiseProperty[int]("GameAuxSendLPF", int)
    game_aux_send_volume = WwiseProperty[float]("GameAuxSendVolume", float)
    highpass = WwiseProperty[int]("Highpass", int)
    hold_emitter_position_orientation = WwiseProperty[bool]("HoldEmitterPositionOrientation", bool)
    hold_listener_orientation = WwiseProperty[bool]("HoldListenerOrientation", bool)
    listener_relative_routing = WwiseProperty[bool]("ListenerRelativeRouting", bool)
    lowpass = WwiseProperty[int]("Lowpass", int)
    metadata = WwiseProperty[GUID]("Metadata", GUID)
    output_bus_highpass = WwiseProperty[int]("OutputBusHighpass", int)
    output_bus_lowpass = WwiseProperty[int]("OutputBusLowpass", int)
    output_bus_volume = WwiseProperty[float]("OutputBusVolume", float)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    pitch = WwiseProperty[int]("Pitch", int)
    rtpc = WwiseProperty[tuple[Rtpc, ...]]("RTPC", tuple)
    reflections_aux_send = WwiseProperty[_Self]("ReflectionsAuxSend", _Self)
    reflections_volume = WwiseProperty[float]("ReflectionsVolume", float)
    speaker_panning = WwiseProperty[int]("SpeakerPanning", int)
    speaker_panning_3d_spatialization_mid = WwiseProperty[int]("SpeakerPanning3DSpatializationMix", int)
    use_game_aux_sends = WwiseProperty[bool]("UseGameAuxSends", bool)
    user_aux_send_0 = WwiseProperty[_Self]("UserAuxSend0", _Self)
    user_aux_send_1 = WwiseProperty[_Self]("UserAuxSend1", _Self)
    user_aux_send_2 = WwiseProperty[_Self]("UserAuxSend2", _Self)
    user_aux_send_3 = WwiseProperty[_Self]("UserAuxSend3", _Self)
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
    voice_volume = WwiseProperty[float]("Volume", float)
