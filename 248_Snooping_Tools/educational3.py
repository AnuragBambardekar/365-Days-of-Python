import sounddevice as sd
import numpy as np
import wave

SAMPLE_RATE = 44100  
CHANNELS = 1  
DTYPE = np.int16  
RECORD_SECONDS = 5  
OUTPUT_FILENAME = "output.wav"  


print("Recording...")

audio_data = sd.rec(int(SAMPLE_RATE * RECORD_SECONDS), samplerate=SAMPLE_RATE, channels=CHANNELS, dtype=DTYPE)
sd.wait()  

print("Recording finished.")


with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio_data.dtype.itemsize)
    wf.setframerate(SAMPLE_RATE)
    wf.writeframes(audio_data.tobytes())

print(f"Audio saved to {OUTPUT_FILENAME}")
