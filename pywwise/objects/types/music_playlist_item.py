# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EColour, EMusicPlaylistItemType, EPlaylistMode, ERandomType
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.music_segment import MusicSegment


class MusicPlaylistItem(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_musicplaylistitem.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_PLAYLIST_ITEM`.
    """
    colour = WwiseProperty[EColour]("Color", EColour)
    loop_count = WwiseProperty[int]("LoopCount", int)
    normal_or_shuffle = WwiseProperty[ERandomType]("NormalOrShuffle", ERandomType)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    play_mode = WwiseProperty[EPlaylistMode]("PlayMode", EPlaylistMode)
    playlist_item_type = WwiseProperty[EMusicPlaylistItemType]("PlaylistItemType", EMusicPlaylistItemType)
    random_avoid_repeating_count = WwiseProperty[int]("RandomAvoidRepeatingCount", int)
    segment = WwiseProperty[MusicSegment]("Segment", MusicSegment)
    weight = WwiseProperty[float]("Weight", float)
