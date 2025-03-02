# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.enums import ESoundSeedAirChannelMask, ENoiseColour
from pywwise.descriptors import WwiseProperty
from pywwise.objects.abc import WwiseObject


class SoundSeedAirWoosh(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_source_soundseed_air_woosh.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SOURCE_PLUGIN`.
    """
    attenuation_roll_of = WwiseProperty[float]("AttenuationRollOff", float)
    channel_mask = WwiseProperty[ESoundSeedAirChannelMask]("ChannelMask", ESoundSeedAirChannelMask)
    distance_attenuation = WwiseProperty[bool]("DistanceAttenuation", bool)
    duration = WwiseProperty[float]("Duration", float)
    duration_random = WwiseProperty[float]("DurationRandom", float)
    frequency_scale = WwiseProperty[float]("FrequencyScale", float)
    frequency_scale_automate = WwiseProperty[bool]("FrequencyScaleAutomate", bool)
    frequency_scale_random = WwiseProperty[float]("FrequencyScaleRandom", float)
    gain_offset = WwiseProperty[float]("GainOffset", float)
    gain_offset_automate = WwiseProperty[bool]("GainOffsetAutomate", bool)
    gain_offset_random = WwiseProperty[float]("GainOffsetRandom", float)
    min_distance = WwiseProperty[float]("MinDistance", float)
    noise_colour = WwiseProperty[ENoiseColour]("NoiseColour", ENoiseColour)
    oversampling = WwiseProperty[int]("Oversampling", int)
    playback_rate = WwiseProperty[float]("PlaybackRate", float)
    q_factor_scale = WwiseProperty[float]("QFactorScale", float)
    q_factor_scale_automate = WwiseProperty[bool]("QFactorScaleAutomate", bool)
    q_factor_scale_random = WwiseProperty[float]("QFactorScaleRandom", float)
    speed = WwiseProperty[float]("Speed", float)
    speed_automate = WwiseProperty[bool]("SpeedAutomate", bool)
    speed_point_speed_random = WwiseProperty[float]("SpeedPointSpeedRandom", float)
    speed_point_time_random = WwiseProperty[float]("SpeedPointTimeRandom", float)
    speed_random = WwiseProperty[float]("SpeedRandom", float)
    velocity_dynamic_range = WwiseProperty[float]("VelocityDynamicRange", float)
