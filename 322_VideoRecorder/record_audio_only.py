# Check devices
# ffmpeg -list_devices true -f dshow -i dummy

# Record Audio only
# ffmpeg -f dshow -i audio="Microphone Array (Intel® Smart Sound Technology for Digital Microphones)" -t 60 output.wav

# import subprocess

# def list_audio_devices():
#     cmd = ['ffmpeg', '-list_devices', 'true', '-f', 'dshow', '-i', 'dummy']
#     subprocess.run(cmd)

# def record_audio(device_name, duration, output_file):
#     cmd = ['ffmpeg', '-f', 'dshow', '-i', f'audio="{device_name}"', '-t', str(duration), output_file]
#     subprocess.run(cmd)

# # Example usage:
# # List available audio devices
# list_audio_devices()

# # Record audio for 60 seconds from a specific device
# device_name = "Microphone Array (Intel® Smart Sound Technology for Digital Microphones)"
# output_file = "output.wav"
# record_duration = 60

# record_audio(device_name, record_duration, output_file)


"""
Applied this fix:
https://techblog.dev/posts/2022/11/fix-ffmpeg-could-not-find-device-with-name-dshow-error-windows/
"""

import subprocess

# Specify the path to your batch file
batch_file_path = 'record_audio.bat'

# Use subprocess to run the batch file
try:
    subprocess.run([batch_file_path], check=True)
    print("Batch file executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing the batch file: {e}")
