# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.objects.abc import WwiseObject


class WwisePeakLimiter(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect_wwise_peak_limiter.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WwisePeakLimiter`.
    """
    channel_link = WwiseProperty[bool]("ChannelLink", bool)
    look_ahead = WwiseProperty[float]("LookAhead", float)
    output_gain = WwiseProperty[float]("OutputGain", float)
    process_lfe = WwiseProperty[bool]("ProcessLFE", bool)
    ratio = WwiseProperty[float]("Ratio", float)
    release_time = WwiseProperty[float]("ReleaseTime", float)
    threshold = WwiseProperty[float]("Threshold", float)
