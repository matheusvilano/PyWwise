# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EMatrixReverbDelayCount, EMatrixReverbDelayLengthsMode
from pywwise.objects.abc import WwiseObject


class WwiseMatrixReverb(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect_wwise_matrix_reverb.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WWISE_MATRIX_REVERB`.
    """
    delay_lengths_mode = WwiseProperty[EMatrixReverbDelayLengthsMode]("DelayLengthsMode", EMatrixReverbDelayLengthsMode)
    delay_time_1 = WwiseProperty[float]("DelayTime1", float)
    delay_time_2 = WwiseProperty[float]("DelayTime2", float)
    delay_time_3 = WwiseProperty[float]("DelayTime3", float)
    delay_time_4 = WwiseProperty[float]("DelayTime4", float)
    delay_time_5 = WwiseProperty[float]("DelayTime5", float)
    delay_time_6 = WwiseProperty[float]("DelayTime6", float)
    delay_time_7 = WwiseProperty[float]("DelayTime7", float)
    delay_time_8 = WwiseProperty[float]("DelayTime8", float)
    delay_time_9 = WwiseProperty[float]("DelayTime9", float)
    delay_time_10 = WwiseProperty[float]("DelayTime10", float)
    delay_time_11 = WwiseProperty[float]("DelayTime11", float)
    delay_time_12 = WwiseProperty[float]("DelayTime12", float)
    delay_time_13 = WwiseProperty[float]("DelayTime13", float)
    delay_time_14 = WwiseProperty[float]("DelayTime14", float)
    delay_time_15 = WwiseProperty[float]("DelayTime15", float)
    delay_time_16 = WwiseProperty[float]("DelayTime16", float)
    dry_level = WwiseProperty[float]("DryLevel", float)
    hf_ratio = WwiseProperty[float]("HFRatio", float)
    number_of_delays = WwiseProperty[EMatrixReverbDelayCount]("NumberOfDelays", EMatrixReverbDelayCount)
    pre_delay = WwiseProperty[float]("PreDelay", float)
    process_lfe = WwiseProperty[bool]("ProcessLFE", bool)
    reverb_time = WwiseProperty[float]("ReverbTime", float)
    wet_level = WwiseProperty[float]("WetLevel", float)
