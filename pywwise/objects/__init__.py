# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.objects.abc import WwiseObject, WwiseObjectType
from pywwise.objects.acoustic_texture import AcousticTexture
from pywwise.objects.action import Action
from pywwise.objects.action_exception import ActionException
from pywwise.objects.actor_mixer import ActorMixer
from pywwise.objects.attenuation import Attenuation
from pywwise.objects.audio_device import AudioDevice
from pywwise.objects.audio_source import AudioSource
from pywwise.objects.aux_bus import AuxBus
from pywwise.objects.blend_container import BlendContainer
from pywwise.objects.blend_track import BlendTrack
from pywwise.objects.bus import Bus
from pywwise.objects.control_surface_binding import ControlSurfaceBinding
from pywwise.objects.control_surface_binding_group import ControlSurfaceBindingGroup
from pywwise.objects.control_surface_session import ControlSurfaceSession
from pywwise.objects.conversion import Conversion
from pywwise.objects.curve import Curve
from pywwise.objects.custom_state import CustomState
from pywwise.objects.dialogue_event import DialogueEvent
from pywwise.objects.effect import Effect
from pywwise.objects.effect_slot import EffectSlot
from pywwise.objects.event import Event
from pywwise.objects.external_source import ExternalSource
from pywwise.objects.external_source_file import ExternalSourceFile
from pywwise.objects.folder import Folder
from pywwise.objects.game_parameter import GameParameter
from pywwise.objects.language import Language
from pywwise.objects.marker import Marker
from pywwise.objects.metadata import Metadata
from pywwise.objects.midi_file_source import MidiFileSource
from pywwise.objects.midi_parameter import MidiParameter
from pywwise.objects.mixing_session import MixingSession
from pywwise.objects.modifier import Modifier
from pywwise.objects.modulator_envelope import ModulatorEnvelope
from pywwise.objects.modulator_lfo import ModulatorLfo
from pywwise.objects.modulator_time import ModulatorTime
from pywwise.objects.multi_switch_entry import MultiSwitchEntry
from pywwise.objects.music_clip import MusicClip
from pywwise.objects.music_clip_midi import MusicClipMidi
from pywwise.objects.music_cue import MusicCue
from pywwise.objects.music_event_cue import MusicEventCue
from pywwise.objects.music_fade import MusicFade
from pywwise.objects.music_playlist_container import MusicPlaylistContainer
from pywwise.objects.music_playlist_item import MusicPlaylistItem
from pywwise.objects.music_segment import MusicSegment
from pywwise.objects.music_stinger import MusicStinger
from pywwise.objects.music_switch_container import MusicSwitchContainer
from pywwise.objects.music_track import MusicTrack
from pywwise.objects.music_track_sequence import MusicTrackSequence
from pywwise.objects.music_transition import MusicTransition
from pywwise.objects.object_setting_assoc import ObjectSettingAssoc
from pywwise.objects.panner import Panner
from pywwise.objects.path_2d import Path2d
from pywwise.objects.platform import Platform
from pywwise.objects.plugin_data_source import PluginDataSource
from pywwise.objects.position import Position
from pywwise.objects.project import Project
from pywwise.objects.query import Query
from pywwise.objects.random_sequence_container import RandomSequenceContainer
from pywwise.objects.rtpc import Rtpc
from pywwise.objects.search_criteria import SearchCriteria
from pywwise.objects.sound import Sound
from pywwise.objects.sound_bank import SoundBank
from pywwise.objects.soundcaster_session import SoundcasterSession
from pywwise.objects.source_plugin import SourcePlugin
from pywwise.objects.state import State
from pywwise.objects.state_group import StateGroup
from pywwise.objects.switch import Switch
from pywwise.objects.switch_container import SwitchContainer
from pywwise.objects.switch_group import SwitchGroup
from pywwise.objects.trigger import Trigger
from pywwise.objects.user_project_settings import UserProjectSettings
from pywwise.objects.work_unit import WorkUnit
