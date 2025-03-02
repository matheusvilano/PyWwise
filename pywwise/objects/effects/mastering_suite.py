# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise import EMasteringSuiteLinkMode
from pywwise.descriptors import WwiseProperty
from pywwise.enums import EMasteringSuiteFilterMode, EMasteringSuiteLimiterMode
from pywwise.objects.abc import WwiseObject


class MasteringSuite(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect_wwise_tremolo.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MASTERING_SUITE`.
    """
    compressor_band1_attack = WwiseProperty[float]("compressorBand1Attack", float)
    compressor_band1_enabled = WwiseProperty[bool]("compressorBand1Enabled", bool)
    compressor_band1_knee = WwiseProperty[float]("compressorBand1Knee", float)
    compressor_band1_makeup_gain = WwiseProperty[float]("compressorBand1MakeupGain", float)
    compressor_band1_ratio = WwiseProperty[float]("compressorBand1Ratio", float)
    compressor_band1_release = WwiseProperty[float]("compressorBand1Release", float)
    compressor_band1_threshold = WwiseProperty[float]("compressorBand1Threshold", float)
    compressor_band2_attack = WwiseProperty[float]("compressorBand2Attack", float)
    compressor_band2_enabled = WwiseProperty[bool]("compressorBand2Enabled", bool)
    compressor_band2_knee = WwiseProperty[float]("compressorBand2Knee", float)
    compressor_band2_makeup_gain = WwiseProperty[float]("compressorBand2MakeupGain", float)
    compressor_band2_ratio = WwiseProperty[float]("compressorBand2Ratio", float)
    compressor_band2_release = WwiseProperty[float]("compressorBand2Release", float)
    compressor_band2_threshold = WwiseProperty[float]("compressorBand2Threshold", float)
    compressor_band3_attack = WwiseProperty[float]("compressorBand3Attack", float)
    compressor_band3_enabled = WwiseProperty[bool]("compressorBand3Enabled", bool)
    compressor_band3_knee = WwiseProperty[float]("compressorBand3Knee", float)
    compressor_band3_makeup_gain = WwiseProperty[float]("compressorBand3MakeupGain", float)
    compressor_band3_ratio = WwiseProperty[float]("compressorBand3Ratio", float)
    compressor_band3_release = WwiseProperty[float]("compressorBand3Release", float)
    compressor_band3_threshold = WwiseProperty[float]("compressorBand3Threshold", float)
    compressor_band4_attack = WwiseProperty[float]("compressorBand4Attack", float)
    compressor_band4_enabled = WwiseProperty[bool]("compressorBand4Enabled", bool)
    compressor_band4_knee = WwiseProperty[float]("compressorBand4Knee", float)
    compressor_band4_makeup_gain = WwiseProperty[float]("compressorBand4MakeupGain", float)
    compressor_band4_ratio = WwiseProperty[float]("compressorBand4Ratio", float)
    compressor_band4_release = WwiseProperty[float]("compressorBand4Release", float)
    compressor_band4_threshold = WwiseProperty[float]("compressorBand4Threshold", float)
    compressor_crossover_frequency1 = WwiseProperty[float]("compressorCrossoverFrequency1", float)
    compressor_crossover_frequency2 = WwiseProperty[float]("compressorCrossoverFrequency2", float)
    compressor_crossover_frequency3 = WwiseProperty[float]("compressorCrossoverFrequency3", float)
    compressor_link_mode = WwiseProperty[EMasteringSuiteLinkMode]("compressorLinkMode", EMasteringSuiteLinkMode)
    compressor_link_stereo_pairs = WwiseProperty[bool]("compressorLinkStereoPairs", bool)
    compressor_link_strength = WwiseProperty[float]("compressorLinkStrength", float)
    compressor_num_bands = WwiseProperty[int]("compressorNumBands", int)
    limiter_attack = WwiseProperty[float]("limiterAttack", float)
    limiter_link_channels = WwiseProperty[bool]("limiterLinkChannels", bool)
    limiter_mode = WwiseProperty[EMasteringSuiteLimiterMode]("limiterMode", EMasteringSuiteLimiterMode)
    limiter_output_gain = WwiseProperty[float]("limiterOutputGain", float)
    limiter_release = WwiseProperty[float]("limiterRelease", float)
    limiter_threshold = WwiseProperty[float]("limiterThreshold", float)
    master_volume_channel1 = WwiseProperty[float]("masterVolumeChannel1", float)
    master_volume_channel2 = WwiseProperty[float]("masterVolumeChannel2", float)
    master_volume_channel3 = WwiseProperty[float]("masterVolumeChannel3", float)
    master_volume_channel4 = WwiseProperty[float]("masterVolumeChannel4", float)
    master_volume_channel5 = WwiseProperty[float]("masterVolumeChannel5", float)
    master_volume_channel6 = WwiseProperty[float]("masterVolumeChannel6", float)
    master_volume_channel7 = WwiseProperty[float]("masterVolumeChannel7", float)
    master_volume_channel8 = WwiseProperty[float]("masterVolumeChannel8", float)
    master_volume_channel9 = WwiseProperty[float]("masterVolumeChannel9", float)
    master_volume_channel10 = WwiseProperty[float]("masterVolumeChannel10", float)
    master_volume_channel11 = WwiseProperty[float]("masterVolumeChannel11", float)
    master_volume_channel12 = WwiseProperty[float]("masterVolumeChannel12", float)
    module_enable_compressor = WwiseProperty[bool]("moduleEnableCompressor", bool)
    module_enable_limiter = WwiseProperty[bool]("moduleEnableLimiter", bool)
    module_enable_master_volume = WwiseProperty[bool]("moduleEnableMasterVolume", bool)
    module_enable_param_eq = WwiseProperty[bool]("moduleEnableParamEQ", bool)
    param_band1_enabled = WwiseProperty[bool]("paramBand1Enabled", bool)
    param_band1_filter_mode = WwiseProperty[EMasteringSuiteFilterMode](
        "paramBand1FilterMode", EMasteringSuiteFilterMode)
    param_band1_frequency = WwiseProperty[float]("paramBand1Frequency", float)
    param_band1_gain = WwiseProperty[float]("paramBand1Gain", float)
    param_band1_resonance = WwiseProperty[float]("paramBand1Resonance", float)
    param_band2_enabled = WwiseProperty[bool]("paramBand2Enabled", bool)
    param_band2_filter_mode = WwiseProperty[EMasteringSuiteFilterMode](
        "paramBand2FilterMode", EMasteringSuiteFilterMode)
    param_band2_frequency = WwiseProperty[float]("paramBand2Frequency", float)
    param_band2_gain = WwiseProperty[float]("paramBand2Gain", float)
    param_band2_resonance = WwiseProperty[float]("paramBand2Resonance", float)
    param_band3_enabled = WwiseProperty[bool]("paramBand3Enabled", bool)
    param_band3_filter_mode = WwiseProperty[EMasteringSuiteFilterMode](
        "paramBand3FilterMode", EMasteringSuiteFilterMode)
    param_band3_frequency = WwiseProperty[float]("paramBand3Frequency", float)
    param_band3_gain = WwiseProperty[float]("paramBand3Gain", float)
    param_band3_resonance = WwiseProperty[float]("paramBand3Resonance", float)
    param_band4_enabled = WwiseProperty[bool]("paramBand4Enabled", bool)
    param_band4_filter_mode = WwiseProperty[EMasteringSuiteFilterMode](
        "paramBand4FilterMode", EMasteringSuiteFilterMode)
    param_band4_frequency = WwiseProperty[float]("paramBand4Frequency", float)
    param_band4_gain = WwiseProperty[float]("paramBand4Gain", float)
    param_band4_resonance = WwiseProperty[float]("paramBand4Resonance", float)
    param_band5_enabled = WwiseProperty[bool]("paramBand5Enabled", bool)
    param_band5_filter_mode = WwiseProperty[EMasteringSuiteFilterMode](
        "paramBand5FilterMode", EMasteringSuiteFilterMode)
    param_band5_frequency = WwiseProperty[float]("paramBand5Frequency", float)
    param_band5_gain = WwiseProperty[float]("paramBand5Gain", float)
    param_band5_resonance = WwiseProperty[float]("paramBand5Resonance", float)
    param_band6_enabled = WwiseProperty[bool]("paramBand6Enabled", bool)
    param_band6_filter_mode = WwiseProperty[EMasteringSuiteFilterMode](
        "paramBand6FilterMode", EMasteringSuiteFilterMode)
    param_band6_frequency = WwiseProperty[float]("paramBand6Frequency", float)
    param_band6_gain = WwiseProperty[float]("paramBand6Gain", float)
    param_band6_resonance = WwiseProperty[float]("paramBand6Resonance", float)
    param_eq_num_bands = WwiseProperty[int]("paramEqNumBands", int)
