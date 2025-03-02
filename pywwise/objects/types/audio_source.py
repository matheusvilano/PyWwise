# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EColour, EFadeShape, EMarkerInputMode, ESpeakerBitMask
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.conversion import Conversion
from pywwise.objects.types.marker import Marker


class AudioSource(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_audiofilesource.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.AUDIO_SOURCE`.
    """
    channel_config_override = WwiseProperty[ESpeakerBitMask]("ChannelConfigOverride", ESpeakerBitMask)
    colour = WwiseProperty[EColour]("Color", EColour)
    conversion = WwiseProperty[Conversion]("Conversion", Conversion)
    crossfade_duration = WwiseProperty[float]("CrossfadeDuration", float)
    crossfade_shape = WwiseProperty[EFadeShape]("CrossfadeShape", EFadeShape)
    fade_in_duration = WwiseProperty[float]("FadeInDuration", float)
    fade_in_shape = WwiseProperty[EFadeShape]("FadeInShape", EFadeShape)
    fade_out_duration = WwiseProperty[float]("FadeOutDuration", float)
    fade_out_shape = WwiseProperty[EFadeShape]("FadeOutShape", EFadeShape)
    hdr_envelope = WwiseProperty[float]("HdrEnvelope", float)
    loop_begin = WwiseProperty[float]("LoopBegin", float)
    loop_end = WwiseProperty[float]("LoopEnd", float)
    marker_detection_sensitivity = WwiseProperty[float]("MarkerDetectionSensitivity", float)
    marker_input_mode = WwiseProperty[EMarkerInputMode]("MarkerInputMode", EMarkerInputMode)
    markers = WwiseProperty[list[Marker]]("Markers", list[Marker])
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    override_conversion = WwiseProperty[bool]("OverrideConversion", bool)
    override_wav_loop = WwiseProperty[bool]("OverrideWavLoop", bool)
    trim_begin = WwiseProperty[float]("TrimBegin", float)
    trim_end = WwiseProperty[float]("TrimEnd", float)
    volume_offset = WwiseProperty[float]("VolumeOffset", float)
