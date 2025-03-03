# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import ERoomVerbFilterType, ERoomVerbInsertPosition
from pywwise.objects.abc import WwiseObject


class WwiseRoomVerb(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect_wwise_roomverb.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WWISE_ROOMVERB`.
    """
    centre_level = WwiseProperty[float]("CenterLevel", float)
    dc_filter_cutoff_frequency = WwiseProperty[float]("DCFilterCutFreq", float)
    decay_time = WwiseProperty[float]("DecayTime", float)
    density = WwiseProperty[float]("Density", float)
    density_delay_max = WwiseProperty[float]("DensityDelayMax", float)
    density_delay_min = WwiseProperty[float]("DensityDelayMin", float)
    density_delay_rdm_percentage = WwiseProperty[float]("DensityDelayRdmPerc	", float)
    diffusion = WwiseProperty[float]("Diffusion", float)
    diffusion_delay_max = WwiseProperty[float]("DiffusionDelayMax", float)
    diffusion_delay_rdm_percentage = WwiseProperty[float]("DiffusionDelayRdmPerc", float)
    diffusion_delay_scale_percentage = WwiseProperty[float]("DiffusionDelayScalePerc", float)
    dry_level = WwiseProperty[float]("DryLevel", float)
    early_reflections_front_back_delay = WwiseProperty[float]("ERFrontBackDelay", float)
    early_reflections_level = WwiseProperty[float]("ERLevel", float)
    early_reflections_pattern = WwiseProperty[int]("ERPattern", int)
    enable_early_reflections = WwiseProperty[bool]("EnableEarlyReflections", bool)
    enable_tone_controls = WwiseProperty[bool]("EnableToneControls", bool)
    filter1_curve = WwiseProperty[ERoomVerbFilterType]("Filter1Curve", ERoomVerbFilterType)
    filter1_frequency = WwiseProperty[float]("Filter1Freq", float)
    filter1_gain = WwiseProperty[float]("Filter1Gain", float)
    filter1_insert_position = WwiseProperty[ERoomVerbInsertPosition]("Filter1InsertPos", ERoomVerbInsertPosition)
    filter1_q = WwiseProperty[float]("Filter1Q", float)
    filter2_curve = WwiseProperty[ERoomVerbFilterType]("Filter2Curve", ERoomVerbFilterType)
    filter2_frequency = WwiseProperty[float]("Filter2Freq", float)
    filter2_gain = WwiseProperty[float]("Filter2Gain", float)
    filter2_insert_position = WwiseProperty[ERoomVerbInsertPosition]("Filter2InsertPos", ERoomVerbInsertPosition)
    filter2_q = WwiseProperty[float]("Filter2Q", float)
    filter3_curve = WwiseProperty[ERoomVerbFilterType]("Filter3Curve", ERoomVerbFilterType)
    filter3_frequency = WwiseProperty[float]("Filter3Freq", float)
    filter3_gain = WwiseProperty[float]("Filter3Gain", float)
    filter3_insert_position = WwiseProperty[ERoomVerbInsertPosition]("Filter3InsertPos", ERoomVerbInsertPosition)
    filter3_q = WwiseProperty[float]("Filter3Q", float)
    front_level = WwiseProperty[float]("FrontLevel", float)
    high_frequency_damping = WwiseProperty[float]("HFDamping", float)
    input_centre_level = WwiseProperty[float]("InputCenterLevel", float)
    input_lfe_level = WwiseProperty[float]("InputLFELevel", float)
    lfe_level = WwiseProperty[float]("LFELevel", float)
    pre_delay = WwiseProperty[float]("PreDelay", float)
    quality = WwiseProperty[int]("Quality", int)
    rear_level = WwiseProperty[float]("RearLevel", float)
    reverb_level = WwiseProperty[float]("ReverbLevel", float)
    reverb_unit_input_delay = WwiseProperty[float]("ReverbUnitInputDelay", float)
    reverb_unit_input_delay_rmd_percentage = WwiseProperty[float]("ReverbUnitInputDelayRmdPerc", float)
    room_shape = WwiseProperty[float]("RoomShape", float)
    room_shape_max = WwiseProperty[float]("RoomShapeMax", float)
    room_shape_min = WwiseProperty[float]("RoomShapeMin", float)
    room_size = WwiseProperty[float]("RoomSize", float)
    stereo_width = WwiseProperty[float]("StereoWidth", float)
