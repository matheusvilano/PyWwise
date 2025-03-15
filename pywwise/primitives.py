# Copyright 2024 Matheus Vilano
# SPDX-License-Identifier: Apache-2.0

from abc import ABC as _ABC, abstractmethod as _abstractmethod
from typing import Self as _Self
from uuid import UUID as _UUID


class _PyWwiseType(_ABC):
    """The base class for PyWwise core types."""
    
    @classmethod
    @_abstractmethod
    def get_null(cls) -> _Self:
        """Use when the intention is to represent an "invalid" instance."""
        pass
    
    def is_valid(self) -> bool:
        """
        Checks whether the instance contains a valid value.
        :return: `True`, if the value is valid; else, `False`.
        """
        return self != self.get_null()  # or greater than or equal to 0


class _PyWwiseID(int, _PyWwiseType):
    """The base class for `int` subclasses in PyWwise which represent numeric identifiers."""
    
    def __new__(cls, value: int) -> _Self:
        """
        Creates a new ID.
        :param value: The ID.
        :return: The new ID.
        :raise ValueError: If the ID is less than `0` and not `-1`.
        """
        value = int(value)  # Sometimes the number is a string. In that case, try converting.
        if value < 0 and value != -1:
            raise ValueError("ID value must be non-negative (or -1, if representing an invalid ID).")
        return int.__new__(cls, value)
    
    @classmethod
    def get_null(cls) -> _Self:
        """
        Use when the intention is to represent an "invalid" ID.
        :return: `-1`, which represents an invalid ID.
        """
        return cls(-1)


class _PyWwiseStr(str, _PyWwiseType):
    """The base class for `str` subclasses in PyWwise which represent alphanumeric values."""
    
    def __new__(cls, chars: str) -> _Self:
        """
        Instantiates a new PyWwiseStr.
        :param chars: The string to use to create a new PyWwiseStr.
        :return: The new PyWwiseStr.
        """
        return str.__new__(cls, chars)
    
    @classmethod
    def get_null(cls) -> _Self:
        """
        Gets a "null" instance. Use this to represent ideas such as "invalidity" or "nonexistence".
        :return: A "null" instance, which contains a single character: the null-terminator (`\0`).
        """
        return cls("\0")


class _PyWwisePath(_PyWwiseStr):
    
    def __new__(cls, path: str, windows_style: bool = True) -> _Self:
        """
        Creates a new path-like object using a `str` as the container. By default, any path will be automatically
        converted to a Windows-style path. Example: `"/Actor-Mixer Hierarchy/Default Work Unit"` will be converted to
        `"\\Actor-Mixer Hierarchy\\Default Work Unit"`. This behaviour can be overridden.
        :param path: The path string.
        :param windows_style: Whether the path should be forced to a Windows-style format. Example: if `True`,
                              `"/Actor-Mixer Hierarchy/Default Work Unit"` will be converted to
                              `"\\Actor-Mixer Hierarchy\\Default Work Unit"`.
        :return: A new `PyWwisePath` object.
        :raise ValueError: If the path is empty.
        """
        delimiter = "\\" if windows_style else "/"
        
        if path == "\0":
            path = super().__new__(cls, path)
            path._delimiter = delimiter
            return path
        
        if windows_style:
            path = path.replace("/", "\\")
        else:
            path = path.replace("\\", "/")
        
        if not path:  # Empty!
            raise ValueError("The provided path is invalid or empty. Must be a valid path-like string.")
        
        if path[0] != delimiter:
            path = f"{delimiter}{path}"
        
        if path[-1] == delimiter:
            path = path[:-1]
        
        path = super().__new__(cls, path)
        path._delimiter = delimiter
        return path
    
    def __getitem__(self, item: int | slice) -> str | list[str]:
        """
        Gets one or more components from the path.
        :param item: The index or slice to use.
        :return: One or more components from the path.
        """
        return self.split(self._delimiter)[1:][item]
    
    def __truediv__(self, path: str) -> _Self:
        """
        Build or extend a path using the `/` operator.
        :param path: The path, as a string.
        :return: The new path.
        """
        if isinstance(path, str):
            path = self.__class__(f"{self}{self._delimiter}{path.lstrip('/')}")
            return path.replace("/" if self._delimiter == "\\" else "/", self._delimiter)
        else:
            raise TypeError(f"Unsupported type for path join: {type(path)}")


class Name(_PyWwiseStr):
    """A Wwise object Name. This is usually intended to be used with unique objects (e.g. State Groups)."""
    
    def __new__(cls, name: str) -> _Self:
        """
        Instantiates a new Name.
        :param name: The string to use to create a new Name.
        :return: The new Name.
        :raises ValueError: If the name is empty.
        """
        if len(name) <= 0:
            raise ValueError("The provided name string is empty.")
        return str.__new__(cls, name)


class GUID(_PyWwiseStr):
    """A Wwise object GUID (e.g. `"{63726145-57FB-490B-B611-738BD3EF2F72}"`."""
    
    def __new__(cls, guid: str) -> _Self:
        """
        Instantiates a new GUID.
        :param guid: The string to use to create a new GUID.
        :return: The new GUID.
        :raise ValueError: If the GUID is in the wrong format.
        """
        if (guid[0] != '{' or guid[-1] != '}') or not cls.validate(guid):
            raise ValueError(f"Wrong GUID format. Expected format is: \"{cls.get_null()}\" (alphanumerical).")
        return str.__new__(cls, guid)
    
    @classmethod
    def get_null(cls) -> _Self:
        """
        A GUID containing "zero" (the default "invalid" GUID).
        :return: The GUID "{00000000-0000-0000-0000-000000000000}".
        """
        return GUID("{00000000-0000-0000-0000-000000000000}")
    
    @classmethod
    def validate(cls, value: str) -> bool:
        """
        Validates the provided string as a GUID.
        :param value: The string to validate as a GUID.
        :return: Whether the provided string is a valid GUID.
        """
        try:
            _UUID(value, version=4)
            return True
        except ValueError:
            return False


class ProjectPath(_PyWwisePath):
    """A project path (e.g. `"\\Actor-Mixer Hierarchy\\Default Work Unit\\MyActorMixer"`)."""
    
    def __new__(cls, path: str, windows_style: bool = True):
        """
        Creates a new path-like object using a `str` as the container. By default, any path will be automatically
        converted to a Windows-style path. Example: `"/Actor-Mixer Hierarchy/Default Work Unit"` will be converted to
        `"\\Actor-Mixer Hierarchy\\Default Work Unit"`. This behaviour can be overridden.
        :param path: The path string.
        :param windows_style: Whether the path should be forced to a Windows-style format. Example: if `True`,
                              `"/Actor-Mixer Hierarchy/Default Work Unit"` will be converted to
                              `"\\Actor-Mixer Hierarchy\\Default Work Unit"`.
        :return: A new `PyWwisePath` object.
        :raise ValueError: If the path is empty.
        """
        return super().__new__(cls, path)
    
    @classmethod
    def actor_mixer_hierarchy(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Actor-" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Actor-Mixer Hierarchy' or '\\Actor-Mixer Hierarchy\\Default Work Unit'.
        """
        return cls(rf"\Actor-Mixer Hierarchy\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def attenuations(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Attenuations'" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Attenuations' or '\\Attenuations\\Default Work Unit'.
        """
        return cls(rf"\Attenuations\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def conversion_settings(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Conversion Settings" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Conversion Settings' or '\\Conversion Settings\\Default Work Unit'.
        """
        return cls(rf"\Conversion Settings\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def audio_devices(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Audio Devices" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Audio Devices' or '\\Audio Devices\\Default Work Unit'.
        """
        return cls(rf"\Audio Devices\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def control_surface_sessions(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Control Surface" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Control Surface Sessions' or '\\Control Surface Sessions\\Default Work Unit'.
        """
        return cls(rf"\Control Surface Sessions\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def dynamic_dialogue(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Dynamic Dialogue" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Dynamic Dialogue' or '\\Dynamic Dialogue\\Default Work Unit'.
        """
        return cls(rf"\Dynamic Dialogue\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def effects(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Effects'" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Effects' or '\\Effects\\Default Work Unit'.
        """
        return cls(rf"\Effects\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def events(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Events'" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Events' or '\\Events\\Default Work Unit'.
        """
        return cls(rf"\Events\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def game_parameters(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Game Parameters" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Game Parameters' or '\\Game Parameters\\Default Work Unit'.
        """
        return cls(rf"\Game Parameters\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def interactive_music_hierarchy(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Interactive Music" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Interactive Music Hierarchy' or '\\Interactive Music Hierarchy\\Default Work Unit'.
        """
        return cls(rf"\Interactive Music Hierarchy\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def master_mixer_hierarchy(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Master-" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Master-Mixer Hierarchy' or '\\Master-Mixer Hierarchy\\Default Work Unit'.
        """
        return cls(rf"\Master-Mixer Hierarchy\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def metadata(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Metadata'" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Metadata' or '\\Metadata\\Default Work Unit'.
        """
        return cls(rf"\Metadata\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def mixing_sessions(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Mixing Sessions" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Mixing Sessions' or '\\Mixing Sessions\\Default Work Unit'.
        """
        return cls(rf"\Mixing Sessions\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def modulators(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Modulators'" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Modulators' or '\\Modulators\\Default Work Unit'.
        """
        return cls(rf"\Modulators\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def queries(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Queries'" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Queries' or '\\Queries\\Default Work Unit'.
        """
        return cls(rf"\Queries\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def sound_banks(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "SoundBanks'" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\SoundBanks' or '\\SoundBanks\\Default Work Unit'.
        """
        return cls(rf"\SoundBanks\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def soundcaster_sessions(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Soundcaster Sessions" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Soundcaster Sessions' or '\\Soundcaster Sessions\\Default Work Unit'.
        """
        return cls(rf"\Soundcaster Sessions\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def states(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "States'" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\States' or '\\States\\Default Work Unit'.
        """
        return cls(rf"\States\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def switches(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Switches'" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Switches' or '\\Switches\\Default Work Unit'.
        """
        return cls(rf"\Switches\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def triggers(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Triggers'" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Triggers' or '\\Triggers\\Default Work Unit'.
        """
        return cls(rf"\Triggers\{'Default Work Unit' if default_work_unit else ''}")
    
    @classmethod
    def virtual_acoustics(cls, default_work_unit: bool = False) -> _Self:
        """
        Get path to the default "Virtual Acoustics" folder. May include the Default Work Unit.
        :param default_work_unit: Whether to include the Default Work Unit in the path.
        :return: '\\Virtual Acoustics' or '\\Virtual Acoustics\\Default Work Unit'.
        """
        return cls(rf"\Virtual Acoustics\{'Default Work Unit' if default_work_unit else ''}")


class OriginalsPath(_PyWwisePath):
    """A source file path, relative to the Originals folder. Note: the Originals path can be customized in Wwise."""
    
    def __new__(cls, path: str, windows_style: bool = True) -> _Self:
        """
        Creates a new OriginalsPath. You can think of this as a string container.
        :param path: The source file path, relative to the Originals folder.
        :param windows_style: Whether the path should be forced to a Windows-style format. Example: if `True`,
                      `"/SFX/Ambience"` will be converted to `"\\SFX\\Ambience"`.
        :return: A new OriginalsPath.
        :raise ValueError: If the path is empty.
        """
        return super().__new__(cls, path)
    
    @classmethod
    def default_sfx(cls) -> _Self:
        """
        Get path to the default "SFX'" folder.
        :return: '\\SFX'.
        """
        return cls(rf"\SFX")
    
    @classmethod
    def default_voices(cls) -> _Self:
        """
        Get path to the default "Voices'" folder.
        :return: '\\Voices'.
        """
        return cls(rf"\Voices")


class GameObjectID(_PyWwiseID):
    """A Game Object ID. This is expected to be a non-negative number."""
    
    @classmethod
    def get_global(cls) -> _Self:
        """
        Specialized factory function. Useful for scripts that target all game objects.
        :return: A new GameObjectID containing the default Global game object ID.
        """
        return GameObjectID((1 << 64) - 1)  # That expression equals the max uint64 value.
    
    @classmethod
    def get_transport(cls) -> _Self:
        """
        Specialized factory function. Useful for scripts where the target game object is Wwise's default transport.
        :return: A new GameObjectID containing the default Transport game object ID.
        """
        return GameObjectID((1 << 64) - 2)  # That expression equals the max uint64 value - 1.


class ShortID(_PyWwiseID):
    """A Wwise object short ID. This is expected to be a non-negative number."""


class PlayingID(_PyWwiseID):
    """A Playing ID, which represents an instance generated from an Event. A negative means the ID is invalid."""
