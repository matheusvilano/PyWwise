# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from collections.abc import Sequence as _Sequence

from pywwise.descriptors import WwiseProperty
from pywwise.objects.syncs import Rtpc
from pywwise.objects.types import WwiseObject


class Effect(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.EFFECT`.
    """
    colour = WwiseProperty[int]("Color", int)
    inclusion = WwiseProperty[bool]("Inclusion", bool)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    rtpc = WwiseProperty[_Sequence[Rtpc]]("RTPC", _Sequence[Rtpc])


class EffectSlot(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effectslot.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.EFFECT_SLOT`.
    """
    bypass = WwiseProperty[bool]("Bypass", bool)
    effect = WwiseProperty[Effect]("Effect", Effect)
    rtpc = WwiseProperty[_Sequence[Rtpc]]("RTPC", _Sequence[Rtpc])
    render = WwiseProperty[bool]("Render", bool)
