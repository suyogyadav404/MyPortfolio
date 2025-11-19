@echo off
REM Portfolio Deployment Setup Script
REM This script initializes Git and pushes your portfolio to GitHub

setlocal enabledelayedexpansion

echo.
echo ╔════════════════════════════════════════════════════════════╗
echo ║         PORTFOLIO DEPLOYMENT SETUP                         ║
echo ║                                                            ║
echo ║  This script will:                                         ║
echo ║  1. Initialize Git repository                             ║
echo ║  2. Add all files                                          ║
echo ║  3. Commit changes                                         ║
echo ║  4. Connect to GitHub                                      ║
echo ║  5. Push to GitHub                                         ║
echo ╚════════════════════════════════════════════════════════════╝
echo.

REM Check if Git is installed
where git >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Git is not found in PATH. Please restart PowerShell/CMD and try again.
    echo.
    pause
    exit /b 1
)

echo ✅ Git is installed: 
git --version
echo.

REM Get GitHub information
set /p GITHUB_USERNAME="Enter your GitHub username: "
set /p GITHUB_TOKEN="Enter your GitHub Personal Access Token (or password): "
set /p GITHUB_REPO="Enter your GitHub repository name (e.g., portfolio): "

REM Initialize Git
echo.
echo [1/5] Initializing Git repository...
if exist .git (
    echo ℹ️  Git repository already exists
) else (
    git init
    echo ✅ Git repository initialized
)

echo.
echo [2/5] Configuring Git user...
git config user.name "Suyog"
git config user.email "yadavsuyog623@gmail.com"
echo ✅ Git configured

echo.
echo [3/5] Adding files to Git...
git add -A
echo ✅ Files added

echo.
echo [4/5] Creating initial commit...
git commit -m "Initial portfolio commit"
echo ✅ Commit created

echo.
echo [5/5] Connecting to GitHub and pushing...
echo.
echo Setting remote repository...
git remote remove origin >nul 2>&1
git remote add origin https://%GITHUB_USERNAME%:%GITHUB_TOKEN%@github.com/%GITHUB_USERNAME%/%GITHUB_REPO%.git

echo Pushing to GitHub...
git branch -M main
git push -u origin main

if %ERRORLEVEL% EQ 0 (
    echo.
    echo ╔════════════════════════════════════════════════════════════╗
    echo ║            ✅ DEPLOYMENT SETUP COMPLETE! ✅                ║
    echo ╚════════════════════════════════════════════════════════════╝
    echo.
    echo Your portfolio has been pushed to GitHub!
    echo.
    echo 📍 Repository: https://github.com/%GITHUB_USERNAME%/%GITHUB_REPO%
    echo.
    echo Next steps:
    echo 1. Go to https://www.heroku.com
    echo 2. Create a new app
    echo 3. Connect it to your GitHub repository
    echo 4. Enable automatic deployments
    echo 5. Set environment variables in Heroku settings
    echo.
    echo Your portfolio will be live in minutes!
    echo.
) else (
    echo.
    echo ❌ Failed to push to GitHub
    echo Please check your username, token, and repository name
    echo.
)

pause
