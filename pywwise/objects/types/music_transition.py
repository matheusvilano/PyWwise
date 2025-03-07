# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from typing import Union as _Union

from pywwise.descriptors import WwiseProperty
from pywwise.enums import (EColour, ECustomCueJumpMatchMode, EDestinationContextType, EMusicDestinationJumpTo,
                           EMusicDestinationSyncTo, EMusicSourceExitPoint)
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.music_playlist_container import MusicPlaylistContainer
from pywwise.objects.types.music_segment import MusicSegment
from pywwise.objects.types.music_switch_container import MusicSwitchContainer
from pywwise.objects.types.music_track import MusicTrack

_InteractiveMusic = _Union[MusicPlaylistContainer, MusicSegment, MusicSwitchContainer, MusicTrack]


class MusicTransition(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_musictransition.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_TRANSITION`.
    """
    colour = WwiseProperty[EColour]("Color", EColour)
    destination_context_object = WwiseProperty[_InteractiveMusic]("DestinationContextObject", _InteractiveMusic)
    destination_context_type = WwiseProperty[EDestinationContextType]("DestinationContextType", EDestinationContextType)
    destination_jump_position_preset = WwiseProperty[EMusicDestinationSyncTo]("DestinationJumpPositionPreset",
                                                                              EMusicDestinationSyncTo)
    destination_playlist_jump_to = WwiseProperty[EMusicDestinationJumpTo]("DestinationPlaylistJumpTo",
                                                                          EMusicDestinationJumpTo)
    enable_destination_fade_in = WwiseProperty[bool]("EnableDestinationFadeIn", bool)
    enable_source_fade_out = WwiseProperty[bool]("EnableSourceFadeOut", bool)
    enable_transition_fade_in = WwiseProperty[bool]("EnableTransitionFadeIn", bool)
    enable_transition_fade_out = WwiseProperty[bool]("EnableTransitionFadeOut", bool)
    exit_source_at = WwiseProperty[EMusicSourceExitPoint]("ExitSourceAt", EMusicSourceExitPoint)
    exit_source_custom_cue_match_name = WwiseProperty[str]("ExitSourceCustomCueMatchName", str)
    is_folder = WwiseProperty[bool]("IsFolder", bool)
    jump_to_custom_cue_match_mode = WwiseProperty[ECustomCueJumpMatchMode]("JumpToCustomCueMatchMode",
                                                                           ECustomCueJumpMatchMode)
    jump_to_custom_cue_match_name = WwiseProperty[str]("jumpToCustomCueMatchName", str)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    play_destination_pre_entry = WwiseProperty[bool]("PlayDestinationPreEntry", bool)
    play_post_exit = WwiseProperty[bool]("PlayPostExit", bool)
    play_transition_post_Exit = WwiseProperty[bool]("PlayTransitionPostExit", bool)
    play_transition_pre_entry = WwiseProperty[bool]("PlayTransitionPreEntry", bool)
    source_context_object = WwiseProperty[_InteractiveMusic]("SourceContextObject", _InteractiveMusic)
    source_context_type = WwiseProperty[EDestinationContextType]("SourceContextType", EDestinationContextType)
    use_transition_object = WwiseProperty[bool]("UseTransitionObject", bool)


# Injections - defined in __init__.py
# entries
