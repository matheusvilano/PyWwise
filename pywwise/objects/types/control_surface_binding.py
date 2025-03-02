# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EColour, EControlSurfaceBindingTargetType
from pywwise.objects.abc import WwiseObject


class ControlSurfaceBinding(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_controlsurfacebinding.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.CONTROL_SURFACE_BINDING`.
    """
    colour = WwiseProperty[EColour]("Color", EColour)
    hardware_controller_key = WwiseProperty[str]("HardwareControllerKey", str)
    object_index_in_view = WwiseProperty[int]("ObjectIndexInView", int)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    target_class_id = WwiseProperty[int]("TargetClassId", int)
    target_name = WwiseProperty[str]("TargetName", str)
    target_object = WwiseProperty[WwiseObject]("TargetObject", WwiseObject)
    target_type = WwiseProperty[EControlSurfaceBindingTargetType]("TargetType", EControlSurfaceBindingTargetType)
