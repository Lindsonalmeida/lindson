@echo off
REM Dublê - instalacao no Windows (RTX 3050). Precisa do Python 3.11 instalado (python.org, marque "Add to PATH").
cd /d "%~dp0"
if not exist venv py -3.11 -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install torch==2.6.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124
pip install -r requisitos.txt
echo.
echo Pronto. Para abrir, de dois cliques em abrir.bat
pause
