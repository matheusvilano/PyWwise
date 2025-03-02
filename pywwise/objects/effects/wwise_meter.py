# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EMeterMode, EMeterScope
from pywwise.objects.abc import WwiseObject


class WwiseMeter(WwiseObject):  # TODO: add RTPC property once available
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect_wwise_meter.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WWISE_METER`.
    """
    apply_downstream_volume = WwiseProperty[bool]("ApplyDownstreamVolume", bool)
    attack_time = WwiseProperty[float]("AttackTime", float)
    hold = WwiseProperty[float]("Hold", float)
    infinite_hold = WwiseProperty[bool]("InfiniteHold", bool)
    max = WwiseProperty[float]("Max", float)
    meter_mode = WwiseProperty[EMeterMode]("MeterMode", EMeterMode)
    meter_scope = WwiseProperty[EMeterScope]("MeterScope", EMeterScope)
    min = WwiseProperty[float]("Min", float)
    release_time = WwiseProperty[float]("ReleaseTime", float)
