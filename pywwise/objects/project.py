# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import (EActionNamePosition, ECaseStyleSimple, EColour, EFftWindowSize, EFilterBehaviour,
                           ELineEnding, ESoundBankDefinitionFormat)
from pywwise.objects.abc import WwiseObject
from pywwise.primitives import ProjectPath


class Project(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_project.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.PROJECT`.
    """
    always_save_media_ids_file = WwiseProperty[bool]("AlwaysSaveMediaIdsFile", bool)
    auto_detect_fft_window_size = WwiseProperty[EFftWindowSize]("AutoDetectFFTWindowSize", EFftWindowSize)
    auto_detect_threshold_high = WwiseProperty[float]("AutoDetectThresholdHigh", float)
    auto_detect_threshold_low = WwiseProperty[float]("AutoDetectThresholdLow", float)
    auto_detect_threshold_medium = WwiseProperty[float]("AutoDetectThresholdMedium", float)
    auto_sound_bank_all_events = WwiseProperty[bool]("AutoSoundBankAllEvents", bool)
    auto_sound_bank_enabled = WwiseProperty[bool]("AutoSoundBankEnabled", bool)
    colour = WwiseProperty[EColour]("Color", EColour)
    comm_port_discovery_broadcast = WwiseProperty[int]("CommPortDiscoveryBroadcast", int)
    comm_port_discovery_response = WwiseProperty[int]("CommPortDiscoveryResponse", int)
    comm_serial_post_base = WwiseProperty[int]("CommSerialPostBase", int)
    copy_loose_streamed_media = WwiseProperty[bool]("CopyLooseStreamedMedia", bool)
    default_language = WwiseProperty[str]("DefaultLanguage", str)
    event_action_name_position = WwiseProperty[EActionNamePosition]("EventActionNamePosition", EActionNamePosition)
    event_name_case_type = WwiseProperty[ECaseStyleSimple]("EventNameCaseType", ECaseStyleSimple)
    event_name_modify_case = WwiseProperty[int]("EventNameModifyCase", int)
    external_sources_input_path = WwiseProperty[ProjectPath]("ExternalSourcesInputPath", ProjectPath)
    external_sources_output_path = WwiseProperty[ProjectPath]("ExternalSourcesOutputPath", ProjectPath)
    filter_behaviour = WwiseProperty[EFilterBehaviour]("FilterBehavior", EFilterBehaviour)
    garbage_collect_wave_analysis = WwiseProperty[bool]("GarbageCollectWaveAnalysis", bool)
    generate_main_sound_bank = WwiseProperty[bool]("GenerateMainSoundBank", bool)
    generate_multiple_banks = WwiseProperty[bool]("GenerateMultipleBanks", bool)
    generate_sound_bank_json = WwiseProperty[bool]("GenerateSoundBankJSON", bool)
    generate_sound_bank_xml = WwiseProperty[bool]("GenerateSoundBankXML", bool)
    global_voices_limit = WwiseProperty[int]("GlobalVoicesLimit", int)
    license_key = WwiseProperty[str]("LicenseKey", str)
    line_ending = WwiseProperty[ELineEnding]("LineEnding", ELineEnding)
    max_dangerous_virtual_voices = WwiseProperty[int]("MaxDangerousVirtualVoices", int)
    max_messages_per_message_id = WwiseProperty[int]("MaxMessagesPerMessageId", int)
    media_auto_bank_sub_folders = WwiseProperty[bool]("MediaAutoBankSubFolders", bool)
    media_ids_in_single_file = WwiseProperty[bool]("MediaIDsInSingleFile", bool)
    override_colour = WwiseProperty[bool]("OverrideColor", bool)
    remove_unused_generated_files = WwiseProperty[bool]("RemoveUnusedGeneratedFiles", bool)
    sound_bank_allow_exceeding_sb = WwiseProperty[bool]("SoundBankAllowExceedingSB", bool)
    sound_bank_definition_file_format = WwiseProperty[ESoundBankDefinitionFormat]("SoundBankDefinitionFileFormat",
                                                                                  ESoundBankDefinitionFormat)
    sound_bank_generate_definition_file = WwiseProperty[bool]("SoundBankGenerateDefinitionFile", bool)
    sound_bank_generate_estimated_duration = WwiseProperty[bool]("SoundBankGenerateEstimatedDuration", bool)
    sound_bank_generate_header_file = WwiseProperty[bool]("SoundBankGenerateHeaderFile", bool)
    sound_bank_generate_max_attenuation_info = WwiseProperty[bool]("SoundBankGenerateMaxAttenuationInfo", bool)
    sound_bank_generate_print_colour = WwiseProperty[bool]("SoundBankGeneratePrintColor", bool)
    sound_bank_generate_print_guid = WwiseProperty[bool]("SoundBankGeneratePrintGUID", bool)
    sound_bank_generate_print_path = WwiseProperty[bool]("SoundBankGeneratePrintPath", bool)
    sound_bank_generate_readable_file = WwiseProperty[bool]("SoundBankGenerateReadableFile", bool)
    sound_bank_header_file_path = WwiseProperty[ProjectPath]("SoundBankHeaderFilePath", ProjectPath)
    sound_bank_include_soundbank_names_strings = WwiseProperty[bool]("SoundBankIncludeSoundbankNamesStrings", bool)
    sound_bank_paths = WwiseProperty[str]("SoundBankPaths", str)
    sound_bank_post_generate_custom_cmd_description = WwiseProperty[str]("SoundBankPostGenerateCustomCmdDescription",
                                                                         str)
    sound_bank_post_generate_custom_cmd_lines = WwiseProperty[str]("SoundBankPostGenerateCustomCmdLines", str)
    sound_bank_pre_generate_custom_cmd_description = WwiseProperty[str]("SoundBankPreGenerateCustomCmdDescription", str)
    sound_bank_pre_generate_custom_cmd_lines = WwiseProperty[str]("SoundBankPreGenerateCustomCmdLines", str)
    sound_bank_update_audio_files = WwiseProperty[bool]("SoundBankUpdateAudioFiles", bool)
    source_control_generated_files = WwiseProperty[bool]("SourceControlGeneratedFiles", bool)
    use_action_name_for_event = WwiseProperty[bool]("UseActionNameForEvent", bool)
    use_default_language = WwiseProperty[bool]("UseDefaultLanguage", bool)
    use_max_dangerous_virtual_voices = WwiseProperty[bool]("UseMaxDangerousVirtualVoices", bool)
    use_max_messages_per_message_id = WwiseProperty[bool]("UseMaxMessagesPerMessageId", bool)
    volume_threshold = WwiseProperty[float]("VolumeThreshold", float)
    wwise_console_load_user_settings = WwiseProperty[bool]("WwiseConsoleLoadUserSettings", bool)
    wwise_version_when_created = WwiseProperty[str]("WwiseVersionWhenCreated", str)
