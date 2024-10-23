@echo off
cd /d "%~dp0"
cd ..
streamlit run src/main.py
echo.
echo Press any key to close this window...
pause >nul