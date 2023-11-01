# About

gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate’s text-to-speech API. Writes spoken mp3 data to a file, a file-like object (bytestring) for further audio manipulation, or stdout. It features flexible pre-processing and tokenizing.

```cmd
pip install gTTS
```

We can run it on command line as well.
```cmd
gtts-cli "c'est la vie" --lang fr --output cestlavie.mp3
```
