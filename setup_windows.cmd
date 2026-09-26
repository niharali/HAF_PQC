@echo off

echo ===================================
echo HAF-PQC Windows Setup
echo ===================================


python -m venv venv


call venv\Scripts\activate


python -m pip install --upgrade pip


pip install -r requirements.txt


echo.
echo Setup completed successfully
echo.

pause