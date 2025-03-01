# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EMatchMode
from pywwise.objects.abc import WwiseObject
from pywwise.objects.multi_switch_entry import MultiSwitchEntry
from pywwise.objects.state_group import StateGroup
from pywwise.objects.switch_group import SwitchGroup


class DialogueEvent(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_dialogueevent.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.DIALOGUE_EVENT`.
    """
    arguments = WwiseProperty[list[SwitchGroup | StateGroup]]("Arguments", list[SwitchGroup | StateGroup])
    colour = WwiseProperty[int]("Color", int)
    entries = WwiseProperty[list[MultiSwitchEntry]]("Entries", list[MultiSwitchEntry])
    mode = WwiseProperty[EMatchMode]("Mode", EMatchMode)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    probability = WwiseProperty[int]("Probability", int)
