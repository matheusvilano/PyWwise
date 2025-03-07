# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EMechanismPlayMode, ERandomOrSequence
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.rtpc import Rtpc


class Position(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_position.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.POSITION`.
    """
    new_path_for_each_sound = WwiseProperty[bool]("NewPathForEachSound", bool)
    pan_x = WwiseProperty[float]("PanX", float)
    pan_y = WwiseProperty[float]("PanY", float)
    pan_z = WwiseProperty[float]("PanZ", float)
    play_mechanism_loop = WwiseProperty[bool]("PlayMechanismLoop", bool)
    play_mechanism_random_or_sequence = WwiseProperty[ERandomOrSequence](
        "PlayMechanismRandomOrSequence", ERandomOrSequence)
    play_mechanism_step_or_continuous = WwiseProperty[EMechanismPlayMode]("PlayMechanismStepOrContinuous", EMechanismPlayMode)
    play_mechanism_transition_time = WwiseProperty[float]("PlayMechanismTransitionTime", float)
    play_mechanism_transition_use = WwiseProperty[bool]("PlayMechanismTransitionUse", bool)
    rtpc = WwiseProperty[tuple[Rtpc, ...]]("RTPC", tuple)
