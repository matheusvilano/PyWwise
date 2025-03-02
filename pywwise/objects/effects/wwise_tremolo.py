# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import ETremoloPhaseMode, ETremoloWaveform
from pywwise.objects.abc import WwiseObject


class WwiseTremolo(WwiseObject):
    """
     \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WWISE_TREMOLO`.
    """
    mod_depth = WwiseProperty[float]("ModDepth", float)
    mod_frequency = WwiseProperty[float]("ModFrequency", float)
    mod_pwm = WwiseProperty[float]("ModPWM", float)
    mod_phase_mode = WwiseProperty[ETremoloPhaseMode]("ModPhaseMode", ETremoloPhaseMode)
    mod_phase_offset = WwiseProperty[float]("ModPhaseOffset", float)
    mod_phase_spread = WwiseProperty[float]("ModPhaseSpread", float)
    mod_smoothing = WwiseProperty[float]("ModSmoothing", float)
    mod_waveform = WwiseProperty[ETremoloWaveform]("ModWaveform", ETremoloWaveform)
    output_gain = WwiseProperty[float]("OutputGain", float)
    process_centrering = WwiseProperty[bool]("ProcessCenter", bool)
    process_lfe = WwiseProperty[bool]("ProcessLFE", bool)
