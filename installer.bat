@echo off
setlocal

:: Check Python version
for /f "tokens=2 delims= " %%a in ('python --version 2^>^&1') do set pyver=%%a
if "%pyver%"=="3.11.7" (
    echo Found Python 3.11.7
) else (
    echo Python 3.11.7 is required. Please install it from https://www.python.org/downloads/release/python-3117/
    exit /b 1
)

:: Install GitPython
echo Installing GitPython...
python -m pip install GitPython

echo Done.
endlocal
