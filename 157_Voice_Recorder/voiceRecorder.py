import pyaudio
import wave
import threading

# To export it as ann .exe
# pyinstaller --onefile .\voiceRecorder.py
# .exe file is in /dist folder

CHUNK = 1024  # Number of audio samples per frame
FORMAT = pyaudio.paInt16  # Audio format (16-bit signed integer)
CHANNELS = 1  # Mono audio
RATE = 44100  # Sampling rate in Hz

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open the audio stream
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("Recording started. Press 'q' to stop recording.")

frames = []  # Buffer to store audio frames
stop_recording = False  # Flag to indicate if recording should stop

def capture_audio():
    global stop_recording
    while not stop_recording:
        data = stream.read(CHUNK)
        frames.append(data)

# Start capturing audio in a separate thread
thread = threading.Thread(target=capture_audio)
thread.start()

# Wait for user to stop recording
while True:
    user_input = input()
    if user_input.lower() == 'q':
        stop_recording = True
        break

# Wait for the audio capture thread to finish
thread.join()

print("Recording finished.")

# Stop and close the audio stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio to a WAV file
output_file = "recorded.wav"
wf = wave.open(output_file, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print("Recording saved to", output_file)
