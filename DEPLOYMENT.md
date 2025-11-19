# 🚀 Deployment Guide - Get Your Portfolio Live!

## Option 1: Deploy to Heroku (Recommended - Easiest)

### Prerequisites
- Heroku account (free at https://www.heroku.com)
- GitHub account (free at https://github.com)

### Step-by-Step Deployment:

#### 1. **Create a GitHub Repository**
   - Go to https://github.com/new
   - Create a new repository called `portfolio`
   - Choose "Public" (so you can share it)
   - Click "Create repository"

#### 2. **Upload Your Project to GitHub**
   - On your GitHub repo page, click "Add file" → "Upload files"
   - Upload all files from your portfolio folder EXCEPT:
     - `.venv/` folder (the virtual environment)
     - `.env` file (your secret credentials)
   - Make sure to upload:
     - `app/` folder
     - `run.py`
     - `requirements.txt`
     - `Procfile`
     - `runtime.txt`
     - `.gitignore`
     - `README.md`
   - Add commit message: "Initial portfolio commit"
   - Click "Commit changes"

#### 3. **Connect Heroku to GitHub**
   - Go to https://www.heroku.com and login
   - Click "New" → "Create new app"
   - Enter app name: `suyog-portfolio` (or any unique name)
   - Choose region closest to you
   - Click "Create app"

#### 4. **Deploy from GitHub**
   - In your Heroku app, go to "Deploy" tab
   - Under "Deployment method", click "GitHub"
   - Search for your `portfolio` repository
   - Click "Connect"
   - Scroll down and click "Enable Automatic Deploys"
   - Click "Deploy Branch" (next to "main")

#### 5. **Set Environment Variables**
   - Go to "Settings" tab in your Heroku app
   - Click "Reveal Config Vars"
   - Add these variables:
     ```
     KEY: MAIL_USERNAME
     VALUE: yadavsuyog623@gmail.com
     
     KEY: MAIL_PASSWORD
     VALUE: mnclbcrhmkgoapwz
     
     KEY: SECRET_KEY
     VALUE: your-super-secret-key-change-this
     ```
   - Click "Add"

#### 6. **View Your Live Portfolio**
   - Go to "Open app" button (top right)
   - Your portfolio is now LIVE! 🎉
   - Share the URL with anyone

#### 7. **Update Your Portfolio (Auto-Deploy)**
   - Edit files in VS Code
   - Upload updated files to GitHub
   - Changes automatically deploy to Heroku! ✨

---

## Option 2: Deploy to Render (Free & Easy)

1. Go to https://render.com
2. Sign up with GitHub
3. Click "New" → "Web Service"
4. Connect your GitHub repository
5. Fill in:
   - **Name**: suyog-portfolio
   - **Build command**: `pip install -r requirements.txt`
   - **Start command**: `gunicorn run:app`
6. Add environment variables (same as Heroku)
7. Click "Create Web Service"

---

## Option 3: Deploy to PythonAnywhere (Easiest for Python)

1. Go to https://www.pythonanywhere.com
2. Create free account
3. Upload your project files
4. Create Web App with Flask
5. Configure WSGI file
6. Set environment variables
7. Reload web app

---

## How to Update Your Portfolio

### After Initial Deployment:

**If using Heroku + GitHub:**
1. Edit files in VS Code
2. Go to GitHub.com → Your portfolio repo
3. Click "Add file" → "Upload files"
4. Select your updated files
5. Commit with message: "Updated portfolio"
6. Heroku automatically deploys! ✨

**Changes appear live in ~1-2 minutes**

---

## Customize Your Portfolio

### Update Your Info:
Edit `app/routes.py` and update:
```python
PROJECTS = [...]  # Add your real projects
SKILLS = {...}    # Add your skills
```

### Update Contact Email:
In Heroku Settings → Config Vars, update `MAIL_USERNAME`

### Add Your Photo:
1. Save image to `app/static/images/profile.jpg`
2. Edit `app/templates/index.html`
3. Find the image line and update filename

---

## Your Live Portfolio URL

Once deployed on Heroku:
- **URL**: https://suyog-portfolio.herokuapp.com
- **Share this with**: Recruiters, employers, friends!

---

## Troubleshooting

### Heroku App Not Working?
- Check logs: Click "More" → "View logs"
- Verify all config vars are set
- Ensure `Procfile` and `runtime.txt` exist

### Email Not Sending?
- Verify `MAIL_USERNAME` and `MAIL_PASSWORD` in Heroku Config Vars
- Check app logs for errors

### Changes Not Reflecting?
- Make sure you uploaded to GitHub
- Wait 1-2 minutes for Heroku to redeploy
- Hard refresh browser (Ctrl+Shift+R)

---

## Cost

- **Heroku**: Free tier available (but limited)
- **Render**: Free tier available
- **PythonAnywhere**: Free tier available

For unlimited usage, upgrade to paid plans (~$5-10/month)

---

## Next Steps

1. ✅ Create GitHub account
2. ✅ Create Heroku account
3. ✅ Upload project to GitHub
4. ✅ Connect Heroku to GitHub
5. ✅ Deploy!
6. ✅ Share your live portfolio! 🎉

---

**Your portfolio is ready to go LIVE! 🚀**
