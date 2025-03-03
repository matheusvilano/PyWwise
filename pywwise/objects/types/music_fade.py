# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EFadeType, EMusicFadeShape
from pywwise.objects.abc import WwiseObject


class MusicFade(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_musicfade.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_FADE`.
    """
    fade_curve = WwiseProperty[EMusicFadeShape]("FadeCurve", EMusicFadeShape)
    fade_offset = WwiseProperty[float]("FadeOffset", float)
    fade_time = WwiseProperty[float]("FadeTime", float)
    fade_type = WwiseProperty[EFadeType]("FadeType", EFadeType)
