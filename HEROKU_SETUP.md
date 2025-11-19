# 🚀 Heroku Deployment - Step by Step

## Your GitHub Repository
- **URL**: https://github.com/suyogyadav404/MyPortfolio
- **Status**: ✅ Pushed and ready

## Step 1: Create Heroku Account (5 minutes)

1. Go to https://www.heroku.com
2. Click "Sign Up"
3. Fill in:
   - Email: yadavsuyog623@gmail.com
   - Password: (create strong password)
   - First Name: Suyog
4. Check email and verify
5. You'll be directed to Dashboard

## Step 2: Create Heroku App (2 minutes)

1. In Heroku Dashboard, click "Create new app"
2. Fill in:
   - **App name**: suyog-portfolio (or choose your own unique name)
   - **Region**: Select closest to your location (US or Europe)
3. Click "Create app"
4. You'll see your app dashboard

## Step 3: Connect GitHub to Heroku (5 minutes)

1. In your app dashboard, click **"Deploy"** tab
2. Under "Deployment method":
   - Click **"GitHub"**
   - Click **"Connect to GitHub"** button
   - Sign in with GitHub if asked
3. Under "Connect to GitHub":
   - Search for: **MyPortfolio**
   - Click **"Connect"** next to it

## Step 4: Enable Automatic Deployments (2 minutes)

1. Scroll down to "Automatic deploys"
2. Select branch: **main**
3. Check: "Wait for CI to pass before deploy"
4. Click **"Enable Automatic Deploys"**

This means every time you push to GitHub, Heroku automatically deploys!

## Step 5: Deploy Your App (3 minutes)

1. Scroll to "Manual deploy"
2. Click **"Deploy Branch"** (next to "main")
3. Watch the logs scroll by - your app is building!
4. Wait for message: "Your app was successfully deployed"

## Step 6: Configure Email (3 minutes)

1. Click **"Settings"** tab
2. Click **"Reveal Config Vars"**
3. Add these variables (click "Add" after each):

```
KEY: MAIL_USERNAME
VALUE: yadavsuyog623@gmail.com

KEY: MAIL_PASSWORD
VALUE: mnclbcrhmkgoapwz

KEY: SECRET_KEY
VALUE: suyog-portfolio-secret-2024-production
```

4. After adding all 3, go back to **Deploy** tab
5. Click **"Deploy Branch"** again to restart with new config

## Step 7: View Your Live Portfolio! 🎉

1. In top right, click **"Open app"** button
2. Your portfolio opens in browser!
3. **Copy the URL** - this is your live portfolio
4. Test the contact form to verify it works

## That's It! You're Live! 🌐

Your portfolio is now accessible from anywhere!

### What You Can Now Do:

**Share Your Portfolio:**
- Send the Heroku URL to recruiters, friends, employers
- Add to your resume
- Post on LinkedIn
- Include in job applications

**Make Updates:**
1. Edit files in VS Code
2. Run: `git add -A`
3. Run: `git commit -m "Updated projects"`
4. Run: `git push origin main`
5. Heroku auto-deploys in 1-2 minutes! ✨

**Update Your Portfolio Content:**

Edit `app/routes.py`:
```python
PROJECTS = [
    {
        'title': 'Your Project Name',
        'description': 'What it does',
        'technologies': ['Python', 'Flask'],
        'link': 'https://github.com/...'
    }
]
```

Edit `app/templates/index.html`:
- Change your name and title
- Add your profile image
- Update social media links

Edit `app/static/css/style.css`:
- Change colors
- Modify fonts
- Adjust spacing

---

**Questions? Check QUICK_START.md or DEPLOYMENT.md**

You're all set! 🚀
