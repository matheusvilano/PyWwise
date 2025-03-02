# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EModPhaseMode, EModWaveform
from pywwise.objects.abc import WwiseObject


class WwiseFlanger(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect_wwise_flanger.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WWISE_FLANGER`.
    """
    delay_time = WwiseProperty[float]("DelayTime", float)
    dry_level = WwiseProperty[float]("DryLevel", float)
    enable_lfo = WwiseProperty[bool]("EnableLFO", bool)
    feed_back_level = WwiseProperty[float]("FeedBackLevel", float)
    feed_forward_level = WwiseProperty[float]("FeedForwardLevel", float)
    mod_depth = WwiseProperty[float]("ModDepth", float)
    mod_frequency = WwiseProperty[float]("ModFrequency", float)
    mod_pwm = WwiseProperty[float]("ModPWM", float)
    mod_phase_mode = WwiseProperty[EModPhaseMode]("ModPhaseMode", EModPhaseMode)
    mod_phase_offset = WwiseProperty[float]("ModPhaseOffset", float)
    mod_phase_spread = WwiseProperty[float]("ModPhaseSpread", float)
    mod_smoothing = WwiseProperty[float]("ModSmoothing", float)
    mod_waveform = WwiseProperty[EModWaveform]("ModWaveform", EModWaveform)
    output_level = WwiseProperty[float]("OutputLevel", float)
    process_centre = WwiseProperty[bool]("ProcessCenter", bool)
    process_lfe = WwiseProperty[bool]("ProcessLFE", bool)
    wet_dry_mix = WwiseProperty[float]("WetDryMix", float)
