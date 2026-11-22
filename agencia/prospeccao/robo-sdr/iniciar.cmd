@echo off
rem Robô SDR (modo manual). Uso: iniciar.cmd sdr2   (sem nada = sdr1). O instalar.cmd cria iniciar-sdr1/2/3.cmd com caminho absoluto.
rem Não copie este arquivo para a pasta Inicializar: lá vai só o ATALHO que o instalador cria.
if not exist "%~dp0robo.js" (echo Este arquivo foi copiado para fora da pasta do robo. Rode o instalar.cmd na pasta robo-sdr. & pause & exit /b 1)
set N=%1
if "%N%"=="" set N=sdr1
cd /d "%~dp0"
title Robo %N%
:loop
node "%~dp0robo.js" --numero %N%
timeout /t 60 >nul
goto loop
