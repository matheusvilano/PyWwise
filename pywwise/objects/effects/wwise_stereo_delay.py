# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EStereoDelayFilterType, EStereoDelayInput
from pywwise.objects.abc import WwiseObject


class WwiseStereoDelay(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect_wwise_stereo_delay.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WWISE_STEREO_DELAY`.
    """
    dry_level = WwiseProperty[float]("DryLevel", float)
    enable_cross_feed = WwiseProperty[bool]("EnableCrossFeed", bool)
    enable_feedback = WwiseProperty[bool]("EnableFeedback", bool)
    filter_frequency = WwiseProperty[float]("FilterFrequency", float)
    filter_gain = WwiseProperty[float]("FilterGain", float)
    filter_q = WwiseProperty[float]("FilterQFactor", float)
    filter_type = WwiseProperty[EStereoDelayFilterType]("FilterType", EStereoDelayFilterType)
    front_rear_balance = WwiseProperty[float]("FrontRearBalance", float)
    left_crossfeed = WwiseProperty[float]("LeftCrossfeed", float)
    left_delay_time = WwiseProperty[float]("LeftDelayTime", float)
    left_feedback = WwiseProperty[float]("LeftFeedback", float)
    left_input_type = WwiseProperty[EStereoDelayInput]("LeftInputType", EStereoDelayInput)
    right_crossfeed = WwiseProperty[float]("RightCrossfeed", float)
    right_delay_time = WwiseProperty[float]("RightDelayTime", float)
    right_feedback = WwiseProperty[float]("RightFeedback", float)
    right_input_type = WwiseProperty[EStereoDelayInput]("RightInputType", EStereoDelayInput)
    wet_level = WwiseProperty[float]("WetLevel", float)
