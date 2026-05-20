@echo off

cls

call "%~dp0.venv\Scripts\activate.bat"
python "%~dp0main.py"

pause