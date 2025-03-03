# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.rtpc import Rtpc


class Panner(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_panner.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.PANNER`.
    """
    pan_x = WwiseProperty[float]("PanX", float)
    pan_y = WwiseProperty[float]("PanY", float)
    pan_z = WwiseProperty[float]("PanZ", float)
    rtpc = WwiseProperty[tuple[Rtpc, ...]]("RTPC", tuple)
