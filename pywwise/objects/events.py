# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EActionType, EScope, ESeekType, ESetterType
from pywwise.objects.effects import Effect, EffectSlot
from pywwise.objects.types import WwiseObject


class Action(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.ACTION`."""
    absolute_or_relative = WwiseProperty("AbsoluteOrRelative", ESetterType)
    action_type = WwiseProperty("ActionType", EActionType)
    apply_to_dynamic_sequence = WwiseProperty("ApplyToDynamicSequence", bool)
    apply_to_state_transition = WwiseProperty("ApplyToStateTransition", bool)
    bypass_flag = WwiseProperty("BypassFlag", bool)
    bypass_game_parameter_internal_transition = WwiseProperty("BypassGameParameterInternalTransition", bool)
    delay = WwiseProperty("Delay", float)
    effect_slot = WwiseProperty("EffectSlot", EffectSlot)
    fade_in_curve = WwiseProperty("FadeInCurve", int)
    fade_out_curve = WwiseProperty("FadeOutCurve", int)
    fade_time = WwiseProperty("FadeTime", float)
    game_parameter_value = WwiseProperty("GameParameterValue", float)
    highpass = WwiseProperty("Highpass", int)
    inclusion = WwiseProperty("Inclusion", bool)
    lowpass = WwiseProperty("Lowpass", int)
    master_resume = WwiseProperty("MasterResume", bool)
    pause_delayed_resume_action = WwiseProperty("PauseDelayedResumeAction", bool)
    pitch = WwiseProperty("Pitch", float)
    probability = WwiseProperty("Probability", float)
    resume_state_transition = WwiseProperty("ResumeStateTransition", bool)
    scope = WwiseProperty("Scope", EScope)
    seek_percent = WwiseProperty("SeekPercent", float)
    seek_time = WwiseProperty("SeekTime", float)
    seek_to_marker = WwiseProperty("SeekToMarker", bool)
    seek_type = WwiseProperty("SeekType", ESeekType)
    target = WwiseProperty("Target", WwiseObject)
    target_effect = WwiseProperty("TargetEffect", Effect)
    volume = WwiseProperty("Volume", float)


class ActionException(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.ACTION_EXCEPTION`."""


class DialogueEvent(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.DIALOGUE_EVENT`."""


class Event(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.EVENT`."""
