# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.enums import EActionNamePosition, ECaseStyleSimple, ESoundBankDefinitionFormat
from pywwise.objects.abc import WwiseObject
from pywwise.objects.types.conversion import Conversion
from pywwise.primitives import ProjectPath


class UserProjectSettings(WwiseObject):
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_userprojectsettings.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.USER_PROJECT_SETTINGS`.
    """
    auto_sound_bank_all_events = WwiseProperty[bool]("AutoSoundBankAllEvents", bool)
    auto_sound_bank_enabled = WwiseProperty[bool]("AutoSoundBankEnabled", bool)
    conversion = WwiseProperty[Conversion]("Conversion", Conversion)
    convert_external_sources = WwiseProperty[bool]("ConvertExternalSources", bool)
    copy_loose_streamed_media = WwiseProperty[bool]("CopyLooseStreamedMedia", bool)
    default_sound_volume = WwiseProperty[float]("DefaultSoundVolume", float)
    event_action_name_position = WwiseProperty[EActionNamePosition]("EventActionNamePosition", EActionNamePosition)
    event_creation_settings_override = WwiseProperty[bool]("EventCreationSettingsOverride", bool)
    event_name_case_type = WwiseProperty[ECaseStyleSimple]("EventNameCaseType", ECaseStyleSimple)
    event_name_modify_case = WwiseProperty[bool]("EventNameModifyCase", bool)
    external_sources_input_path = WwiseProperty[ProjectPath]("ExternalSourcesInputPath", ProjectPath)
    external_sources_output_path = WwiseProperty[ProjectPath]("ExternalSourcesOutputPath", ProjectPath)
    generate_main_sound_bank = WwiseProperty[bool]("GenerateMainSoundBank", bool)
    generate_multiple_banks = WwiseProperty[bool]("GenerateMultipleBanks", bool)
    generate_sound_bank_json = WwiseProperty[bool]("GenerateSoundBankJSON", bool)
    generate_sound_bank_xml = WwiseProperty[bool]("GenerateSoundBankXML", bool)
    media_auto_bank_sub_folders = WwiseProperty[bool]("MediaAutoBankSubFolders", bool)
    override_conversion = WwiseProperty[bool]("OverrideConversion", bool)
    post_generate_step_user_override = WwiseProperty[bool]("PostGenerateStepUserOverride", bool)
    pre_generate_step_user_override = WwiseProperty[bool]("PreGenerateStepUserOverride", bool)
    remove_unused_generated_files = WwiseProperty[bool]("RemoveUnusedGeneratedFiles", bool)
    settings_user_override = WwiseProperty[bool]("SettingsUserOverride", bool)
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
