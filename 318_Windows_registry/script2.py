import winreg

path = winreg.HKEY_CURRENT_USER
BambaKey = winreg.OpenKeyEx(path, r"SOFTWARE\\BambaKey")

myvalue = winreg.QueryValueEx(BambaKey, "myval" )
myothervalue = winreg.QueryValueEx(BambaKey, "myothervalue" )

if BambaKey:
    winreg.CloseKey(BambaKey)

print(myvalue)
print(myothervalue)
print(myvalue[0])
print(myothervalue[0])