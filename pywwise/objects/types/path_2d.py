# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.objects.abc import WwiseObject


class Path2d(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_path2d.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.PATH_2D`.
    """
    append_offset = WwiseProperty[int]("AppendOffset", int)
    duration = WwiseProperty[int]("Duration", int)
    flags = WwiseProperty[int]("Flags", int)
    linear_time = WwiseProperty[bool]("LinearTime", bool)
    random_x = WwiseProperty[float]("RandomX", float)
    random_y = WwiseProperty[float]("RandomY", float)
    random_z = WwiseProperty[float]("RandomZ", float)
