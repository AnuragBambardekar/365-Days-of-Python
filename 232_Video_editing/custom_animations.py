from moviepy.editor import *
import numpy as np
import math

import cv2

video_clip = VideoFileClip("./gen_vids/combined.mp4")
image_clip = ImageClip("./gen_vids/dog.png").set_duration(video_clip.duration)

# Open the video file
input_video_path = "./gen_vids/combined.mp4"
cap = cv2.VideoCapture(input_video_path)

# Get the original video's width and height
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"Input Video Resolution: {width},{height}")

center_x = video_clip.size[0]/2 - image_clip.size[0]/2
center_y = video_clip.size[1]/2 - image_clip.size[1]/2
radius = 200

def simple_motion(t):
    # t is current position (in seconds) on video
    # use this paramater to define some movement
    # return 0,0
    # return t*5, t*5
    return (t/ video_clip.duration) * 1280, (t/video_clip.duration) * 720 # lets go from upper left corner to lower right corner

def circular_motion(t):
    # to increase rotation speed, change 2pi to 4pi
    return center_x + radius * np.cos((t/video_clip.duration) * 2 * math.pi), center_y + radius * np.sin((t/video_clip.duration) * 2 * math.pi) # make the image go in a circle

image_clip = image_clip.set_position(simple_motion) # it is moving upper left corner of image (0,0)
# image_clip = image_clip.set_position(circular_motion)

final_clip = CompositeVideoClip([video_clip, image_clip])
final_clip.write_videofile("./gen_vids/output_simple.mp4", fps=video_clip.fps)