# Copyright 2025 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.descriptors import WwiseProperty
from pywwise.objects.abc import WwiseObject


class Impacter(WwiseObject):  # TODO: Implement enums for this class once the plugin is not in beta anymore.
    """
    https://www.audiokinetic.com/en/library/edge/?source=SDK&id=wwiseobject_source_impacter.html \n
    A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SOURCE_PLUGIN`. Note: this plugin is in BETA and subject to change. Some
    properties might also not work as expected or even be displayed in the Wwise UI.
    """
    excitation_mask = WwiseProperty[int]("ExcitationMask", int)
    excitation_selection_mode = WwiseProperty[int]("ExcitationSelectionMode", int)
    fm_depth = WwiseProperty[float]("FMDepth", float)
    fm_depth_random = WwiseProperty[float]("FMDepthRandom", float)
    file_excitation = WwiseProperty[int]("FileExcitation", int)
    file_model = WwiseProperty[int]("FileModel", int)
    impact_position = WwiseProperty[float]("ImpactPosition", float)
    impact_position_random = WwiseProperty[float]("ImpactPositionRandom", float)
    mass = WwiseProperty[float]("Mass", float)
    mass_random = WwiseProperty[float]("MassRandom", float)
    min_duration = WwiseProperty[float]("MinDuration", float)
    model_mask = WwiseProperty[int]("ModelMask", int)
    model_selection_mode = WwiseProperty[int]("ModelSelectionMode", int)
    num_files = WwiseProperty[int]("NumFiles", int)
    output_level = WwiseProperty[float]("OutputLevel", float)
    velocity = WwiseProperty[float]("Velocity", float)
    velocity_random = WwiseProperty[float]("VelocityRandom", float)
