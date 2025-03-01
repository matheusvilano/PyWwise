# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.objects.types import WwiseObject
from pywwise.descriptors import WwiseProperty


class MidiFileSource(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_midifilesource.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MIDI_FILE_SOURCE`.
    """


class MidiParameter(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_midiparameter.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MIDI_PARAMETER`.
    """
    simulation_value = WwiseProperty[float]("SimulationValue", float)
