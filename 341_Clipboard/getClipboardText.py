import ctypes
from ctypes import wintypes

# Constants
CF_TEXT = 1

# Function prototypes
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

OpenClipboard = user32.OpenClipboard
OpenClipboard.argtypes = [wintypes.HWND]
OpenClipboard.restype = ctypes.wintypes.BOOL

CloseClipboard = user32.CloseClipboard
CloseClipboard.argtypes = []
CloseClipboard.restype = ctypes.wintypes.BOOL

GetClipboardData = user32.GetClipboardData
GetClipboardData.argtypes = [wintypes.UINT]
GetClipboardData.restype = wintypes.HANDLE

GlobalLock = kernel32.GlobalLock
GlobalLock.argtypes = [wintypes.HANDLE]
GlobalLock.restype = ctypes.c_void_p

GlobalUnlock = kernel32.GlobalUnlock
GlobalUnlock.argtypes = [wintypes.HANDLE]
GlobalUnlock.restype = wintypes.BOOL

# Function to get text from the clipboard
def get_clipboard_text():
    try:
        # Open the clipboard
        if not OpenClipboard(0):
            raise ctypes.WinError()

        # Get clipboard data
        handle = GetClipboardData(CF_TEXT)
        if not handle:
            raise ctypes.WinError()

        # Lock the memory and retrieve the data
        locked_memory = GlobalLock(handle)
        clipboard_text = ctypes.c_char_p(locked_memory).value
        GlobalUnlock(handle)

        return clipboard_text.decode('utf-8')

    finally:
        # Close the clipboard
        CloseClipboard()

# Example usage
try:
    clipboard_text = get_clipboard_text()
    print(f"Clipboard text: {clipboard_text}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
