# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.enums import ESoundSeedAirChannelMask
from pywwise.descriptors import WwiseProperty
from pywwise.objects.abc import WwiseObject


class SoundSeedAirWind(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_source_soundseed_air_wind.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SOURCE_PLUGIN`.
    """
    attenuation_roll_of = WwiseProperty[float]("AttenuationRollOff", float)
    average_velocity = WwiseProperty[float]("AverageVelocity", float)
    average_velocity_automate = WwiseProperty[bool]("AverageVelocityAutomate", bool)
    average_velocity_random = WwiseProperty[float]("AverageVelocityRandom", float)
    channel_mask = WwiseProperty[ESoundSeedAirChannelMask]("ChannelMask", ESoundSeedAirChannelMask)
    direction = WwiseProperty[float]("Direction", float)
    direction_automate = WwiseProperty[bool]("DirectionAutomate", bool)
    direction_random = WwiseProperty[float]("DirectionRandom", float)
    duration = WwiseProperty[float]("Duration", float)
    duration_random = WwiseProperty[float]("DurationRandom", float)
    frequency_scale = WwiseProperty[float]("FrequencyScale", float)
    frequency_scale_automate = WwiseProperty[bool]("FrequencyScaleAutomate", bool)
    frequency_scale_random = WwiseProperty[float]("FrequencyScaleRandom", float)
    gain_offset = WwiseProperty[float]("GainOffset", float)
    gain_offset_automate = WwiseProperty[bool]("GainOffsetAutomate", bool)
    gain_offset_random = WwiseProperty[float]("GainOffsetRandom", float)
    gustiness = WwiseProperty[float]("Gustiness", float)
    gustiness_automate = WwiseProperty[bool]("GustinessAutomate", bool)
    gustiness_random = WwiseProperty[float]("GustinessRandom", float)
    max_distance = WwiseProperty[float]("MaxDistance", float)
    min_distance = WwiseProperty[float]("MinDistance", float)
    playback_rate = WwiseProperty[float]("PlaybackRate", float)
    q_factor_scale = WwiseProperty[float]("QFactorScale", float)
    q_factor_scale_automate = WwiseProperty[bool]("QFactorScaleAutomate", bool)
    q_factor_scale_random = WwiseProperty[float]("QFactorScaleRandom", float)
    variability = WwiseProperty[float]("Variability", float)
    variability_automate = WwiseProperty[bool]("VariabilityAutomate", bool)
    variability_random = WwiseProperty[float]("VariabilityRandom", float)
    velocity_dynamic_range = WwiseProperty[float]("VelocityDynamicRange", float)
