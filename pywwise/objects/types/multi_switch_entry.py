# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.random_sequence_container import RandomSequenceContainer
from pywwise.objects.types.switch_container import SwitchContainer
from pywwise.objects.types.blend_container import BlendContainer
from pywwise.objects.types.sound import Sound
from pywwise.objects.types.music_playlist_container import MusicPlaylistContainer
from pywwise.objects.types.music_segment import MusicSegment
from pywwise.objects.types.music_switch_container import MusicSwitchContainer


class MultiSwitchEntry(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_multiswitchentry.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MULTI_SWITCH_ENTRY`.
    """
    # audio_node = WwiseObject[]
