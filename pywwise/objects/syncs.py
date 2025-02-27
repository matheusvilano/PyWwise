# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.objects.types import WwiseObject


class Curve(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.CURVE`."""


class CustomState(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.CUSTOM_STATE`."""


class GameParameter(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.GAME_PARAMETER`."""


class MultiSwitchEntry(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MULTI_SWITCH_ENTRY`."""


class State(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.STATE`."""


class Switch(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SWITCH`."""


class SwitchGroup(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SWITCH_GROUP`."""


class StateGroup(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.STATE_GROUP`."""


class Rtpc(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.RTPC`."""


class Trigger(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.TRIGGER`."""
