# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.objects.abc import WwiseObject


class WwiseCompressor(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect_wwise_compressor.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WWISE_COMPRESSOR`.
    """
    attack_time = WwiseProperty[float]("AttackTime", float)
    channel_link = WwiseProperty[bool]("ChannelLink", bool)
    output_gain = WwiseProperty[float]("OutputGain", float)
    process_lfe = WwiseProperty[bool]("ProcessLFE", bool)
    ratio = WwiseProperty[float]("Ratio", float)
    release_time = WwiseProperty[float]("ReleaseTime", float)
    threshold = WwiseProperty[float]("Threshold", float)
