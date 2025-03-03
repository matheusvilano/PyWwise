# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types import Event


class MusicEventCue(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_musiceventcue.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_EVENT_CUE`.
    """
    play_at = WwiseProperty[float]("PlayAt", float)
    post_event_target = WwiseProperty[Event]("PostEventTarget", Event)
