# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.objects.types import WwiseObject


class Folder(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_folder.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.FOLDER`.
    """
    colour = WwiseProperty[int]("Color", int)
    inclusion = WwiseProperty[bool]("Inclusion", bool)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)


class WorkUnit(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_workunit.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WORK_UNIT`.
    """
    colour = WwiseProperty[int]("Color", int)
    inclusion = WwiseProperty[bool]("Inclusion", bool)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
