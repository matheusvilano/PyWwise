# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EGuitarDistortionType, EGuitarDistortionFilterType
from pywwise.objects.abc import WwiseObject


class WwiseGuitarDistortion(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect_wwise_guitar_distortion.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WWISE_GUITAR_DISTORTION`.
    """
    distortion_drive = WwiseProperty[float]("DistortionDrive", float)
    distortion_tone = WwiseProperty[float]("DistortionTone", float)
    distortion_type = WwiseProperty[EGuitarDistortionType]("DistortionType", EGuitarDistortionType)
    output_level = WwiseProperty[float]("OutputLevel", float)
    post_eq_band1_enable = WwiseProperty[bool]("PostEQBand1Enable", bool)
    post_eq_band1_type = WwiseProperty[EGuitarDistortionFilterType]("PostEQBand1FilterType", EGuitarDistortionFilterType)
    post_eq_band1_frequency = WwiseProperty[float]("PostEQBand1Frequency", float)
    post_eq_band1_gain = WwiseProperty[float]("PostEQBand1Gain", float)
    post_eq_band1_q = WwiseProperty[float]("PostEQBand1QFactor", float)
    post_eq_band2_enable = WwiseProperty[bool]("PostEQBand2Enable", bool)
    post_eq_band2_type = WwiseProperty[EGuitarDistortionFilterType]("PostEQBand2FilterType", EGuitarDistortionFilterType)
    post_eq_band2_frequency = WwiseProperty[float]("PostEQBand2Frequency", float)
    post_eq_band2_gain = WwiseProperty[float]("PostEQBand2Gain", float)
    post_eq_band2_q = WwiseProperty[float]("PostEQBand2QFactor", float)
    post_eq_band3_enable = WwiseProperty[bool]("PostEQBand3Enable", bool)
    post_eq_band3_type = WwiseProperty[EGuitarDistortionFilterType]("PostEQBand3FilterType", EGuitarDistortionFilterType)
    post_eq_band3_frequency = WwiseProperty[float]("PostEQBand3Frequency", float)
    post_eq_band3_gain = WwiseProperty[float]("PostEQBand3Gain", float)
    post_eq_band3_q = WwiseProperty[float]("PostEQBand3QFactor", float)
    pre_eq_band1_enable = WwiseProperty[bool]("PreEQBand1Enable", bool)
    pre_eq_band1_type = WwiseProperty[EGuitarDistortionFilterType]("PreEQBand1FilterType", EGuitarDistortionFilterType)
    pre_eq_band1_frequency = WwiseProperty[float]("PreEQBand1Frequency", float)
    pre_eq_band1_gain = WwiseProperty[float]("PreEQBand1Gain", float)
    pre_eq_band1_q = WwiseProperty[float]("PreEQBand1QFactor", float)
    pre_eq_band2_enable = WwiseProperty[bool]("PreEQBand2Enable", bool)
    pre_eq_band2_type = WwiseProperty[EGuitarDistortionFilterType]("PreEQBand2FilterType", EGuitarDistortionFilterType)
    pre_eq_band2_frequency = WwiseProperty[float]("PreEQBand2Frequency", float)
    pre_eq_band2_gain = WwiseProperty[float]("PreEQBand2Gain", float)
    pre_eq_band2_q = WwiseProperty[float]("PreEQBand2QFactor", float)
    pre_eq_band3_enable = WwiseProperty[bool]("PreEQBand3Enable", bool)
    pre_eq_band3_type = WwiseProperty[EGuitarDistortionFilterType]("PreEQBand3FilterType", EGuitarDistortionFilterType)
    pre_eq_band3_frequency = WwiseProperty[float]("PreEQBand3Frequency", float)
    pre_eq_band3_gain = WwiseProperty[float]("PreEQBand3Gain", float)
    pre_eq_band3_q = WwiseProperty[float]("PreEQBand3QFactor", float)
    rectification = WwiseProperty[float]("Rectification", float)
    wet_dry_mix = WwiseProperty[float]("WetDryMix", float)
    