from moviepy.editor import *

# Load video clips
clip1 = VideoFileClip("126_Merge_video_clips/cat.mp4")
clip2 = VideoFileClip("126_Merge_video_clips/cat2.mp4")

# Concatenate video clips
final_clip = concatenate_videoclips([clip1, clip2])

# Save final clip
final_clip.write_videofile("126_Merge_video_clips/merged_cat.mp4")

from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

# Set the file paths for the input videos and the output video
input_video_1 = '126_Merge_video_clips/cat.mp4'
input_video_2 = '126_Merge_video_clips/cat2.mp4'
output_video = '126_Merge_video_clips/merged_cat.mp4'

# Load the input videos
clip1 = VideoFileClip(input_video_1)
clip2 = VideoFileClip(input_video_2)

# Set the size of the final video
final_clip = concatenate_videoclips([clip1, clip2], method="compose")
final_clip.resize(width=1920)

# Merge the input videos horizontally and write the output video to file
final_clip.write_videofile(output_video, codec='libx264', audio_codec='aac')
