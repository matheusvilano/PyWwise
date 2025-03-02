# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EPitchShifterFilterType, EPitchShifterInput
from pywwise.objects.abc import WwiseObject


class WwisePitchShifter(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect_wwise_pitch_shifter.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WWISE_PITCH_SHIFTER`.
    """
    delay_time = WwiseProperty[float]("DelayTime", float)
    dry_level = WwiseProperty[float]("DryLevel", float)
    filter_frequency = WwiseProperty[float]("FilterFrequency", float)
    filter_gain = WwiseProperty[float]("FilterGain", float)
    filter_q = WwiseProperty[float]("FilterQFactor", float)
    filter_type = WwiseProperty[EPitchShifterFilterType]("FilterType", EPitchShifterFilterType)
    input = WwiseProperty[EPitchShifterInput]("Input", EPitchShifterInput)
    pitch = WwiseProperty[float]("Pitch", float)
    process_lfe = WwiseProperty[bool]("ProcessLFE", bool)
    sync_dry = WwiseProperty[bool]("SyncDry", bool)
    wet_level = WwiseProperty[float]("WetLevel", float)
