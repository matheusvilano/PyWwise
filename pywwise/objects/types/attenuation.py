# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EColour
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.rtpc import Rtpc


class Attenuation(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_attenuation.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.ATTENUATION`.
    """
    colour = WwiseProperty[EColour]("Color", EColour)
    cone_attenuation = WwiseProperty[float]("ConeAttenuation", float)
    cone_high_pass_filter_value = WwiseProperty[int]("ConeHighPassFilterAngle", int)
    cone_inner_angle = WwiseProperty[int]("ConeInnerAngle", int)
    cone_low_pass_filter_value = WwiseProperty[int]("ConeLowPassFilterAngle", int)
    cone_outer_angle = WwiseProperty[int]("ConeOuterAngle", int)
    cone_use = WwiseProperty[bool]("ConeUse", bool)
    height_spread_enable = WwiseProperty[bool]("HeightSpreadEnable", bool)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    rtpc = WwiseProperty[tuple[Rtpc, ...]]("RTPC", tuple)
    radius_max = WwiseProperty[float]("RadiusMax", float)
