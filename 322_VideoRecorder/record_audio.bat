@echo off

chcp 65001

ffmpeg -f dshow ^
-i audio="Microphone Array (Intel® Smart Sound Technology for Digital Microphones)" ^
-t 60 recording.wav
