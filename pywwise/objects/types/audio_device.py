# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EColour
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.effect_slot import EffectSlot
from pywwise.objects.types.rtpc import Rtpc


class AudioDevice(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_audiodevice.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.AUDIO_DEVICE`.
    """
    bypass_effect = WwiseProperty[bool]("BypassEffect", bool)
    colour = WwiseProperty[EColour]("Color", EColour)
    effects = WwiseProperty[list[EffectSlot]]("Effects", list[EffectSlot])
    inclusion = WwiseProperty[bool]("Inclusion", bool)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    rtpc = WwiseProperty[list[Rtpc]]("RTPC", list[Rtpc])
