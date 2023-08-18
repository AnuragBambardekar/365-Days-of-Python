from moviepy.editor import VideoFileClip, clips_array

length=5

clip1 = VideoFileClip("./gen_vids/one_ffmpeg_resize.mp4").subclip(0,0+length).margin(2)
clip2 = VideoFileClip("./gen_vids/two_ffmpeg_resize.mp4").subclip(0,0+length).margin(2)
clip3 = VideoFileClip("./gen_vids/three_ffmpeg_resize.mp4").subclip(0,0+length).margin(2)

combined = clips_array([[clip1, clip2],
                        [clip3, clip1]])

combined.write_videofile("test.mp4")