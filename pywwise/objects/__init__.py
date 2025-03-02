# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.objects.abc import WwiseObject, WwiseObjectType
from pywwise.objects.effects import (MasteringSuite, Wwise3DAudioBedMixer, WwiseCompressor, WwiseConvolutionReverb,
                                     WwiseDelay, WwiseExpander, WwiseFlanger, WwiseGain, WwiseGuitarDistortion,
                                     WwiseHarmonizer, WwiseMatrixReverb, WwiseMeter, WwiseParametricEq,
                                     WwisePeakLimiter, WwisePitchShifter, WwiseRecorder, WwiseReflect, WwiseRoomVerb,
                                     WwiseStereoDelay, WwiseTimeStretch, WwiseTremolo)
from pywwise.objects.sources import (Impacter, MotionSource, SoundSeedAirWind, SoundSeedAirWoosh, SoundSeedGrain,
                                     WwiseSilence, WwiseSynthOne, WwiseToneGenerator)
from pywwise.objects.types import (AcousticTexture, Action, ActionException, ActorMixer, Attenuation, AudioDevice,
                                   AudioSource, AuxBus, BlendContainer, BlendTrack, Bus, ControlSurfaceBinding,
                                   ControlSurfaceBindingGroup, ControlSurfaceSession, Conversion, Curve,
                                   CustomState, DialogueEvent, Effect, EffectSlot, Event, ExternalSource,
                                   ExternalSourceFile, Folder, GameParameter, Language, Marker, Metadata,
                                   MidiFileSource, MidiParameter, MixingSession, Modifier, ModulatorEnvelope,
                                   ModulatorLfo, ModulatorTime, MultiSwitchEntry, MusicClip, MusicClipMidi,
                                   MusicCue, MusicEventCue, MusicFade, MusicPlaylistContainer, MusicPlaylistItem,
                                   MusicSegment, MusicStinger, MusicSwitchContainer, MusicTrack, MusicTrackSequence,
                                   MusicTransition, ObjectSettingAssoc, Panner, Path2d, Platform, PluginDataSource,
                                   Position, Project, Query, RandomSequenceContainer, Rtpc, SearchCriteria, Sound,
                                   SoundBank, SoundcasterSession, SourcePlugin, State, StateGroup, Switch,
                                   SwitchContainer, SwitchGroup, Trigger, UserProjectSettings, WorkUnit)
