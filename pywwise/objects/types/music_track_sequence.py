# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EColour, EMusicClipType, ESwitchOrState
from pywwise.objects.abc import WwiseObject


class MusicTrackSequence(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_musictracksequence.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_TRACK_SEQUENCE`.
    """
    clips = WwiseProperty[tuple[EMusicClipType, ...]]("Clips", tuple)
    colour = WwiseProperty[EColour]("Color", EColour)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    track_sequence_switch = WwiseProperty[ESwitchOrState]("TrackSequenceSwitch", ESwitchOrState)
