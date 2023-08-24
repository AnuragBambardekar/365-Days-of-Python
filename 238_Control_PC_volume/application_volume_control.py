from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

# Get the volume interface
volume = cast(interface, POINTER(IAudioEndpointVolume))

sessions = AudioUtilities.GetAllSessions()

for session in sessions:
    volume = session._ctl.QueryInterface(ISimpleAudioVolume)
    
    # Get all sessions using the volume interface
    # if session.Process:
    #     print(session.Process.name())
    
    if session.Process and session.Process.name() == "msedge.exe":
        volume.SetMasterVolume(0.5,None) # specify the volume relative to master volume (1=100%, 0.5=50%)