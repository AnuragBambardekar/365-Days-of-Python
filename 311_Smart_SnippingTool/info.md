# About Smart Snipping Tool

This is a simple Python application that allows you to capture a region of your screen, perform optical character recognition (OCR) using Tesseract, and display the detected text. Additionally, it provides a "Quit" button and allows you to quit the application by pressing 'q' or the Esc key.

## Features

- Screen capturing using a crosshair selection
- Optical Character Recognition (OCR) for detected text
- "Quit" button to exit the application
- Keyboard shortcuts for quitting (press 'q' or the Esc key)

## Requirements

- Python 3.x
- PyQt5
- OpenCV (cv2)
- Tesseract OCR (tesseract.exe)

## Tesseract Installation
Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and "read" the text embedded in images.

Python-tesseract is a wrapper for Google's Tesseract-OCR Engine. 

- Install Google Tesseract OCR engine for Windows from here: https://tesseract-ocr.github.io/tessdoc/Installation.html

## Note
- Ensure Tesseract OCR is installed and set the path to its executable in the code:
```py
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

## Running the script

The screen capture interface will appear. Use the crosshair cursor to select a region of your screen.

The captured image will be displayed, and the detected text will be printed with the "Detected Text" label in red and the text in green.

To exit the application, you can click the "Quit" button or use the keyboard shortcuts ('q' or Esc).

## Acknowledgments
This application was created with the help of PyQt5, OpenCV, Pillow, and Tesseract OCR.

Feel free to modify and enhance the code to fit your specific needs.

## Future Work
- Smart Video Snipping Tool
- Neater GUI
- Save image and OCR'ed Text

## References
- https://github.com/harupy/snipping-tool/blob/master/snipping_tool.py - Snipping tool Code <br>