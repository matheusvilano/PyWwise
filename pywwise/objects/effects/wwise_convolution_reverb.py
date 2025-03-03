# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import (EConvolutionReverbAlgorithm, EConvolutionReverbBlockSize,
                           EConvolutionReverbIrChannelSelection, EConvolutionReverbIrLpfSlope, ESpeakerBitMask)
from pywwise.objects.abc import WwiseObject


class WwiseConvolutionReverb(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect_wwise_convolution_reverb.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WWISE_CONVOLUTION_REVERB`.
    """
    algo_type_select = WwiseProperty[EConvolutionReverbAlgorithm]("AlgoTypeSelect", EConvolutionReverbAlgorithm)
    centre_level = WwiseProperty[float]("CenterLevel", float)
    channel_config_override = WwiseProperty[ESpeakerBitMask]("ChannelConfigOverride", ESpeakerBitMask)
    dry_level = WwiseProperty[float]("DryLevel", float)
    front_level = WwiseProperty[float]("FrontLevel", float)
    front_rear_delay = WwiseProperty[float]("FrontRearDelay", float)
    full_precision_media = WwiseProperty[bool]("FullPrecisionMedia", bool)
    hardware_acceleration = WwiseProperty[bool]("HardwareAcceleration", bool)
    ir_channel_selection = WwiseProperty[EConvolutionReverbIrChannelSelection](
        "IRChannelSelect", EConvolutionReverbIrChannelSelection)
    ir_convolution_smooth = WwiseProperty[float]("IRConvolutionSmooth", float)
    ir_convolution_smooth_max = WwiseProperty[float]("IRConvolutionSmoothMax", float)
    ir_convolution_start = WwiseProperty[float]("IRConvolutionStart", float)
    ir_convolution_stop = WwiseProperty[float]("IRConvolutionStop", float)
    ir_convolution_threshold = WwiseProperty[float]("IRConvolutionThreshold", float)
    ir_graphic_eq_automate = WwiseProperty[bool]("IRGraphicEQAutomate", bool)
    ir_lpf_automate = WwiseProperty[bool]("IRLPFAutomate", bool)
    ir_lpf_slope = WwiseProperty[EConvolutionReverbIrLpfSlope]("IRLPFSlope", EConvolutionReverbIrLpfSlope)
    ir_lr_mix = WwiseProperty[float]("IRLRMix", float)
    ir_level = WwiseProperty[float]("IRLevel", float)
    ir_level_automate = WwiseProperty[bool]("IRLevelAutomate", bool)
    ir_stretch = WwiseProperty[float]("IRStretch", float)
    input_centre_level = WwiseProperty[float]("InputCenterLevel", float)
    input_lfe_level = WwiseProperty[float]("InputLFELevel", float)
    input_stereo_width = WwiseProperty[float]("InputStereoWidth", float)
    input_threshold = WwiseProperty[float]("InputThreshold", float)
    lfe_level = WwiseProperty[float]("LFELevel", float)
    pre_delay = WwiseProperty[float]("PreDelay", float)
    rear_level = WwiseProperty[float]("RearLevel", float)
    sound_engine_block_size = WwiseProperty[EConvolutionReverbBlockSize](
        "SoundEngineBlockSize", EConvolutionReverbBlockSize)
    sound_engine_sample_rate_default = WwiseProperty[int]("SoundEngineSampleRateDefault", int)
    sound_engine_sample_rate_mac = WwiseProperty[int]("SoundEngineSampleRateMac", int)
    sound_engine_sample_rate_ios = WwiseProperty[int]("SoundEngineSampleRateiOS", int)
    stereo_width = WwiseProperty[float]("StereoWidth", float)
    wet_level = WwiseProperty[float]("WetLevel", float)
