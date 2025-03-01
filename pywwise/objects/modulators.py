# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from collections.abc import Sequence as _Sequence

from pywwise.objects.types import WwiseObject
from pywwise.descriptors import WwiseProperty
from pywwise.objects.syncs import Rtpc
from pywwise.enums import EEnvelopeTriggerOn, EModulatorScope, EModulatorScopeLimited, EWaveformInt


class Modifier(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_modifier.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MODIFIER`.
    """
    enabled = WwiseProperty[bool]("Enabled", bool)
    max = WwiseProperty[float]("Max", float)
    min = WwiseProperty[float]("Min", float)


class ModulatorEnvelope(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_modulatorenvelope.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MODULATOR_ENVELOPE`.
    """
    colour = WwiseProperty[int]("Color", int)
    envelope_attack_curve = WwiseProperty[float]("EnvelopeAttackCurve", float)
    envelope_attack_time = WwiseProperty[float]("EnvelopeAttackTime", float)
    envelope_auto_release = WwiseProperty[bool]("EnvelopeAutoRelease", bool)
    envelope_decay_time = WwiseProperty[float]("EnvelopeDecayTime", float)
    envelope_release_time = WwiseProperty[float]("EnvelopeReleaseTime", float)
    envelope_stop_playback = WwiseProperty[bool]("EnvelopeStopPlayback", bool)
    envelope_sustain_level = WwiseProperty[float]("EnvelopeSustainLevel", float)
    envelope_sustain_time = WwiseProperty[float]("EnvelopeSustainTime", float)
    envelope_trigger_on = WwiseProperty[EEnvelopeTriggerOn]("EnvelopeTriggerOn", EEnvelopeTriggerOn)
    modulator_scope = WwiseProperty[EModulatorScopeLimited]("ModulatorScope", EModulatorScopeLimited)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    rtpc = WwiseProperty[_Sequence[Rtpc]]("RTPC", _Sequence[Rtpc])


class ModulatorLfo(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_modulatorlfo.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MODULATOR_LFO`.
    """
    colour = WwiseProperty[int]("Color", int)
    lfo_attack = WwiseProperty[float]("LfoAttack", float)
    lfo_depth = WwiseProperty[float]("LfoDepth", float)
    lfo_frequency = WwiseProperty[float]("LfoFrequency", float)
    lfo_initial_phase = WwiseProperty[float]("LfoInitialPhase", float)
    lfo_pwm = WwiseProperty[float]("LfoPWM", float)
    lfo_smoothing = WwiseProperty[float]("LfoSmoothing", float)
    lfo_waveform = WwiseProperty[EWaveformInt]("LfoWaveform", EWaveformInt)
    modulator_scope = WwiseProperty[EModulatorScope]("ModulatorScope", EModulatorScope)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    rtpc = WwiseProperty[_Sequence[Rtpc]]("RTPC", _Sequence[Rtpc])


class ModulatorTime(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_modulatortime.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MODULATOR_TIME`.
    """
    colour = WwiseProperty[int]("Color", int)
    envelope_stop_playback = WwiseProperty[bool]("EnvelopeStopPlayback", bool)
    envelope_trigger_on = WwiseProperty[EEnvelopeTriggerOn]("EnvelopeTriggerOn", EEnvelopeTriggerOn)
    modulator_scope = WwiseProperty[EModulatorScopeLimited]("ModulatorScope", EModulatorScopeLimited)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    rtpc = WwiseProperty[_Sequence[Rtpc]]("RTPC", _Sequence[Rtpc])
    time_mod_duration = WwiseProperty[float]("TimeModDuration", float)
    time_mod_initial_delay = WwiseProperty[float]("TimeModInitialDelay", float)
    time_mod_loops = WwiseProperty[int]("TimeModLoops", int)
    time_mod_playback_rate = WwiseProperty[float]("TimeModPlaybackRate", float)
