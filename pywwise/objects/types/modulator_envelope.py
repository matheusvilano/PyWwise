# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EColour, EEnvelopeTriggerOn, EModulatorScopeLimited
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.rtpc import Rtpc


class ModulatorEnvelope(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_modulatorenvelope.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MODULATOR_ENVELOPE`.
    """
    colour = WwiseProperty[EColour]("Color", EColour)
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
    rtpc = WwiseProperty[tuple[Rtpc, ...]]("RTPC", tuple)
