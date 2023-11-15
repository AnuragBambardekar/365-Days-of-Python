# Run regedit to open up the registry

# utility: to save and load configurations
import winreg

path = winreg.HKEY_CURRENT_USER
software = winreg.OpenKeyEx(path, r"SOFTWARE\\")

# Make a new key
new_key = winreg.CreateKey(software, "BambaKey")
winreg.SetValueEx(new_key, "myval", 0, winreg.REG_SZ, "Hello World")
winreg.SetValueEx(new_key, "myothervalue", 0, winreg.REG_SZ, "20")

if new_key:
    winreg.CloseKey(new_key)