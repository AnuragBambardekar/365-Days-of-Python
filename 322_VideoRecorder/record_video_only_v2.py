# ffmpeg -list_devices true -f dshow -i dummy
# ffmpeg -f dshow -list_options true -i video="HP Wide Vision HD Camera"
# ffmpeg -f dshow -s 1280x720 -r 30 -vcodec mjpeg -i video="HP Wide Vision HD Camera" output.avi

import subprocess

# Specify the path to your batch file
batch_file_path = 'record_video.bat'

# Use subprocess to run the batch file
try:
    subprocess.run([batch_file_path], check=True)
    print("Batch file executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing the batch file: {e}")