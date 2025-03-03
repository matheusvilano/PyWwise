# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EColour, EFadeMode, EFadeShape
from pywwise.objects.abc import WwiseObject


class MusicClip(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_musicclip.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_CLIP`.
    """
    begin_trim_offset = WwiseProperty[float]("BeginTrimOffset", float)
    colour = WwiseProperty[EColour]("Color", EColour)
    end_trim_offset = WwiseProperty[float]("EndTrimOffset", float)
    fade_in_duration = WwiseProperty[float]("FadeInDuration", float)
    fade_in_mode = WwiseProperty[EFadeMode]("FadeInDuration", EFadeMode)
    fade_in_shape = WwiseProperty[EFadeShape]("FadeInShape", EFadeShape)
    fade_out_duration = WwiseProperty[float]("FadeOutDuration", float)
    fade_out_mode = WwiseProperty[EFadeMode]("FadeOutMode", EFadeMode)
    fade_out_shape = WwiseProperty[EFadeShape]("FadeOutShape", EFadeShape)
    highpass = WwiseProperty[int]("Highpass", int)
    lowpass = WwiseProperty[int]("Lowpass", int)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    play_at = WwiseProperty[float]("PlayAt", float)
    volume = WwiseProperty[float]("Volume", float)
