# PyWwise

PyWwise is an open-source Python wrapper around the Wwise Authoring Application Programming Interface (WAAPI). PyWwise 
is meant to make Wwise scripting (e.g. automation, data validation, etc.) much easier to achieve. There are multiple 
benefits in using PyWwise; the three main highlights are:

- Pythonic Architecture
- Object-Oriented
- Fully Documented

## Installation

PyWwise is available on the [Python Package Index](https://pypi.org/project/pywwise/), and so it is recommended to 
install it via `pip`. Using CMD, Terminal, PowerShell, or any command-line interface of your choice, run the command 
`pip install pywwise` to install the latest version of PyWwise.

## Usage

Getting started with PyWwise is easy, as it exposes only a select amount of modules. The first step is always to import 
`pywwise` and initialize a connection to an instance of Wwise using the factory function `new`. After that, you will 
likely need some imports from `pywwise.types`, `pywwise.enums`, and/or `pywwise.structs`, depending on what WAAPI 
functions and/or topics you are looking to use. PyWwise is fully documented, so each function or topic will let you 
know what will be needed.

Since PyWwise is entirely based on WAAPI and the [`waapi-client`](https://pypi.org/project/waapi-client/) package, you 
may use the official [Wwise Authoring API Reference](https://www.audiokinetic.com/en/library/edge/?source=SDK&id=waapi_index.html), 
which is maintained by Audiokinetic. Their documentation provides a complete list of functions and topics which are all 
supported and reflected by PyWwise.

## Modules

### Initialization: `pywwise`
This is where the factory function `new` exists; this functions establishes a connection with an instance of Wwise. 
When working with a single connection, the PyWwise convention is to name the connection "ak". Here is a simple example:

```python
import pywwise
from pywwise.types import SystemPath  # this is an alias of pathlib.Path, which is commonly used in PyWwise

ak = pywwise.new_waapi_connection()  # the default URL is "ws://127.0.0.1:8080/waapi"

path = SystemPath("C:/Users/leozin/Documents/WwiseTests/TestTone.wav")
ak.wwise.debug.generate_tone_wav(path)
```

### Core Types: `pywwise.types`
This is where helper types such as `Name`, `GUID`, `ShortID`, and `ProjectPath` exist. As you get familiar with PyWwise, 
you will notice that many functions use specialized PyWwise types instead of primitives such as `str`. This is to 
maximize readability and deploy some error checking (e.g. the constructor in `GUID` checks to see if the provided value 
is a valid GUID, in terms of format). Here is an example:

```python
import pywwise
from pywwise.types import GUID

ak = pywwise.new_waapi_connection()  # the default URL is "ws://127.0.0.1:8080/waapi"

# GUID will validate the value and throw a ValueError in case something is wrong
active_state: tuple[str, str] = ak.soundengine.get_state(GUID("{3182E70A-1CD2-4ABD-8652-EEA2E600E4A7}"))
print(active_state)
```

### Enumerations: `pywwise.enums`
PyWwise has many enumerations that help WAAPI users obey certain constraints of Wwise. Here is an example:

```python
import pywwise
from pywwise.enums import EBitDepth, ESampleRate  # common PyWwise enums to help with "quantized" parameters
from pywwise.types import SystemPath  # this is an alias of pathlib.Path, which is commonly used in PyWwise

ak = pywwise.new_waapi_connection()  # the default URL is "ws://127.0.0.1:8080/waapi"

path = SystemPath("C:/Users/leozin/Documents/WwiseTests/TestTone.wav")
bit_depth = EBitDepth.INT_16  # Wwise only supports 16-bit integer and 32-bit float; EBitDepth enumerates those options.
sample_rate = ESampleRate.SR_44100  # Wwise only supports certain sample rates; ESampleRate enumerates all options.

ak.wwise.debug.generate_tone_wav(path, bit_depth, sample_rate)
```

### Dataclasses: `pywwise.structs`
This is where object-oriented data containers live, in the form of dataclasses (a feature of Python). Examples include 
`Vector3` (which is commonly used to represent a point in 3D space) and `PlatformInfo` (which represents a platform 
entry in Wwise's Platform Manager).

```python
import pywwise
from pywwise.types import GameObjectID
from pywwise.structs import Vector3

ak = pywwise.new_waapi_connection()  # the default URL is "ws://127.0.0.1:8080/waapi"

# Position the Transport (Wwise Authoring's default game object) at the world's origin (centre) point.
ak.soundengine.set_position(GameObjectID.get_transport(), Vector3.get_zero(), Vector3.get_zero())
```
