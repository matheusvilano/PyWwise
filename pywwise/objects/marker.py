# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.objects.abc import WwiseObject


class Marker(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_marker.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MARKER`.
    """
    colour = WwiseProperty[int]("Color", int)
    label = WwiseProperty[str]("Label", str)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    time = WwiseProperty[float]("Time", float)
