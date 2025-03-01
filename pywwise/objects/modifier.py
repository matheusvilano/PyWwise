# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.objects.abc import WwiseObject


class Modifier(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_modifier.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MODIFIER`.
    """
    enabled = WwiseProperty[bool]("Enabled", bool)
    max = WwiseProperty[float]("Max", float)
    min = WwiseProperty[float]("Min", float)
