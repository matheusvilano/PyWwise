# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EAllowStingerNext, EColour, EMusicSegmentPlayPoint
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.music_segment import MusicSegment
from pywwise.objects.types.trigger import Trigger


class MusicStinger(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_musicstinger.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_STINGER`.
    """
    colour = WwiseProperty[EColour]("Color", EColour)
    custom_cue_match_name = WwiseProperty[str]("CustomCueMatchName", str)
    dont_play_again_time = WwiseProperty[float]("DontPlayAgainTime", float)
    num_segment_advance = WwiseProperty[EAllowStingerNext]("NumSegmentAdvance", EAllowStingerNext)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    play_segment_at = WwiseProperty[EMusicSegmentPlayPoint]("PlaySegmentAt", EMusicSegmentPlayPoint)
    segment = WwiseProperty[MusicSegment]("Segment", MusicSegment)
    trigger = WwiseProperty[Trigger]("Trigger", Trigger)
