# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from pywwise.primitives import GUID, Name, ProjectPath
from pywwise.structs import WwiseObjectInfo
from pywwise.waapi.ak.ak import WwiseConnection


class WwiseObject:
    """The base class for any class that serves as interface for getting/setting properties on Wwise objects."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        self._ak: WwiseConnection = ak
        self._guid: GUID = obj.guid
        self._name: Name = obj.name
        self._path: ProjectPath = obj.path
    
    @property
    def guid(self) -> GUID:
        """
        Get GUID.
        :return: Current GUID.
        """
        return self._guid
    
    @property
    def name(self) -> Name:
        """
        Get name.
        :return: Current name.
        """
        return self._name
    
    @name.setter
    def name(self, name: Name | str):
        """
        Set name.
        :param name: New name.
        """
        self._ak.wwise.core.object.set_name(self._guid, name)
    
    @property
    def path(self) -> ProjectPath:
        """
        Get path.
        :return: Current path.
        """
        return self._path
    
    @path.setter
    def path(self, path: ProjectPath):
        """
        Set path.
        :param path: New path.
        """
        if path[-1] == '\\':  # ProjectPath always uses `\\` instead of `/`.
            path = path[:-1]  # Remove slash.
        tokens = path.split('\\')
        if tokens[-1] == self.name:  # We only need the path up to the parent.
            path = tokens[:-1]  # Remove name.
        self._ak.wwise.core.object.move(self.guid, path)


class AcousticTexture(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.ACOUSTIC_TEXTURE`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Action(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.ACTION`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class ActionException(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.ACTION_EXCEPTION`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class ActorMixer(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.ACTOR_MIXER`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Attenuation(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.ATTENUATION`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class AudioDevice(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.AUDIO_DEVICE`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class AudioSource(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.AUDIO_SOURCE`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class AuxBus(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.AUX_BUS`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class BlendContainer(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.BLEND_CONTAINER`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class BlendTrack(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.BLEND_TRACK`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Bus(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.BUS`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class ControlSurfaceBinding(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.CONTROL_SURFACE_BINDING`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class ControlSurfaceBindingGroup(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.CONTROL_SURFACE_BINDING_GROUP`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class ControlSurfaceSession(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.CONTROL_SURFACE_SESSION`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Conversion(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.CONVERSION`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Curve(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.CURVE`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class CustomState(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.CUSTOM_STATE`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class DialogueEvent(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.DIALOGUE_EVENT`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Effect(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.EFFECT`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class EffectSlot(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.EFFECT_SLOT`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Event(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.EVENT`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class ExternalSource(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.EXTERNAL_SOURCE`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class ExternalSourceFile(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.EXTERNAL_SOURCE_FILE`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Folder(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.FOLDER`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class GameParameter(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.GAME_PARAMETER`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Language(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.LANGUAGE`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Marker(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MARKER`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Metadata(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.METADATA`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class MidiFileSource(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MIDI_FILE_SOURCE`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class MidiParameter(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MIDI_PARAMETER`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class MixingSession(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MIXING_SESSION`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Modifier(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MODIFIER`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class ModulatorEnvelope(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MODULATOR_ENVELOPE`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class ModulatorLfo(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MODULATOR_LFO`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class ModulatorTime(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MODULATOR_TIME`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class MultiSwitchEntry(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MULTI_SWITCH_ENTRY`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class MusicClip(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_CLIP`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class MusicClipMidi(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_CLIP_MIDI`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class MusicCue(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_CUE`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class MusicEventCue(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_EVENT_CUE`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class MusicFade(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_FADE`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class MusicPlaylistContainer(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_PLAYLIST_CONTAINER`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class MusicPlaylistItem(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_PLAYLIST_ITEM`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class MusicSegment(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_SEGMENT`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class MusicStinger(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_STINGER`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class MusicSwitchContainer(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_SWITCH_CONTAINER`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class MusicTrack(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_TRACK`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class MusicTrackSequence(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_TRACK_SEQUENCE`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class MusicTransition(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.MUSIC_TRANSITION`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class ObjectSettingAssoc(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.OBJECT_SETTING_ASSOC`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Panner(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.PANNER`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Path2d(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.PATH_2D`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Platform(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.PLATFORM`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class PluginDataSource(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.PLUGIN_DATA_SOURCE`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Position(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.POSITION`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Project(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.PROJECT`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Query(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.QUERY`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class RandomSequenceContainer(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.RANDOM_SEQUENCE_CONTAINER`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Rtpc(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.RTPC`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class SearchCriteria(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SEARCH_CRITERIA`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Sound(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SOUND`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class SoundBank(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SOUND_BANK`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class SoundcasterSession(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SOUNDCASTER_SESSION`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class SourcePlugin(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SOURCE_PLUGIN`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class State(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.STATE`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class StateGroup(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.STATE_GROUP`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Switch(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SWITCH`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class SwitchContainer(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SWITCH_CONTAINER`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class SwitchGroup(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.SWITCH_GROUP`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class Trigger(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.TRIGGER`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class UserProjectSettings(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.USER_PROJECT_SETTINGS`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!


class WorkUnit(WwiseObject):
    """A class serving as an interface for getting/setting properties on Wwise objects. This type specifically targets
    the class represented by `EObjectType.WORK_UNIT`."""
    
    def __init__(self, obj: WwiseObjectInfo, ak: WwiseConnection):
        """
        Conversion-type constructor. Uses generic object info to create a strongly-typed object.
        :param obj: A `WwiseObjectInfo` instance, which contains generic information such as the `GUID` of the object.
        """
        super().__init__(obj, ak)
        raise NotImplementedError("WwiseObject types will only be feature-complete in Beta 2.")  # TODO: Implement this!
