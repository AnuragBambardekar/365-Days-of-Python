@echo off
setlocal enabledelayedexpansion
set chars=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()
set password=
set length=12

:generate
set /a rand=!random! %% 82
set /a idx=rand %% 82
for /l %%i in (!idx!,1,!idx!) do (
    set password=!password!!chars:~%%i,1!
)
set /a length-=1
if !length! gtr 0 goto generate

echo Generated Password: %password%
pause
