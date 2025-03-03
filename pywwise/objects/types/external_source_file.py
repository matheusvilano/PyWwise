# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EExternalAnalysisType, ELoudnessNormalizationType
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.conversion import Conversion


class ExternalSourceFile(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_externalsourcefile.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.EXTERNAL_SOURCE_FILE`.
    """
    analysis_type = WwiseProperty[EExternalAnalysisType]("AnalysisType", EExternalAnalysisType)
    conversion = WwiseProperty[Conversion]("Conversion", Conversion)
    loudness_normalization_target = WwiseProperty[float]("LoudnessNormalizationTarget", float)
    loudness_normalization_type = WwiseProperty[ELoudnessNormalizationType](
        "LoudnessNormalizationType", ELoudnessNormalizationType)
    override_conversion = WwiseProperty[bool]("OverrideConversion", bool)
