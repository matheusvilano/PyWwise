# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EColour
from pywwise.objects.abc import WwiseObject


class MusicClipMidi(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_musicclipmidi.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_CLIP_MIDI`.
    """
    begin_trim_offset = WwiseProperty[float]("BeginTrimOffset", float)
    colour = WwiseProperty[EColour]("Color", EColour)
    end_trim_offset = WwiseProperty[float]("EndTrimOffset", float)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    play_at = WwiseProperty[float]("PlayAt", float)
