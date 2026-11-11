@echo off
rem Robô SDR: abre sozinho quando o Windows liga (atalho na pasta Inicializar)
cd /d "%~dp0"
title Robo SDR
:loop
node robo.js
echo Robo parou. Reiniciando em 1 minuto...
timeout /t 60 >nul
goto loop
