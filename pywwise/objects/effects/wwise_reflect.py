# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import (EReflectAlgorithm, EReflectChannelConfig, EReflectDecorrelationStrengthSource,
                           EReflectFilterType, EReflectThresholdMode)
from pywwise.objects.abc import WwiseObject


class WwiseReflect(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect_wwise_reflect.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WWISE_REFLECT`.
    """
    base_texture_frequency = WwiseProperty[float]("BaseTextureFrequency", float)
    centre_percentage = WwiseProperty[float]("CenterPerc", float)
    curve_usage_mask = WwiseProperty[int]("CurveUsageMask", int)
    decorrelation_algorithm = WwiseProperty[EReflectAlgorithm]("DecorrAlgorithmSelect", EReflectAlgorithm)
    decorrelation_filter_max_reflection_order = WwiseProperty[int]("DecorrFilterMaxReflectionOrder", int)
    decorrelation_hardware_acceleration = WwiseProperty[bool]("DecorrHardwareAcceleration", bool)
    decorrelation_strength = WwiseProperty[float]("DecorrStrength", float)
    decorrelation_strength_source = WwiseProperty[EReflectDecorrelationStrengthSource](
        "DecorrStrengthSource", EReflectDecorrelationStrengthSource)
    decorrelation_window_width = WwiseProperty[int]("DecorrWindowWidth", int)
    diffraction_warping = WwiseProperty[float]("DiffractionWarping", float)
    distance_threshold = WwiseProperty[float]("DistanceThreshold", float)
    distance_warping = WwiseProperty[float]("DistanceWarping", float)
    dry = WwiseProperty[float]("Dry", float)
    fade_time = WwiseProperty[float]("FadeTime", float)
    fusing_time = WwiseProperty[float]("FusingTime", float)
    material_filtering_select = WwiseProperty[EReflectAlgorithm]("MaterialFilteringSelect", EReflectAlgorithm)
    max_distance = WwiseProperty[float]("MaxDistance", float)
    max_reflections = WwiseProperty[float]("MaxReflections", float)
    output_channel_config = WwiseProperty[EReflectChannelConfig]("OutputChannelConfig", EReflectChannelConfig)
    param_filter_cutoff = WwiseProperty[float]("ParamFilterCutoff", float)
    param_filter_type = WwiseProperty[EReflectFilterType]("ParamFilterType", EReflectFilterType)
    pitch_threshold = WwiseProperty[float]("PitchThreshold", float)
    speed_of_sound = WwiseProperty[float]("SpeedOfSound", float)
    stereo_decorrelation = WwiseProperty[bool]("StereoDecorrelation", bool)
    threshold_mode = WwiseProperty[EReflectThresholdMode]("ThresholdMode", EReflectThresholdMode)
    wet = WwiseProperty[float]("Wet", float)
