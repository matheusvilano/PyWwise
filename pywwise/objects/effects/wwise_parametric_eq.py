# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EParametricEqFilterType
from pywwise.objects.abc import WwiseObject


class WwiseParametricEq(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_effect_wwise_parametric_eq.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WWISE_PARAMETRIC_EQ`.
    """
    filter_type_band1 = WwiseProperty[EParametricEqFilterType]("FilterTypeBand1", EParametricEqFilterType)
    filter_type_band2 = WwiseProperty[EParametricEqFilterType]("FilterTypeBand2", EParametricEqFilterType)
    filter_type_band3 = WwiseProperty[EParametricEqFilterType]("FilterTypeBand3", EParametricEqFilterType)
    frequency_band1 = WwiseProperty[float]("FrequencyBand1", float)
    frequency_band2 = WwiseProperty[float]("FrequencyBand2", float)
    frequency_band3 = WwiseProperty[float]("FrequencyBand3", float)
    gain_band1 = WwiseProperty[float]("GainBand1", float)
    gain_band2 = WwiseProperty[float]("GainBand2", float)
    gain_band3 = WwiseProperty[float]("GainBand3", float)
    on_off_band1 = WwiseProperty[bool]("OnOffBand1", bool)
    on_off_band2 = WwiseProperty[bool]("OnOffBand2", bool)
    on_off_band3 = WwiseProperty[bool]("OnOffBand3", bool)
    output_level = WwiseProperty[float]("OutputLevel", float)
    process_lfe = WwiseProperty[bool]("ProcessLFE", bool)
    q_band1 = WwiseProperty[float]("QFactorBand1", float)
    q_band2 = WwiseProperty[float]("QFactorBand2", float)
    q_band3 = WwiseProperty[float]("QFactorBand3", float)
