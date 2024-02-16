@echo off
echo Setting up Python virtual environment...

python -m venv venv

REM Activate the virtual environment on Windows
venv\Scripts\activate

pip install -r .pysetup

echo Done setting up a Python environment.
pause