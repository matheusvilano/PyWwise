# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.objects.types import WwiseObject


class SoundBank(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SOUND_BANK`."""
    colour = WwiseProperty[int]("Color", int)
    fill = WwiseProperty[bool]("Fill", bool)
    maximum = WwiseProperty[int]("Maximum", int)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
