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

:: Check for default values in appsettings.json
set "defaultsFound=0"
findstr /c:"\"PAT\": \"your_personal_access_token_here\"" appsettings.json > nul && (echo Make sure PAT is updated from the default value. && set "defaultsFound=1")
findstr /c:"\"Organization\": \"organization\"" appsettings.json > nul && (echo Make sure Organization is updated from the default value. && set "defaultsFound=1")
findstr /c:"\"Project\": \"project\"" appsettings.json > nul && (echo Make sure Project is updated from the default value. && set "defaultsFound=1")
findstr /c:"\"Repo\": \"repo\"" appsettings.json > nul && (echo Make sure Repo is updated from the default value. && set "defaultsFound=1")

if "%defaultsFound%"=="1" (
    echo One or more default values are not updated in appsettings.json. Please update them before proceeding.
    exit /b 1
)

:: Install GitPython
echo Installing GitPython...
python -m pip install GitPython

:: Install BS4
echo Installing BS4...
python -m pip install beautifulsoup4

:: Failsafe
python -m pip install -r requirements.txt

echo Done.
endlocal
