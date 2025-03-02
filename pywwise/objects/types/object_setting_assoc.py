# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.objects.abc import WwiseObject


class ObjectSettingAssoc(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_objectsettingassoc.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.OBJECT_SETTING_ASSOC`.
    """
    continue_play = WwiseProperty[bool]("ContinuePlay", bool)
    fade_in_time = WwiseProperty[float]("FadeInTime", float)
    fade_out_time = WwiseProperty[float]("FadeOutTime", float)
    first_occurrence_only = WwiseProperty[bool]("FirstOccurenceOnly", bool)
