# PyWwise

PyWwise is an open-source Python wrapper around the Wwise Authoring Application Programming Interface (WAAPI). PyWwise 
is meant to make Wwise scripting (e.g. automation, data validation, etc.) much easier to achieve. There are multiple 
benefits in using PyWwise; the three main highlights are:

- Pythonic Architecture
- Object-Oriented
- Fully Documented

## Installation

PyWwise is available on the [Python Package Index](https://pypi.org/project/pywwise/), and so it is recommended to install it via `pip`. Using CMD, 
Terminal, PowerShell, or any command-line interface of your choice, run the command `pip install pywwise` to install 
the latest version of PyWwise.

## Usage

Getting started with PyWwise is easy: the first step is always to import `pywwise` and initialize a WAAPI connection to 
an instance of Wwise using the factory function `new_waapi_connection`. PyWwise is fully documented, so each function 
or topic will let you know what will be needed. Using an IDE like JetBrains PyCharm Community is recommended.

Since PyWwise is based on WAAPI and the [`waapi-client`](https://pypi.org/project/waapi-client/) package, you may also 
use the official [Wwise Authoring API Reference](https://www.audiokinetic.com/library/edge/?source=SDK&id=waapi_index.html), which is maintained by Audiokinetic. Their documentation provides 
a complete list of functions and topics which are all supported and reflected by PyWwise.

## Modules

The root module `pywwise` is where the factory function `new_waapi_connection` exists; this functions establishes a 
connection with an instance of Wwise. When working with a single connection, the PyWwise convention is to name the 
connection "ak". Here is a simple example:

```python
import pywwise

ak = pywwise.new_waapi_connection()  # the default URL is "ws://127.0.0.1:8080/waapi"
path = pywwise.SystemPath("C:/Users/leozin/Documents/WwiseTests/TestTone.wav")  # SystemPath is an alias of pathlib.Path
ak.wwise.debug.generate_tone_wav(path)  # this will output a WAV file containing a tone!
ak.disconnect()
```

Alternatively, you may use a `with` statement for context management, so the connection to Wwise is automatically closed 
once the `with` block is done. Here is a variation on the previous example:

```python
from pywwise import new_waapi_connection, SystemPath

with new_waapi_connection() as ak:  # the default URL is "ws://127.0.0.1:8080/waapi"
    path = SystemPath("C:/Users/leozin/Documents/WwiseTests/TestTone.wav")  # SystemPath is an alias of pathlib.Path
    ak.wwise.debug.generate_tone_wav(path)  # this will output a WAV file containing a tone!
```

Inside the root module `pywwise`, you will find **any** PyWwise core type, enum, etc. meant for end-users. It is also 
possible to import those directly from PyWwise's submodules, but that is not necessary.

## Examples

### Getting the active State from the sound engine
As you get familiar with PyWwise, you will notice that many functions use specialized PyWwise types for params/args 
instead of primitives such as `str`. This is to maximize readability, allow type-matched behaviours, and deploy some 
error checking (e.g. the constructor in `GUID` checks to see if the provided value is a valid GUID, in terms of format). 
Here is an example showcasing `GUID`:

```python
from pywwise import new_waapi_connection, GUID

with new_waapi_connection() as ak:  # the default URL is "ws://127.0.0.1:8080/waapi"
    wwise_obj_guid = GUID("{3182E70A-1CD2-4ABD-8652-EEA2E600E4A7}")  # if the GUID is invalid, a ValueError is thrown
    active_state: tuple[str, str] = ak.soundengine.get_state(wwise_obj_guid)  # the type hint is for readability only
    print(active_state)
```

Other common primitive-like types are `Name`, `ShortID`, `ProjectPath`, `PlayingID`, and `GameObjectID`. Some of those 
have member functions to check validity or get common "default" values.

### Generating a tone WAV
PyWwise has many enumerations that help WAAPI users obey certain constraints of Wwise (e.g. "quantized" parameters; in 
other words, parameters that only accept certain values). Here is an example showcasing `EBitDepth` and `ESampleRate`:

```python
from pywwise import new_waapi_connection, EBitDepth, ESampleRate, SystemPath

with new_waapi_connection() as ak:  # the default URL is "ws://127.0.0.1:8080/waapi"

    output_path = SystemPath("C:/Users/leozin/Documents/WwiseTests/TestTone.wav")
    bit_depth = EBitDepth.INT_16  # Wwise only supports 16-bit integer and 32-bit float; EBitDepth enumerates those options.
    sample_rate = ESampleRate.SR_44100  # Wwise only supports certain sample rates; ESampleRate enumerates all options.
    
    ak.wwise.debug.generate_tone_wav(output_path, bit_depth, sample_rate)
```

### Setting the position of a GameObject in the sound engine
PyWwise also has tons of dataclasses - classes that are primarily containers of data. Good examples are `Vector3` 
(commonly used to represent a point in 3D space) and `PlatformInfo` (represents a platform entry in Wwise's Platform 
Manager). Here is example using `Vector3`:

```python
from pywwise import new_waapi_connection, GameObjectID, Vector3

with new_waapi_connection() as ak: # the default URL is "ws://127.0.0.1:8080/waapi"

    # Position the Transport (Wwise Authoring's default game object) at the world's origin (centre) point.
    ak.soundengine.set_position(GameObjectID.get_transport(), Vector3.get_zero(), Vector3.get_zero())
```
