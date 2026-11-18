@echo off
rem Duplo clique para instalar o MotionForge (sem administrador).
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0instalar-windows.ps1" %*
pause
