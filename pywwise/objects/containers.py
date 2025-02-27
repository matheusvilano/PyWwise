# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.objects.types import WwiseObject


class ActorMixer(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.ACTOR_MIXER`."""


class BlendContainer(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.BLEND_CONTAINER`."""


class BlendTrack(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.BLEND_TRACK`."""


class ObjectSettingAssoc(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.OBJECT_SETTING_ASSOC`."""


class RandomSequenceContainer(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.RANDOM_SEQUENCE_CONTAINER`."""


class SwitchContainer(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SWITCH_CONTAINER`."""
