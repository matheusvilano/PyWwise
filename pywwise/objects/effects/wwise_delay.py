# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.objects.abc import WwiseObject


class WwiseDelay(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect_wwise_delay.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WWISE_DELAY`.
    """
    delay_time = WwiseProperty[float]("DelayTime", float)
    feedback = WwiseProperty[float]("Feedback", float)
    feedback_enabled = WwiseProperty[bool]("FeedbackEnabled", bool)
    output_level = WwiseProperty[float]("OutputLevel", float)
    process_lfe = WwiseProperty[bool]("ProcessLFE", bool)
    wet_dry_mix = WwiseProperty[float]("WetDryMix", float)
