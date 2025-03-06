# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from typing import Union as _Union

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EColour
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.curve import Curve
from pywwise.objects.types.game_parameter import GameParameter
from pywwise.objects.types.midi_parameter import MidiParameter
from pywwise.objects.types.modulator_envelope import ModulatorEnvelope
from pywwise.objects.types.modulator_lfo import ModulatorLfo
from pywwise.objects.types.modulator_time import ModulatorTime

_ControlInputType = _Union[ModulatorLfo, ModulatorEnvelope, ModulatorTime, GameParameter, MidiParameter]

_ControlInputTypeTuple = (ModulatorLfo, ModulatorEnvelope, ModulatorTime, GameParameter, MidiParameter)


class Rtpc(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_rtpc.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.RTPC`.
    """
    colour = WwiseProperty[EColour]("Color", EColour)
    control_input = WwiseProperty[_ControlInputType]("ControlInput", _ControlInputTypeTuple)
    curve = WwiseProperty[Curve]("Curve", Curve)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    property_name = WwiseProperty[str]("PropertyName", str)
