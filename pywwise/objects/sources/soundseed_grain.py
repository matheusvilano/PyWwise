# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import (ESoundSeedGrainChannelConfig, ESoundSeedGrainDurationLink, ESoundSeedGrainEnvelopeType,
                           ESoundSeedGrainFilterType, ESoundSeedGrainFrequencyTime, ESoundSeedGrainPositioning,
                           ESoundSeedGrainQuantization, ESoundSeedGrainQuantizationSimple, ESoundSeedGrainSelection,
                           ESoundSeedGrainWaveform, ESoundSeedGrainWindowMode)
from pywwise.objects.abc import WwiseObject


class SoundSeedGrain(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_source_soundseed_grain.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SOURCE_PLUGIN`.
    """
    amplitude = WwiseProperty[float]("Amplitude", float)
    amplitude_mod1_depth = WwiseProperty[float]("AmplitudeMod1Depth", float)
    amplitude_mod1_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "AmplitudeMod1Quantization", ESoundSeedGrainQuantizationSimple)
    amplitude_mod2_depth = WwiseProperty[float]("AmplitudeMod2Depth", float)
    amplitude_mod2_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "AmplitudeMod2Quantization", ESoundSeedGrainQuantizationSimple)
    amplitude_mod3_depth = WwiseProperty[float]("AmplitudeMod3Depth", float)
    amplitude_mod3_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "AmplitudeMod3Quantization", ESoundSeedGrainQuantizationSimple)
    amplitude_mod4_depth = WwiseProperty[float]("AmplitudeMod4Depth", float)
    amplitude_mod4_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "AmplitudeMod4Quantization", ESoundSeedGrainQuantizationSimple)
    attack = WwiseProperty[float]("Attack", float)
    attack_mod1_depth = WwiseProperty[float]("AttackMod1Depth", float)
    attack_mod1_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "AttackMod1Quantization", ESoundSeedGrainQuantization)
    attack_mod2_depth = WwiseProperty[float]("AttackMod2Depth", float)
    attack_mod2_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "AttackMod2Quantization", ESoundSeedGrainQuantization)
    attack_mod3_depth = WwiseProperty[float]("AttackMod13Depth", float)
    attack_mod3_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "AttackMod3Quantization", ESoundSeedGrainQuantization)
    attack_mod4_depth = WwiseProperty[float]("AttackMod4Depth", float)
    attack_mod4_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "AttackMod4Quantization", ESoundSeedGrainQuantization)
    azimuth = WwiseProperty[float]("Azimuth", float)
    azimuth_mod1_depth = WwiseProperty[float]("AzimuthMod1Depth", float)
    azimuth_mod1_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "AzimuthMod1Quantization", ESoundSeedGrainQuantizationSimple)
    azimuth_mod2_depth = WwiseProperty[float]("AzimuthMod2Depth", float)
    azimuth_mod2_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "AzimuthMod2Quantization", ESoundSeedGrainQuantizationSimple)
    azimuth_mod3_depth = WwiseProperty[float]("AzimuthMod3Depth", float)
    azimuth_mod3_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "AzimuthMod3Quantization", ESoundSeedGrainQuantizationSimple)
    azimuth_mod4_depth = WwiseProperty[float]("AzimuthMod4Depth", float)
    azimuth_mod4_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "AzimuthMod4Quantization", ESoundSeedGrainQuantizationSimple)
    duration = WwiseProperty[float]("Duration", float)
    duration_link = WwiseProperty[ESoundSeedGrainDurationLink]("DurationLink", ESoundSeedGrainDurationLink)
    duration_mod1_depth = WwiseProperty[float]("DurationMod1Depth", float)
    duration_mod1_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "DurationMod1Quantization", ESoundSeedGrainQuantization)
    duration_mod2_depth = WwiseProperty[float]("DurationMod2Depth", float)
    duration_mod2_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "DurationMod2Quantization", ESoundSeedGrainQuantization)
    duration_mod3_depth = WwiseProperty[float]("DurationMod3Depth", float)
    duration_mod3_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "DurationMod3Quantization", ESoundSeedGrainQuantization)
    duration_mod4_depth = WwiseProperty[float]("DurationMod4Depth", float)
    duration_mod4_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "DurationMod4Quantization", ESoundSeedGrainQuantization)
    duration_multiplier = WwiseProperty[float]("DurationMultiplier", float)
    duration_multiplier_mod1_depth = WwiseProperty[float]("DurationMultiplierMod1Depth", float)
    duration_multiplier_mod1_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "DurationMultiplierMod1Quantization", ESoundSeedGrainQuantizationSimple)
    duration_multiplier_mod2_depth = WwiseProperty[float]("DurationMultiplierMod2Depth", float)
    duration_multiplier_mod2_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "DurationMultiplierMod2Quantization", ESoundSeedGrainQuantizationSimple)
    duration_multiplier_mod3_depth = WwiseProperty[float]("DurationMultiplierMod3Depth", float)
    duration_multiplier_mod3_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "DurationMultiplierMod3Quantization", ESoundSeedGrainQuantizationSimple)
    duration_multiplier_mod4_depth = WwiseProperty[float]("DurationMultiplierMod4Depth", float)
    duration_multiplier_mod4_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "DurationMultiplierMod4Quantization", ESoundSeedGrainQuantizationSimple)
    elevation = WwiseProperty[float]("Elevation", float)
    elevation_mod1_depth = WwiseProperty[float]("ElevationMod1Depth", float)
    elevation_mod1_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "ElevationMod1Quantization", ESoundSeedGrainQuantizationSimple)
    elevation_mod2_depth = WwiseProperty[float]("ElevationMod2Depth", float)
    elevation_mod2_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "ElevationMod2Quantization", ESoundSeedGrainQuantizationSimple)
    elevation_mod3_depth = WwiseProperty[float]("ElevationMod3Depth", float)
    elevation_mod3_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "ElevationMod3Quantization", ESoundSeedGrainQuantizationSimple)
    elevation_mod4_depth = WwiseProperty[float]("ElevationMod4Depth", float)
    elevation_mod4_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "ElevationMod4Quantization", ESoundSeedGrainQuantizationSimple)
    envelope_type = WwiseProperty[ESoundSeedGrainEnvelopeType]("EnvelopeType", ESoundSeedGrainEnvelopeType)
    filter_frequency = WwiseProperty[float]("FilterFreq", float)
    filter_frequency_mod1_depth = WwiseProperty[float]("FilterFreqMod1Depth", float)
    filter_frequency_mod1_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "FilterFreqMod1Quantization", ESoundSeedGrainQuantization)
    filter_frequency_mod2_depth = WwiseProperty[float]("FilterFreqMod2Depth", float)
    filter_frequency_mod2_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "FilterFreqMod2Quantization", ESoundSeedGrainQuantization)
    filter_frequency_mod3_depth = WwiseProperty[float]("FilterFreqMod3Depth", float)
    filter_frequency_mod3_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "FilterFreqMod3Quantization", ESoundSeedGrainQuantization)
    filter_frequency_mod4_depth = WwiseProperty[float]("FilterFreqMod4Depth", float)
    filter_frequency_mod4_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "FilterFreqMod4Quantization", ESoundSeedGrainQuantization)
    filter_q = WwiseProperty[float]("FilterQ", float)
    filter_q_mod1_depth = WwiseProperty[float]("FilterQMod1Depth", float)
    filter_q_mod1_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "FilterQMod1Quantization", ESoundSeedGrainQuantizationSimple)
    filter_q_mod2_depth = WwiseProperty[float]("FilterQMod2Depth", float)
    filter_q_mod2_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "FilterQMod2Quantization", ESoundSeedGrainQuantizationSimple)
    filter_q_mod3_depth = WwiseProperty[float]("FilterQMod3Depth", float)
    filter_q_mod3_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "FilterQMod3Quantization", ESoundSeedGrainQuantizationSimple)
    filter_q_mod4_depth = WwiseProperty[float]("FilterQMod4Depth", float)
    filter_q_mod4_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "FilterQMod4Quantization", ESoundSeedGrainQuantizationSimple)
    filter_type = WwiseProperty[ESoundSeedGrainFilterType]("FilterType", ESoundSeedGrainFilterType)
    grain_rate = WwiseProperty[float]("GrainRate", float)
    grain_rate_mod1_depth = WwiseProperty[float]("GrainRateMod1Depth", float)
    grain_rate_mod1_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "GrainRateMod1Quantization", ESoundSeedGrainQuantization)
    grain_rate_mod2_depth = WwiseProperty[float]("GrainRateMod2Depth", float)
    grain_rate_mod2_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "GrainRateMod2Quantization", ESoundSeedGrainQuantization)
    grain_rate_mod3_depth = WwiseProperty[float]("GrainRateMod3Depth", float)
    grain_rate_mod3_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "GrainRateMod3Quantization", ESoundSeedGrainQuantization)
    grain_rate_mod4_depth = WwiseProperty[float]("GrainRateMod4Depth", float)
    grain_rate_mod4_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "GrainRateMod4Quantization", ESoundSeedGrainQuantization)
    grain_time = WwiseProperty[float]("GrainTime", float)
    grain_time_mod1_depth = WwiseProperty[float]("GrainTimeMod1Depth", float)
    grain_time_mod1_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "GrainTimeMod1Quantization", ESoundSeedGrainQuantization)
    grain_time_mod2_depth = WwiseProperty[float]("GrainTimeMod2Depth", float)
    grain_time_mod2_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "GrainTimeMod2Quantization", ESoundSeedGrainQuantization)
    grain_time_mod3_depth = WwiseProperty[float]("GrainTimeMod3Depth", float)
    grain_time_mod3_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "GrainTimeMod3Quantization", ESoundSeedGrainQuantization)
    grain_time_mod4_depth = WwiseProperty[float]("GrainTimeMod4Depth", float)
    grain_time_mod4_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "GrainTimeMod4Quantization", ESoundSeedGrainQuantization)
    marker_select = WwiseProperty[float]("MarkerSelect", float)
    marker_select_mod1_depth = WwiseProperty[float]("MarkerSelectMod1Depth", float)
    marker_select_mod1_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "MarkerSelectMod1Quantization", ESoundSeedGrainQuantizationSimple)
    marker_select_mod2_depth = WwiseProperty[float]("MarkerSelectMod2Depth", float)
    marker_select_mod2_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "MarkerSelectMod2Quantization", ESoundSeedGrainQuantizationSimple)
    marker_select_mod3_depth = WwiseProperty[float]("MarkerSelectMod3Depth", float)
    marker_select_mod3_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "MarkerSelectMod3Quantization", ESoundSeedGrainQuantizationSimple)
    marker_select_mod4_depth = WwiseProperty[float]("MarkerSelectMod4Depth", float)
    marker_select_mod4_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "MarkerSelectMod4Quantization", ESoundSeedGrainQuantizationSimple)
    max_num_grains = WwiseProperty[int]("MaxNumGrains", int)
    midi_map_transpose = WwiseProperty[bool]("MidiMapTranspose", bool)
    mod_amount1 = WwiseProperty[float]("ModAmount1", float)
    mod_amount2 = WwiseProperty[float]("ModAmount2", float)
    mod_amount3 = WwiseProperty[float]("ModAmount3", float)
    mod_amount4 = WwiseProperty[float]("ModAmount4", float)
    mod_period1 = WwiseProperty[float]("ModPeriod1", float)
    mod_period2 = WwiseProperty[float]("ModPeriod2", float)
    mod_period3 = WwiseProperty[float]("ModPeriod3", float)
    mod_period4 = WwiseProperty[float]("ModPeriod4", float)
    mod_rate1 = WwiseProperty[float]("ModRate1", float)
    mod_rate2 = WwiseProperty[float]("ModRate2", float)
    mod_rate3 = WwiseProperty[float]("ModRate3", float)
    mod_rate4 = WwiseProperty[float]("ModRate4", float)
    mod_select1 = WwiseProperty[ESoundSeedGrainSelection]("ModSelect1", ESoundSeedGrainSelection)
    mod_select2 = WwiseProperty[ESoundSeedGrainSelection]("ModSelect2", ESoundSeedGrainSelection)
    mod_select3 = WwiseProperty[ESoundSeedGrainSelection]("ModSelect3", ESoundSeedGrainSelection)
    mod_select4 = WwiseProperty[ESoundSeedGrainSelection]("ModSelect4", ESoundSeedGrainSelection)
    mod_waveform1 = WwiseProperty[ESoundSeedGrainWaveform]("ModWaveform1", ESoundSeedGrainWaveform)
    mod_waveform2 = WwiseProperty[ESoundSeedGrainWaveform]("ModWaveform2", ESoundSeedGrainWaveform)
    mod_waveform3 = WwiseProperty[ESoundSeedGrainWaveform]("ModWaveform3", ESoundSeedGrainWaveform)
    mod_waveform4 = WwiseProperty[ESoundSeedGrainWaveform]("ModWaveform4", ESoundSeedGrainWaveform)
    offset = WwiseProperty[float]("Offset", float)
    offset_mod1_depth = WwiseProperty[float]("OffsetMod1Depth", float)
    offset_mod1_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "OffsetMod1Quantization", ESoundSeedGrainQuantizationSimple)
    offset_mod2_depth = WwiseProperty[float]("OffsetMod2Depth", float)
    offset_mod2_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "OffsetMod2Quantization", ESoundSeedGrainQuantizationSimple)
    offset_mod3_depth = WwiseProperty[float]("OffsetMod3Depth", float)
    offset_mod3_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "OffsetMod3Quantization", ESoundSeedGrainQuantizationSimple)
    offset_mod4_depth = WwiseProperty[float]("OffsetMod4Depth", float)
    offset_mod4_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "OffsetMod4Quantization", ESoundSeedGrainQuantizationSimple)
    output_channel_config = WwiseProperty[ESoundSeedGrainChannelConfig](
        "OutputChannelConfig", ESoundSeedGrainChannelConfig)
    output_level = WwiseProperty[float]("OutputLevel", float)
    positioning_select = WwiseProperty[ESoundSeedGrainPositioning]("PositioningSelect", ESoundSeedGrainPositioning)
    quantize_to_markers = WwiseProperty[bool]("QuantizeToMarkers", bool)
    release = WwiseProperty[float]("Release", float)
    release_mod1_depth = WwiseProperty[float]("ReleaseMod1Depth", float)
    release_mod1_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "ReleaseMod1Quantization", ESoundSeedGrainQuantization)
    release_mod2_depth = WwiseProperty[float]("ReleaseMod2Depth", float)
    release_mod2_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "ReleaseMod2Quantization", ESoundSeedGrainQuantization)
    release_mod3_depth = WwiseProperty[float]("ReleaseMod3Depth", float)
    release_mod3_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "ReleaseMod3Quantization", ESoundSeedGrainQuantization)
    release_mod4_depth = WwiseProperty[float]("ReleaseMod4Depth", float)
    release_mod4_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "ReleaseMod4Quantization", ESoundSeedGrainQuantization)
    select_frequency_time_grain = WwiseProperty[ESoundSeedGrainFrequencyTime](
        "SelectFreqTimeGrain", ESoundSeedGrainFrequencyTime)
    speed = WwiseProperty[float]("Speed", float)
    speed_mod1_depth = WwiseProperty[float]("SpeedMod1Depth", float)
    speed_mod1_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "SpeedMod1Quantization", ESoundSeedGrainQuantizationSimple)
    speed_mod2_depth = WwiseProperty[float]("SpeedMod2Depth", float)
    speed_mod2_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "SpeedMod2Quantization", ESoundSeedGrainQuantizationSimple)
    speed_mod3_depth = WwiseProperty[float]("SpeedMod3Depth", float)
    speed_mod3_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "SpeedMod3Quantization", ESoundSeedGrainQuantizationSimple)
    speed_mod4_depth = WwiseProperty[float]("SpeedMod4Depth", float)
    speed_mod4_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "SpeedMod4Quantization", ESoundSeedGrainQuantizationSimple)
    spread = WwiseProperty[float]("Spread", float)
    spread_mod1_depth = WwiseProperty[float]("SpreadMod1Depth", float)
    spread_mod1_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "SpreadMod1Quantization", ESoundSeedGrainQuantizationSimple)
    spread_mod2_depth = WwiseProperty[float]("SpreadMod2Depth", float)
    spread_mod2_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "SpreadMod2Quantization", ESoundSeedGrainQuantizationSimple)
    spread_mod3_depth = WwiseProperty[float]("SpreadMod3Depth", float)
    spread_mod3_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "SpreadMod3Quantization", ESoundSeedGrainQuantizationSimple)
    spread_mod4_depth = WwiseProperty[float]("SpreadMod4Depth", float)
    spread_mod4_quantization = WwiseProperty[ESoundSeedGrainQuantizationSimple](
        "SpreadMod4Quantization", ESoundSeedGrainQuantizationSimple)
    transpose = WwiseProperty[float]("Transpose", float)
    transpose_mod1_depth = WwiseProperty[float]("TransposeMod1Depth", float)
    transpose_mod1_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "TransposeMod1Quantization", ESoundSeedGrainQuantization)
    transpose_mod2_depth = WwiseProperty[float]("TransposeMod2Depth", float)
    transpose_mod2_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "TransposeMod2Quantization", ESoundSeedGrainQuantization)
    transpose_mod3_depth = WwiseProperty[float]("TransposeMod3Depth", float)
    transpose_mod3_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "TransposeMod3Quantization", ESoundSeedGrainQuantization)
    transpose_mod4_depth = WwiseProperty[float]("TransposeMod4Depth", float)
    transpose_mod4_quantization = WwiseProperty[ESoundSeedGrainQuantization](
        "TransposeMod4Quantization", ESoundSeedGrainQuantization)
    transpose_root = WwiseProperty[int]("TransposeRoot", int)
    window_mode = WwiseProperty[ESoundSeedGrainWindowMode]("WindowMode", ESoundSeedGrainWindowMode)
