# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EColour, EModulatorScope, EWaveformInt
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.rtpc import Rtpc


class ModulatorLfo(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_modulatorlfo.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MODULATOR_LFO`.
    """
    colour = WwiseProperty[EColour]("Color", EColour)
    lfo_attack = WwiseProperty[float]("LfoAttack", float)
    lfo_depth = WwiseProperty[float]("LfoDepth", float)
    lfo_frequency = WwiseProperty[float]("LfoFrequency", float)
    lfo_initial_phase = WwiseProperty[float]("LfoInitialPhase", float)
    lfo_pwm = WwiseProperty[float]("LfoPWM", float)
    lfo_smoothing = WwiseProperty[float]("LfoSmoothing", float)
    lfo_waveform = WwiseProperty[EWaveformInt]("LfoWaveform", EWaveformInt)
    modulator_scope = WwiseProperty[EModulatorScope]("ModulatorScope", EModulatorScope)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    rtpc = WwiseProperty[tuple[Rtpc, ...]]("RTPC", tuple)
