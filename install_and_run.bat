@echo off
echo ==========================================
echo   Stock Prediction Application Setup
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo ✓ Python is already installed
    goto :install_packages
)

py --version >nul 2>&1
if %errorlevel% == 0 (
    echo ✓ Python is already installed (using py launcher)
    set PYTHON_CMD=py
    goto :install_packages
)

echo ❌ Python is not installed or not in PATH
echo.
echo Please install Python first:
echo 1. Go to https://python.org/downloads/
echo 2. Download Python 3.8 or higher
echo 3. During installation, CHECK "Add Python to PATH"
echo 4. Restart your computer after installation
echo 5. Run this script again
echo.
pause
exit /b 1

:install_packages
echo.
echo 📦 Installing required packages...
if defined PYTHON_CMD (
    %PYTHON_CMD% -m pip install --upgrade pip
    %PYTHON_CMD% -m pip install Flask yfinance pandas numpy plotly requests beautifulsoup4 textblob matplotlib seaborn scikit-learn
) else (
    python -m pip install --upgrade pip
    python -m pip install Flask yfinance pandas numpy plotly requests beautifulsoup4 textblob matplotlib seaborn scikit-learn
)

if %errorlevel% neq 0 (
    echo ❌ Failed to install packages
    echo Try running as administrator or check your internet connection
    pause
    exit /b 1
)

echo ✅ All packages installed successfully!
echo.

:run_app
echo 🚀 Starting the Stock Prediction Web Application...
echo.
echo ┌─────────────────────────────────────────────┐
echo │  🌐 Open your browser and go to:           │
echo │  http://localhost:5000                     │
echo │                                             │
echo │  Press Ctrl+C to stop the server          │
echo └─────────────────────────────────────────────┘
echo.

if defined PYTHON_CMD (
    %PYTHON_CMD% app.py
) else (
    python app.py
)

pause 