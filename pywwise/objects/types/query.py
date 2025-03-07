# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EColour, ELogicalOperator, EObjectTypeQuery, EPlatformOption
from pywwise.objects.abc import WwiseObject


class Query(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_query.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.QUERY`.
    """
    colour = WwiseProperty[EColour]("Color", EColour)
    logical_operator = WwiseProperty[ELogicalOperator]("LogicalOperator", ELogicalOperator)
    object_type = WwiseProperty[EObjectTypeQuery]("ObjectType", EObjectTypeQuery)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    platform = WwiseProperty[EPlatformOption]("Platform", EPlatformOption)
    start_object = WwiseProperty[WwiseObject]("StartObject", WwiseObject)
    waql = WwiseProperty[str]("WAQL", str)
