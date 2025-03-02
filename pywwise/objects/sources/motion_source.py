# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EMotionChannelConfig, EMotionDriver
from pywwise.objects.abc import WwiseObject


class MotionSource(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_source_motion_source.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SOURCE_PLUGIN`.
    """
    channel_1 = WwiseProperty[EMotionDriver]("Channel1", EMotionDriver)
    channel_2 = WwiseProperty[EMotionDriver]("Channel2", EMotionDriver)
    channel_3 = WwiseProperty[EMotionDriver]("Channel3", EMotionDriver)
    channel_4 = WwiseProperty[EMotionDriver]("Channel4", EMotionDriver)
    channel_config = WwiseProperty[EMotionChannelConfig]("ChannelConfig", EMotionChannelConfig)
    driver_a = WwiseProperty[float]("DriverA", float)
    driver_b = WwiseProperty[float]("DriverB", float)
    driver_c = WwiseProperty[float]("DriverC", float)
    driver_d = WwiseProperty[float]("DriverD", float)
    driver_e = WwiseProperty[float]("DriverE", float)
    driver_f = WwiseProperty[float]("DriverF", float)
    driver_g = WwiseProperty[float]("DriverG", float)
    driver_h = WwiseProperty[float]("DriverH", float)
    high_1 = WwiseProperty[EMotionDriver]("High1", EMotionDriver)
    high_2 = WwiseProperty[EMotionDriver]("High2", EMotionDriver)
    left_trigger = WwiseProperty[EMotionDriver]("LeftTrigger", EMotionDriver)
    low_1 = WwiseProperty[EMotionDriver]("Low1", EMotionDriver)
    low_2 = WwiseProperty[EMotionDriver]("Low2", EMotionDriver)
    right_trigger = WwiseProperty[EMotionDriver]("RightTrigger", EMotionDriver)
