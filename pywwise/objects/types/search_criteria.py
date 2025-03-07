# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import (ELogicalOperator, ESampleRateConversionQuality, ESearchCriteriaContainerType,
                           ESearchCriteriaCurveType, ESearchCriteriaCurveUsage, ESearchCriteriaLfeOption,
                           ESearchCriteriaMode, ESearchCriteriaNumericOperator, ESearchCriteriaOtherChannelsCountOption,
                           ESearchCriteriaRtpcOperator, ESearchCriteriaSoundbankReferences, ESearchCriteriaSoundType,
                           ESearchCriteriaSRConversionType, ESearchCriteriaStateProperty,
                           ESearchCriteriaSwitchingOperator, ESearchCriteriaUsingOperator)
from pywwise.objects.abc import WwiseObject


class SearchCriteria(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_searchcriteria.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SEARCH_CRITERIA`.
    """
    attenuation = WwiseProperty[str]("Attenuation", str)
    conditional_operator = WwiseProperty[ELogicalOperator]("ConditionalOperator", ELogicalOperator)
    conversion = WwiseProperty[str]("Conversion", str)
    curve_type = WwiseProperty[ESearchCriteriaCurveType]("CurveType", ESearchCriteriaCurveType)
    curve_usage = WwiseProperty[ESearchCriteriaCurveUsage]("CurveUsage", ESearchCriteriaCurveUsage)
    default_switch_state = WwiseProperty[str]("DefaultSwitchState", str)
    effect = WwiseProperty[str]("Effect", str)
    effect_class_id = WwiseProperty[str]("EffectClassID", str)
    events_referenced_in_operator = WwiseProperty[ESearchCriteriaSoundbankReferences]("EventReferencedInOperator",
                                                                                      ESearchCriteriaSoundbankReferences)
    game_parameter = WwiseProperty[str]("GameParameter", str)
    has_empty_assignation = WwiseProperty[bool]("HasEmptyAssignation", bool)
    inclusion = WwiseProperty[bool]("Inclusion", bool)
    is_checked = WwiseProperty[bool]("IsChecked", bool)
    is_linked = WwiseProperty[bool]("IsLinked", bool)
    is_source_of_override = WwiseProperty[bool]("IsSourceOfOverride", bool)
    is_special_search = WwiseProperty[bool]("IsSpecialSearch", bool)
    is_used = WwiseProperty[bool]("IsUsed", bool)
    left_value = WwiseProperty[float]("LeftValue", float)
    logical_operator = WwiseProperty[ELogicalOperator]("LogicalOperator", ELogicalOperator)
    metadata = WwiseProperty[str]("Metadata", str)
    metadata_class_id = WwiseProperty[str]("MetadataClassID", str)
    mode = WwiseProperty[ESearchCriteriaMode]("Mode", ESearchCriteriaMode)
    music_segment = WwiseProperty[str]("MusicSegment", str)
    numeric_operator = WwiseProperty[ESearchCriteriaNumericOperator]("NumericOperator", ESearchCriteriaNumericOperator)
    object_referenced = WwiseProperty[str]("ObjectReferenced", str)
    output_bus = WwiseProperty[str]("OutputBus", str)
    property_name = WwiseProperty[str]("PropertyName", str)
    rtpc_operator = WwiseProperty[ESearchCriteriaRtpcOperator]("RTPCOperator", ESearchCriteriaRtpcOperator)
    right_value = WwiseProperty[float]("RightValue", float)
    rnd_seq_container_type = WwiseProperty[ESearchCriteriaContainerType]("RndSeqContainerType",
                                                                         ESearchCriteriaContainerType)
    sr_conversion_quality = WwiseProperty[ESampleRateConversionQuality]("SRConversionQuality",
                                                                        ESampleRateConversionQuality)
    sample_rate_conversion_type = WwiseProperty[ESearchCriteriaSRConversionType]("SampleRateConversionType",
                                                                                 ESearchCriteriaSRConversionType)
    sound_type = WwiseProperty[ESearchCriteriaSoundType]("SoundType", ESearchCriteriaSoundType)
    source_audio_format = WwiseProperty[str]("SourceAudioFormat", str)
    source_channels_lfe_option = WwiseProperty[ESearchCriteriaLfeOption]("SourceChannelsLFEOption",
                                                                         ESearchCriteriaLfeOption)
    source_channels_others_count = WwiseProperty[int]("SourceChannelsOthersCount", int)
    source_channels_others_option = WwiseProperty[ESearchCriteriaOtherChannelsCountOption]("SourceChannelsOthersOption",
                                                                                           ESearchCriteriaOtherChannelsCountOption)
    source_language = WwiseProperty[str]("SourceLanguage", str)
    source_type = WwiseProperty[str]("SourceType", str)
    state = WwiseProperty[str]("State", str)
    state_group = WwiseProperty[str]("StateGroup", str)
    state_property_usage = WwiseProperty[ESearchCriteriaStateProperty]("StatePropertyUsage",
                                                                       ESearchCriteriaStateProperty)
    switch_group = WwiseProperty[str]("SwitchGroup", str)
    switching_operator = WwiseProperty[ESearchCriteriaSwitchingOperator]("SwitchingOperator",
                                                                         ESearchCriteriaSwitchingOperator)
    trigger = WwiseProperty[str]("Trigger", str)
    u_int_value = WwiseProperty[int]("UIntValue", int)
    user_string = WwiseProperty[str]("UserString", str)
    using_operator = WwiseProperty[ESearchCriteriaUsingOperator]("UsingOperator", ESearchCriteriaUsingOperator)
