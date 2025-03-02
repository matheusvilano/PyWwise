# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EActionType, EScope, ESeekType, ESetterType
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.effect import Effect
from pywwise.objects.types.effect_slot import EffectSlot


class Action(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_action.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.ACTION`.
    """
    absolute_or_relative = WwiseProperty[ESetterType]("AbsoluteOrRelative", ESetterType)
    action_type = WwiseProperty[EActionType]("ActionType", EActionType)
    apply_to_dynamic_sequence = WwiseProperty[bool]("ApplyToDynamicSequence", bool)
    apply_to_state_transition = WwiseProperty[bool]("ApplyToStateTransition", bool)
    bypass_flag = WwiseProperty[bool]("BypassFlag", bool)
    bypass_game_parameter_internal_transition = WwiseProperty[bool]("BypassGameParameterInternalTransition", bool)
    delay = WwiseProperty[float]("Delay", float)
    effect_slot = WwiseProperty[EffectSlot]("EffectSlot", EffectSlot)
    fade_in_curve = WwiseProperty[int]("FadeInCurve", int)
    fade_out_curve = WwiseProperty[int]("FadeOutCurve", int)
    fade_time = WwiseProperty[float]("FadeTime", float)
    game_parameter_value = WwiseProperty[float]("GameParameterValue", float)
    highpass = WwiseProperty[int]("Highpass", int)
    inclusion = WwiseProperty[bool]("Inclusion", bool)
    lowpass = WwiseProperty[int]("Lowpass", int)
    master_resume = WwiseProperty[bool]("MasterResume", bool)
    pause_delayed_resume_action = WwiseProperty[bool]("PauseDelayedResumeAction", bool)
    pitch = WwiseProperty[float]("Pitch", float)
    probability = WwiseProperty[float]("Probability", float)
    resume_state_transition = WwiseProperty[bool]("ResumeStateTransition", bool)
    scope = WwiseProperty[EScope]("Scope", EScope)
    seek_percent = WwiseProperty[float]("SeekPercent", float)
    seek_time = WwiseProperty[float]("SeekTime", float)
    seek_to_marker = WwiseProperty[bool]("SeekToMarker", bool)
    seek_type = WwiseProperty[ESeekType]("SeekType", ESeekType)
    target = WwiseProperty[WwiseObject]("Target", WwiseObject)
    target_effect = WwiseProperty[Effect]("TargetEffect", Effect)
    volume = WwiseProperty[float]("Volume", float)
