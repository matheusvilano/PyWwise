# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EColour, EMusicCueType
from pywwise.objects.abc import WwiseObject


class MusicCue(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_musiccue.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_CUE`.
    """
    colour = WwiseProperty[EColour]("Color", EColour)
    cue_type = WwiseProperty[EMusicCueType]("CueType", EMusicCueType)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    time_ms = WwiseProperty[float]("TimeMs", float)
