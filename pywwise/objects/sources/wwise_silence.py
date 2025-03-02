# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.objects.abc import WwiseObject


class WwiseSilence(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_source_wwise_silence.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SOURCE_PLUGIN`.
    """
    length = WwiseProperty[float]("Length", float)
    length_max = WwiseProperty[float]("LengthMax", float)
    length_min = WwiseProperty[float]("LengthMin", float)
