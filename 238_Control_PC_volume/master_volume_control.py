# pip install comtypes
# pip install pycaw

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

# Get the volume interface
volume = cast(interface, POINTER(IAudioEndpointVolume))

# volume.SetMasterVolumeLevel(-18.0, None) # -65 to 0 is the range
# volume.SetMute(1, None) # Mute
# volume.SetMute(0, None) # Unmute

current = volume.GetMasterVolumeLevel()
volume.SetMasterVolumeLevel(current+6.0, None)
