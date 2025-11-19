# Deploy to PythonAnywhere - Step by Step

## Step 1: Create Account
1. Go to https://www.pythonanywhere.com
2. Click **"Create a free account"**
3. Fill in username, email, password
4. Click **"Register"**
5. Verify your email

## Step 2: Clone Your Repository
1. Click **"Consoles"** in the top menu
2. Click **"Bash"** to open a terminal
3. Run this command:
```bash
git clone https://github.com/suyogyadav404/MyPortfolio.git
```
4. Wait for it to finish (should say "done")

## Step 3: Install Dependencies
Still in the Bash console, run:
```bash
cd MyPortfolio
pip install -r requirements.txt
```
Wait for all packages to install.

## Step 4: Create Web App
1. Click **"Web"** in the top menu
2. Click **"+ Add a new web app"**
3. Choose **"Flask"**
4. Choose **"Python 3.10"**
5. You'll see a path - edit it to:
```
/home/YOUR_USERNAME/MyPortfolio
```
(Replace YOUR_USERNAME with your PythonAnywhere username)

6. Click **"Next"**

## Step 5: Configure Flask App
1. In the Web tab, find the section "Code" 
2. Click the link under "WSGI configuration file"
3. Replace the entire content with:
```python
import os
import sys

path = '/home/YOUR_USERNAME/MyPortfolio'
if path not in sys.path:
    sys.path.append(path)

from wsgi import app
```
(Replace YOUR_USERNAME with your actual username)

4. Click the **"Save"** button at the top right

## Step 6: Reload Web App
1. Go back to the **"Web"** tab
2. Click the green **"Reload"** button
3. Wait 5-10 seconds

## Step 7: Visit Your Live Site!
Your portfolio is now live at:
```
https://YOUR_USERNAME.pythonanywhere.com
```

## Optional: Add Environment Variables (for email)
1. Go to **"Files"** tab
2. Create/edit `.env` file with:
```
SECRET_KEY=your-secret-key
MAIL_USERNAME=yadavsuyog623@gmail.com
MAIL_PASSWORD=mnclbcrhmkgoapwz
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
```
3. Go back to **Web** → click **Reload**

Your portfolio is live! 🎉
