# Clipboard

A clipboard is a temporary storage area in a computer's memory that is used to store data that has been cut or copied from a document or application. This data can then be pasted into another location or application. The clipboard is a fundamental part of the copy-and-paste functionality in modern computer systems.

Here's how it typically works:

1. Cutting or Copying: When you cut or copy something (text, images, files, etc.) in an application, the data is placed on the clipboard.

2. Clipboard Storage: The clipboard temporarily holds the copied or cut data in a specific format.

3. Pasting: When you paste, the data on the clipboard is retrieved and placed in the location you choose.

For example, if you copy a piece of text from a document and then paste it into an email, you are using the clipboard. The clipboard allows for the transfer of data between different applications or within the same application.

In the context of programming, the clipboard is often accessed and manipulated using APIs (Application Programming Interfaces) provided by the operating system. Developers can use these APIs to interact with the clipboard, allowing their applications to support copy-and-paste functionality. The Win32 API on Windows and the NSPasteboard on macOS are examples of such APIs.

## Multiple Clipboards

- You can have a list of copied items and then select from it what you want to paste by just selecting the index.

```cmd
['win32clipboard.CloseClipboard()', '', '', '', '']
['win32clipboard.CloseClipboard()', 'data = win32clipboard.GetClipboardData()', '', '', '']
1
0
1
```