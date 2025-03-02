# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EToneGenChannelMask, EToneGenDurationMode, EToneGenSweepFrequencyType, EToneGenWaveform
from pywwise.objects.abc import WwiseObject


class WwiseToneGenerator(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_source_wwise_tone_generator.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SOURCE_PLUGIN`.
    """
    attack_time = WwiseProperty[float]("AttackTime", float)
    channel_mask = WwiseProperty[EToneGenChannelMask]("ChannelMask", EToneGenChannelMask)
    decay_time = WwiseProperty[float]("DecayTime", float)
    duration_mode = WwiseProperty[EToneGenDurationMode]("DurMode", EToneGenDurationMode)
    release_time = WwiseProperty[float]("ReleaseTime", float)
    start_frequency = WwiseProperty[float]("StartFreq", float)
    start_frequency_random_max = WwiseProperty[float]("StartFreqRandMax", float)
    start_frequency_random_min = WwiseProperty[float]("StartFreqRandMin", float)
    stop_frequency = WwiseProperty[float]("StopFreq", float)
    stop_frequency_random_max = WwiseProperty[float]("StopFreqRandMax", float)
    stop_frequency_random_min = WwiseProperty[float]("StopFreqRandMin", float)
    sustain_level = WwiseProperty[float]("SustainLevel", float)
    sustian_time = WwiseProperty[float]("SustainTime", float)
    sweep_frequency = WwiseProperty[float]("SweepFreq", float)
    sweep_frequency_type = WwiseProperty[EToneGenSweepFrequencyType]("SweepFreqType", EToneGenSweepFrequencyType)
    wave_gain = WwiseProperty[float]("WaveGain", float)
    wave_type = WwiseProperty[EToneGenWaveform]("WaveType", EToneGenWaveform)
