# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.objects.effects import EffectSlot
from pywwise.objects.syncs import Rtpc
from pywwise.objects.types import WwiseObject


class AudioDevice(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.AUDIO_DEVICE`."""
    bypass_effect = WwiseProperty[bool]("BypassEffect", bool)
    colour = WwiseProperty[int]("Color", int)
    effects = WwiseProperty[list[EffectSlot]]("Effects", list[EffectSlot])
    inclusion = WwiseProperty[bool]("Inclusion", bool)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    rtpc = WwiseProperty[list[Rtpc]]("RTPC", list[Rtpc])


class AuxBus(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.AUX_BUS`."""


class Bus(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.BUS`."""
