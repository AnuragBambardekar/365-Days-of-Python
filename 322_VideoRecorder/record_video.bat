@echo off

ffmpeg -f dshow ^
-s 1280x720 -r 30 ^
-vcodec mjpeg ^
-i video="HP Wide Vision HD Camera" output.avi