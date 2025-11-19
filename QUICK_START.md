# 🚀 Quick Start: Push to GitHub & Deploy

## Prerequisites
- GitHub account (https://github.com)
- Heroku account (https://www.heroku.com)

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Fill in:
   - **Repository name**: `portfolio`
   - **Visibility**: Public
   - **Do NOT check** "Initialize with README"
3. Click "Create repository"
4. You'll see a page with your repository URL

## Step 2: Generate GitHub Personal Access Token

1. Go to https://github.com/settings/tokens/new
2. Fill in:
   - **Note**: Portfolio deployment
   - **Expiration**: 90 days
   - **Select scopes**: Check `repo` (full control of private repositories)
3. Click "Generate token"
4. **COPY the token** (you won't see it again!)

## Step 3: Run Deployment Script

Open PowerShell in your portfolio folder and run:

```powershell
.\deploy.ps1
```

Or use the batch file:
```cmd
deploy.bat
```

**The script will ask you:**
- GitHub username (e.g., `suyog123`)
- Repository name (e.g., `portfolio`)
- GitHub Personal Access Token (the one you just created)

## Step 4: Connect Heroku to GitHub

1. Go to https://www.heroku.com
2. Login to your account
3. Click "Create new app"
4. Fill in app name: `suyog-portfolio` (must be unique)
5. Click "Create app"

### In Deploy Tab:
1. Click "GitHub" under Deployment method
2. Connect to GitHub (login if needed)
3. Search for `portfolio` repository
4. Click "Connect"
5. Check "Enable Automatic Deploys"
6. Click "Deploy Branch"

### In Settings Tab:
1. Click "Reveal Config Vars"
2. Add these variables:

```
MAIL_USERNAME = yadavsuyog623@gmail.com
MAIL_PASSWORD = mnclbcrhmkgoapwz
SECRET_KEY = suyog-portfolio-secret-2024-production
```

3. Click "Deploy Branch" again in Deploy tab

## Step 5: Your Portfolio is LIVE! 🎉

Your portfolio is now accessible at:
```
https://suyog-portfolio.herokuapp.com
```

(Replace `suyog-portfolio` with your actual app name)

## Making Updates (Future)

Every time you want to update your portfolio:

### Option 1: Via GitHub Web (Easiest)
1. Go to your GitHub repo
2. Click "Add file" → "Upload files"
3. Select updated files
4. Commit with a message
5. **Heroku automatically deploys!** ✨

### Option 2: Via Git Command
```powershell
cd c:\Users\Suyog\Desktop\portfolio

# Make your changes in VS Code

# Then run:
git add -A
git commit -m "Updated my projects section"
git push origin main
```

Heroku will automatically redeploy (1-2 minutes).

## Useful Commands

```powershell
# Check git status
git status

# See your commits
git log --oneline

# View what changed
git diff

# Undo last commit (keep changes)
git reset --soft HEAD~1

# See all remotes
git remote -v
```

## Troubleshooting

**Portfolio not showing up?**
- Wait 2-3 minutes for Heroku to finish deploying
- Check Heroku logs: Dashboard → "More" → "View logs"
- Restart the app: "More" → "Restart dynos"

**Changes not appearing?**
- Wait 2 minutes for automatic redeploy
- Hard refresh browser: Ctrl+Shift+R
- Check GitHub shows your latest commit

**Email not working?**
- Verify environment variables in Heroku Settings
- Check that MAIL_USERNAME and MAIL_PASSWORD are set
- Restart the app

**Permission denied when pushing?**
- Verify your GitHub token is valid
- Make sure repository exists
- Try `git push -u origin main` again

## Files You Changed
- `.env` - Email configuration (DO NOT upload to GitHub)
- `app/routes.py` - Updated with email configuration
- `app/__init__.py` - Updated with environment variables
- `requirements.txt` - Added gunicorn
- `Procfile` - New for Heroku
- `runtime.txt` - New for Heroku
- `.gitignore` - New to protect secrets

## What Gets Uploaded to GitHub

**YES:**
- `app/` folder
- `run.py`
- `requirements.txt`
- `Procfile`
- `runtime.txt`
- `README.md`
- `DEPLOYMENT.md`
- `.gitignore`

**NO (Protected):**
- `.env` - Your email credentials
- `.venv/` - Virtual environment
- `__pycache__/` - Cache files

---

**You're all set! Your portfolio is live! 🚀**
