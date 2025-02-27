# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from collections.abc import Sequence as _Sequence

from pywwise.objects.types import WwiseObject
from pywwise.descriptors import WwiseProperty
from pywwise.objects.syncs import Rtpc


class Metadata(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_metadata.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.METADATA`.
    """
    colour = WwiseProperty[int]("Color", int)
    inclusion = WwiseProperty[bool]("Inclusion", bool)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    rtpc = WwiseProperty[_Sequence[Rtpc]]("RTPC", _Sequence[Rtpc])
