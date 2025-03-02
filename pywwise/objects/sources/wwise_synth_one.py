# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EFrequencyMode, ENoiseColour, ESynthOneOperationMode, ESynthOneWaveform
from pywwise.objects.abc import WwiseObject


class WwiseSynthOne(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_source_wwise_synth_one.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SOURCE_PLUGIN`.
    """
    base_frequency = WwiseProperty[float]("BaseFrequency", float)
    fm_amount = WwiseProperty[float]("FMAmount", float)
    frequency_mode = WwiseProperty[EFrequencyMode]("FrequencyMode", EFrequencyMode)
    noise_level = WwiseProperty[ENoiseColour]("NoiseLevel", ENoiseColour)
    noise_shape = WwiseProperty[float]("NoiseShape", float)
    operation_mode = WwiseProperty[ESynthOneOperationMode]("OperationMode", ESynthOneOperationMode)
    osc1_invert = WwiseProperty[bool]("Osc1Invert", bool)
    osc1_level = WwiseProperty[float]("Osc1Level", float)
    osc1_pwm = WwiseProperty[float]("Osc1Pwm", float)
    osc1_transpose = WwiseProperty[float]("Osc1Transpose", float)
    osc1_waveform = WwiseProperty[ESynthOneWaveform]("Osc1Waveform", ESynthOneWaveform)
    osc2_invert = WwiseProperty[bool]("Osc2Invert", bool)
    osc2_level = WwiseProperty[float]("Osc2Level", float)
    osc2_pwm = WwiseProperty[float]("Osc2Pwm", float)
    osc2_transpose = WwiseProperty[float]("Osc2Transpose", float)
    osc2_waveform = WwiseProperty[ESynthOneWaveform]("Osc2Waveform", ESynthOneWaveform)
    output_level = WwiseProperty[float]("OutputLevel", float)
    oversampling = WwiseProperty[bool]("Oversampling", bool)
