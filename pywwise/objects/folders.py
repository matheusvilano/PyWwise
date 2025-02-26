# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.objects.types import WwiseObject


class Folder(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.FOLDER`."""
    colour = WwiseProperty("Color", int)
    inclusion = WwiseProperty("Inclusion", bool)
    override_colour = WwiseProperty("OverrideColor", bool)


class WorkUnit(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WORK_UNIT`."""
