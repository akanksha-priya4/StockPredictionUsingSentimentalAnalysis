@echo off
echo 🚀 Preparing Stock Analysis App for Vercel Deployment...
echo.

echo Step 1: Initializing Git repository...
git init
if %ERRORLEVEL% neq 0 (
    echo Error: Git not found. Please install Git first.
    pause
    exit /b 1
)

echo Step 2: Adding files to Git...
git add .

echo Step 3: Creating initial commit...
git commit -m "Initial commit: Stock Prediction & Financial Analysis App"

echo.
echo ✅ Git repository prepared!
echo.
echo Next steps:
echo 1. Create a new repository on GitHub
echo 2. Run: git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
echo 3. Run: git branch -M main
echo 4. Run: git push -u origin main
echo 5. Go to vercel.com and import your GitHub repository
echo.
echo See DEPLOYMENT_GUIDE.md for detailed instructions.
echo.
pause 