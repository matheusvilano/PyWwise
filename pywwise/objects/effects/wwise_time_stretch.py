# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import ETimeStretchMode, ETimeStretchStereoProcessing
from pywwise.objects.abc import WwiseObject


class WwiseTimeStretch(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect_wwise_time_stretch.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WWISE_TIME_STRETCH`.
    """
    output_gain = WwiseProperty[float]("OutputGain", float)
    pitch_shift = WwiseProperty[float]("PitchShift", float)
    pitch_shift_random = WwiseProperty[float]("PitchShiftRandom", float)
    quality = WwiseProperty[float]("Quality", float)
    stretch_mode = WwiseProperty[ETimeStretchMode]("QualityEnable", ETimeStretchMode)
    stereo_processing = WwiseProperty[ETimeStretchStereoProcessing]("StereoProcessing", ETimeStretchStereoProcessing)
    time_stretch = WwiseProperty[float]("TimeStretch", float)
    time_stretch_random = WwiseProperty[float]("TimeStretchRandom", float)
    window_size = WwiseProperty[int]("WindowSize", int)
