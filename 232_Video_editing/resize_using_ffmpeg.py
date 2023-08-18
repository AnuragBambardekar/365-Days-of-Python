import subprocess

input_video_path = "three.mp4"
output_video_path = "three_ffmpeg_resize.mp4"
new_width = 1280
new_height = 720

ffmpeg_cmd = [
    "ffmpeg",
    "-i", input_video_path,
    "-vf", f"scale={new_width}:{new_height}",
    "-c:a", "copy",
    output_video_path
]

# Run the ffmpeg command
subprocess.run(ffmpeg_cmd)
