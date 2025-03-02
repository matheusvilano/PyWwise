# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EColour
from pywwise.objects.abc import WwiseObject


class Event(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_event.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.EVENT`.
    """
    colour = WwiseProperty[EColour]("Color", EColour)
    inclusion = WwiseProperty[bool]("Inclusion", bool)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
