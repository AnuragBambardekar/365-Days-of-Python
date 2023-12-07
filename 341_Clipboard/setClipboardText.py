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

EmptyClipboard = user32.EmptyClipboard
EmptyClipboard.argtypes = []
EmptyClipboard.restype = ctypes.wintypes.BOOL

SetClipboardData = user32.SetClipboardData
SetClipboardData.argtypes = [wintypes.UINT, wintypes.HANDLE]
SetClipboardData.restype = wintypes.HANDLE

GlobalAlloc = kernel32.GlobalAlloc
GlobalAlloc.argtypes = [wintypes.UINT, ctypes.c_size_t]
GlobalAlloc.restype = wintypes.HANDLE

GlobalLock = kernel32.GlobalLock
GlobalLock.argtypes = [wintypes.HANDLE]
GlobalLock.restype = ctypes.c_void_p

GlobalUnlock = kernel32.GlobalUnlock
GlobalUnlock.argtypes = [wintypes.HANDLE]
GlobalUnlock.restype = wintypes.BOOL

# Main function to set text on the clipboard
def set_clipboard_text(text):
    # Open the clipboard
    if not OpenClipboard(0):
        raise ctypes.WinError()

    try:
        # Empty the clipboard
        EmptyClipboard()

        # Allocate global memory
        data = text.encode('utf-8')
        handle = GlobalAlloc(0x2000, len(data) + 1)  # GMEM_MOVEABLE

        if handle:
            # Lock the memory and copy the data
            locked_memory = GlobalLock(handle)
            ctypes.memmove(locked_memory, data, len(data))
            GlobalUnlock(handle)

            # Set clipboard data
            SetClipboardData(CF_TEXT, handle)
        else:
            raise ctypes.WinError()
    finally:
        # Close the clipboard
        CloseClipboard()

# Example usage
set_clipboard_text("Hello, Clipboard! - YOLO")
