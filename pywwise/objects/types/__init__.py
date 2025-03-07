# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.objects.types.acoustic_texture import AcousticTexture
from pywwise.objects.types.action import Action
from pywwise.objects.types.action_exception import ActionException
from pywwise.objects.types.actor_mixer import ActorMixer
from pywwise.objects.types.attenuation import Attenuation
from pywwise.objects.types.audio_device import AudioDevice
from pywwise.objects.types.audio_source import AudioSource
from pywwise.objects.types.aux_bus import AuxBus
from pywwise.objects.types.blend_container import BlendContainer
from pywwise.objects.types.blend_track import BlendTrack
from pywwise.objects.types.bus import Bus
from pywwise.objects.types.control_surface_binding import ControlSurfaceBinding
from pywwise.objects.types.control_surface_binding_group import ControlSurfaceBindingGroup
from pywwise.objects.types.control_surface_session import ControlSurfaceSession
from pywwise.objects.types.conversion import Conversion
from pywwise.objects.types.curve import Curve
from pywwise.objects.types.custom_state import CustomState
from pywwise.objects.types.dialogue_event import DialogueEvent
from pywwise.objects.types.effect import Effect
from pywwise.objects.types.effect_slot import EffectSlot
from pywwise.objects.types.event import Event
from pywwise.objects.types.external_source import ExternalSource
from pywwise.objects.types.external_source_file import ExternalSourceFile
from pywwise.objects.types.folder import Folder
from pywwise.objects.types.game_parameter import GameParameter
from pywwise.objects.types.language import Language
from pywwise.objects.types.marker import Marker
from pywwise.objects.types.metadata import Metadata
from pywwise.objects.types.midi_file_source import MidiFileSource
from pywwise.objects.types.midi_parameter import MidiParameter
from pywwise.objects.types.mixing_session import MixingSession
from pywwise.objects.types.modifier import Modifier
from pywwise.objects.types.modulator_envelope import ModulatorEnvelope
from pywwise.objects.types.modulator_lfo import ModulatorLfo
from pywwise.objects.types.modulator_time import ModulatorTime
from pywwise.objects.types.multi_switch_entry import MultiSwitchEntry
from pywwise.objects.types.music_clip import MusicClip
from pywwise.objects.types.music_clip_midi import MusicClipMidi
from pywwise.objects.types.music_cue import MusicCue
from pywwise.objects.types.music_event_cue import MusicEventCue
from pywwise.objects.types.music_fade import MusicFade
from pywwise.objects.types.music_playlist_container import MusicPlaylistContainer
from pywwise.objects.types.music_playlist_item import MusicPlaylistItem
from pywwise.objects.types.music_segment import MusicSegment
from pywwise.objects.types.music_stinger import MusicStinger
from pywwise.objects.types.music_switch_container import MusicSwitchContainer
from pywwise.objects.types.music_track import MusicTrack
from pywwise.objects.types.music_track_sequence import MusicTrackSequence
from pywwise.objects.types.music_transition import MusicTransition
from pywwise.objects.types.object_setting_assoc import ObjectSettingAssoc
from pywwise.objects.types.panner import Panner
from pywwise.objects.types.path_2d import Path2d
from pywwise.objects.types.platform import Platform
from pywwise.objects.types.plugin_data_source import PluginDataSource
from pywwise.objects.types.position import Position
from pywwise.objects.types.project import Project
from pywwise.objects.types.query import Query
from pywwise.objects.types.random_sequence_container import RandomSequenceContainer
from pywwise.objects.types.rtpc import Rtpc
from pywwise.objects.types.search_criteria import SearchCriteria
from pywwise.objects.types.sound import Sound
from pywwise.objects.types.sound_bank import SoundBank
from pywwise.objects.types.soundcaster_session import SoundcasterSession
from pywwise.objects.types.source_plugin import SourcePlugin
from pywwise.objects.types.state import State
from pywwise.objects.types.state_group import StateGroup
from pywwise.objects.types.switch import Switch
from pywwise.objects.types.switch_container import SwitchContainer
from pywwise.objects.types.switch_group import SwitchGroup
from pywwise.objects.types.trigger import Trigger
from pywwise.objects.types.user_project_settings import UserProjectSettings
from pywwise.objects.types.work_unit import WorkUnit


# Injections - solution for circular imports; add as needed, as a last resort. Also document in class.
MusicPlaylistContainer.transition_root = WwiseProperty[MusicTransition]("TransitionRoot", MusicTransition)
MusicSegment.stingers = WwiseProperty[tuple[MusicStinger, ...]]("Stingers", tuple)
MusicStinger.segment = WwiseProperty[MusicSegment]("Segment", MusicSegment)
MusicSwitchContainer.transition_root = WwiseProperty[MusicTransition]("TransitionRoot", MusicTransition)
MusicTrack.transition_root = WwiseProperty[MusicTransition]("TransitionRoot", MusicTransition)
MusicTransition.entries = WwiseProperty[tuple[MultiSwitchEntry, ...]]("Entries", tuple)
