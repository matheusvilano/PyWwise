# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EColour
from pywwise.objects.abc import WwiseObject


class SwitchGroup(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_switchgroup.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SWITCH_GROUP`.
    """
    colour = WwiseProperty[EColour]("Color", EColour)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    use_game_parameter = WwiseProperty[bool]("UseGameParameter", bool)
