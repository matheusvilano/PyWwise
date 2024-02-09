from typing import TypeAlias as _TypeAlias


class Name(str):
    """A Wwise object Name. This is usually intended to be used with unique objects (e.g. State Groups)."""


class GUID(str):
    """A Wwise object GUID (e.g. `"{63726145-57FB-490B-B611-738BD3EFAF72}"`."""


class ProjectPath(str):
    """A project path (e.g. `"/Actor-Mixer Hierarchy/Default Work Unit/MyActorMixer"`)."""


class ShortID(int):
    """A Wwise object short ID. This is expected to be a non-negative number."""
