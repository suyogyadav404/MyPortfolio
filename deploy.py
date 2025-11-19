#!/usr/bin/env python3
"""
Interactive deployment helper for portfolio
This script guides you through the deployment process
"""

def print_section(title):
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60 + "\n")

def step_1_github():
    print_section("STEP 1: Create GitHub Repository")
    print("""
1. Go to https://github.com/new
2. Fill in:
   - Repository name: portfolio
   - Description: My personal portfolio website
   - Visibility: Public
   - Do NOT initialize with README (we have one)
3. Click "Create repository"
4. You'll see a page with "Quick setup" instructions
5. COPY the HTTPS link (looks like: https://github.com/YOUR-USERNAME/portfolio.git)
   """)
    input("Press ENTER after you create the repository...")
    github_url = input("Paste your GitHub repository URL: ").strip()
    return github_url

def step_2_upload_files():
    print_section("STEP 2: Upload Files to GitHub")
    print("""
1. Go to your GitHub repository page
2. Click the green "Code" button
3. Click "Upload files"
4. Drag and drop OR click to select these files/folders:
   
   ✓ app/                    (entire folder)
   ✓ run.py
   ✓ requirements.txt
   ✓ Procfile
   ✓ runtime.txt
   ✓ README.md
   ✓ .gitignore
   ✓ DEPLOYMENT.md
   
   ✗ DO NOT upload:
   ✗ .venv/                  (virtual environment)
   ✗ .env                    (your secrets!)
   ✗ __pycache__/
   
5. At bottom, enter commit message: "Initial portfolio commit"
6. Click "Commit changes"
    """)
    input("Press ENTER after uploading files to GitHub...")

def step_3_heroku_account():
    print_section("STEP 3: Create Heroku Account")
    print("""
1. Go to https://www.heroku.com
2. Click "Sign up"
3. Fill in your details:
   - Email: yadavsuyog623@gmail.com
   - Password: (create a strong password)
   - First Name: Suyog
   - Company: (leave blank or your company)
4. Check the email verification link
5. You'll be directed to create your first app

Done? Press ENTER...
    """)
    input("Press ENTER after creating Heroku account...")

def step_4_create_heroku_app():
    print_section("STEP 4: Create Heroku App")
    print("""
1. Go to https://dashboard.heroku.com/apps
2. Click "Create new app"
3. Fill in:
   - App name: suyog-portfolio (or anything unique)
   - Choose region: Europe (if you're in Asia, pick Singapore)
4. Click "Create app"
5. You'll see your app dashboard

COPY your app name from the URL: https://dashboard.heroku.com/apps/YOUR-APP-NAME
    """)
    app_name = input("Enter your Heroku app name: ").strip()
    return app_name

def step_5_connect_github():
    print_section("STEP 5: Connect GitHub to Heroku")
    print("""
1. In your Heroku app dashboard, click "Deploy" tab
2. Under "Deployment method":
   - Click "GitHub"
   - Click "Connect to GitHub"
   - Sign in if asked
3. Under "Connect to GitHub":
   - Search for: portfolio
   - Click "Connect" next to your portfolio repo
4. Under "Automatic deploys":
   - Select "main" branch (or "master")
   - Check "Wait for CI to pass before deploy"
   - Click "Enable Automatic Deploys"
5. Under "Manual deploy":
   - Click "Deploy Branch" (to deploy now)
   - Wait for it to finish (you'll see logs)

This may take 1-2 minutes. Wait for "Your app was successfully deployed" message.
    """)
    input("Press ENTER after connecting GitHub and deploying...")

def step_6_config_vars():
    print_section("STEP 6: Set Email Configuration")
    print("""
1. In Heroku app dashboard, click "Settings" tab
2. Click "Reveal Config Vars"
3. Add these variables (click "Add" after each):

   First variable:
   - KEY: MAIL_USERNAME
   - VALUE: yadavsuyog623@gmail.com
   - Click "Add"

   Second variable:
   - KEY: MAIL_PASSWORD
   - VALUE: mnclbcrhmkgoapwz
   - Click "Add"

   Third variable:
   - KEY: SECRET_KEY
   - VALUE: suyog-portfolio-secret-2024-production
   - Click "Add"

IMPORTANT: After adding these, go back to Deploy tab and click "Deploy Branch" again
to restart the app with new configuration!
    """)
    input("Press ENTER after setting config variables...")

def step_7_view_live():
    print_section("STEP 7: View Your Live Portfolio!")
    print("""
1. In Heroku dashboard, click "Open app" button (top right)
2. Your portfolio should open in browser!
3. Test the contact form to make sure email works
4. Copy the URL - that's your live portfolio!

You can share this URL with anyone: https://your-app-name.herokuapp.com
    """)
    input("Press ENTER after viewing your live app...")

def step_8_future_updates():
    print_section("STEP 8: How to Make Updates")
    print("""
Every time you want to update your portfolio:

1. Edit files in VS Code on your computer
2. Go to GitHub.com → Your portfolio repo
3. Click "Add file" → "Upload files"
4. Select the updated files
5. Enter commit message (e.g., "Updated projects section")
6. Click "Commit changes"
7. Heroku automatically deploys! ✨ (Wait 1-2 minutes)

That's it! No more complex steps needed.

Example updates you can make:
- Edit app/routes.py to update projects and skills
- Edit app/templates/index.html to update content
- Edit app/static/css/style.css to change colors
- Add images to app/static/images/

NEVER upload:
- .env file (your secrets)
- .venv/ folder
    """)
    input("Press ENTER to finish...")

def main():
    print("""
╔════════════════════════════════════════════════════════════╗
║         🚀 PORTFOLIO DEPLOYMENT ASSISTANT 🚀               ║
║                                                            ║
║  This will guide you through deploying your portfolio     ║
║  to the internet in just 8 simple steps!                  ║
║                                                            ║
║  Estimated time: 15-20 minutes                            ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    input("Press ENTER to start deployment...\n")
    
    github_url = step_1_github()
    step_2_upload_files()
    step_3_heroku_account()
    app_name = step_4_create_heroku_app()
    step_5_connect_github()
    step_6_config_vars()
    step_7_view_live()
    step_8_future_updates()
    
    print_section("🎉 CONGRATULATIONS! 🎉")
    print(f"""
Your portfolio is now LIVE!

📍 Repository: {github_url}
🚀 Heroku App: https://dashboard.heroku.com/apps/{app_name}
🌐 Live URL: https://{app_name}.herokuapp.com

Summary of what happens now:
1. Your portfolio is accessible from anywhere
2. Changes you make appear automatically (1-2 min)
3. You can share your portfolio link with anyone
4. Your contact form sends emails to your inbox

Next steps:
- Customize your projects and skills
- Add your real profile photo
- Update social media links
- Share with recruiters and friends!

Need help? Check DEPLOYMENT.md in your project folder.

Happy coding! 🚀
    """)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nDeployment assistant cancelled. Run this script again when ready!")
    except Exception as e:
        print(f"\nError: {e}")
        print("Please try again or check the DEPLOYMENT.md file for manual instructions.")
