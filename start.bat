@echo off
echo ==========================================
echo   Stock Prediction Application
echo ==========================================
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting application...
echo Open your browser and go to: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python app.py
pause 