# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EHarmonizerFilterType, EHarmonizerInput
from pywwise.objects.abc import WwiseObject


class WwiseHarmonizer(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect_wwise_harmonizer.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WWISE_HARMONIZER`.
    """
    dry_level = WwiseProperty[float]("DryLevel", float)
    input_format = WwiseProperty[EHarmonizerInput]("Input", EHarmonizerInput)
    process_lfe = WwiseProperty[bool]("ProcessLFE", bool)
    sync_dry = WwiseProperty[bool]("SyncDry", bool)
    voice1_enable = WwiseProperty[bool]("Voice1Enable", bool)
    voice1_filter_frequency = WwiseProperty[float]("Voice1FilterFrequency", float)
    voice1_filter_gain = WwiseProperty[float]("Voice1FilterGain", float)
    voice1_filter_q = WwiseProperty[float]("Voice1FilterQFactor", float)
    voice1_filter_type = WwiseProperty[EHarmonizerFilterType]("Voice1FilterType", EHarmonizerFilterType)
    voice1_gain = WwiseProperty[float]("Voice1Gain", float)
    voice1_pitch = WwiseProperty[float]("Voice1Pitch", float)
    voice2_enable = WwiseProperty[bool]("Voice2Enable", bool)
    voice2_filter_frequency = WwiseProperty[float]("Voice2FilterFrequency", float)
    voice2_filter_gain = WwiseProperty[float]("Voice2FilterGain", float)
    voice2_filter_q = WwiseProperty[float]("Voice2FilterQFactor", float)
    voice2_filter_type = WwiseProperty[EHarmonizerFilterType]("Voice2FilterType", EHarmonizerFilterType)
    voice2_gain = WwiseProperty[float]("Voice2Gain", float)
    voice2_pitch = WwiseProperty[float]("Voice2Pitch", float)
    wet_level = WwiseProperty[float]("WetLevel", float)
    window_size = WwiseProperty[int]("WindowSize", int)
