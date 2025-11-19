# My Portfolio Website

A beautiful, responsive portfolio website built with Python Flask, Bootstrap, and custom CSS. Showcase your projects, skills, and get in touch with potential clients and collaborators.

## Features

✨ **Modern Design**
- Clean, professional aesthetic with smooth animations
- Fully responsive design (mobile, tablet, desktop)
- Beautiful gradient backgrounds and transitions

🎯 **Sections**
- **Hero Section**: Eye-catching introduction with call-to-action buttons
- **About Section**: Personal introduction with profile image
- **Projects Section**: Display your best work with project details and technologies
- **Skills Section**: Organized skills by categories
- **Contact Section**: Contact form with email integration
- **Footer**: Social media links and copyright information

⚡ **Interactive Features**
- Smooth scrolling navigation
- Animated elements on scroll
- Contact form with email integration
- Hover effects on cards and buttons
- Mobile-responsive navigation menu

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Bootstrap 5, Custom CSS
- **Icons**: Font Awesome 6
- **Email**: Flask-Mail (optional)

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone or download this project** to your desired location

2. **Navigate to the project directory**
   ```bash
   cd portfolio
   ```

3. **Create and activate a virtual environment**
   ```bash
   # On Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables** (Optional - for email functionality)
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env with your configuration
   # Configure email settings for the contact form
   ```

6. **Run the application**
   ```bash
   python run.py
   ```

7. **Open in your browser**
   - Navigate to `http://localhost:5000`

## Customization

### Update Personal Information

1. **Edit app/routes.py** to update:
   - Your name and title in the hero section
   - Projects (PROJECTS list)
   - Skills (SKILLS dictionary)

2. **Edit app/templates/index.html** to update:
   - Profile image URL
   - Social media links
   - Any text content

3. **Edit app/static/css/style.css** to:
   - Change color scheme
   - Modify fonts
   - Adjust spacing and sizing

### Add Your Profile Image

1. Save your image to `app/static/images/`
2. Update the image URL in `app/templates/index.html`:
   ```html
   <img src="{{ url_for('static', filename='images/your-image.jpg') }}" alt="Profile">
   ```

### Configure Email (Contact Form)

1. Copy `.env.example` to `.env`
2. For Gmail:
   - Enable 2-factor authentication on your Google Account
   - Generate an App Password: https://myaccount.google.com/apppasswords
   - Copy the 16-character password and add to `.env`
3. Update the email configuration in `app/__init__.py`

## Deployment

### Deploy to Heroku

1. **Create a Heroku account** at https://www.heroku.com

2. **Install Heroku CLI** from https://devcenter.heroku.com/articles/heroku-cli

3. **Create Procfile**
   ```bash
   echo "web: gunicorn run:app" > Procfile
   ```

4. **Install gunicorn**
   ```bash
   pip install gunicorn
   ```

5. **Update requirements.txt**
   ```bash
   pip freeze > requirements.txt
   ```

6. **Login to Heroku**
   ```bash
   heroku login
   ```

7. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

8. **Set environment variables**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set MAIL_USERNAME=your-email@gmail.com
   heroku config:set MAIL_PASSWORD=your-app-password
   ```

9. **Deploy**
   ```bash
   git push heroku main
   ```

### Deploy to PythonAnywhere

1. Sign up at https://www.pythonanywhere.com
2. Upload your project files
3. Create a new web app with Python and Flask
4. Configure the WSGI file to point to `run.py`
5. Set environment variables in the dashboard
6. Reload the web app

### Deploy to Vercel/Netlify (Static Version)

For a static version without backend:
1. Use Next.js or Jekyll to generate static files
2. Deploy the `dist` folder to Vercel or Netlify

## File Structure

```
portfolio/
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── routes.py            # Route handlers and data
│   ├── templates/
│   │   └── index.html       # Main HTML template
│   └── static/
│       ├── css/
│       │   └── style.css    # Custom styles
│       ├── js/
│       │   └── script.js    # JavaScript functionality
│       └── images/          # Your images here
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
└── README.md               # This file
```

## Features to Add

- [ ] Blog section
- [ ] Project filters by category
- [ ] Testimonials section
- [ ] Download resume button
- [ ] GitHub integration
- [ ] Dark mode toggle
- [ ] Multi-language support
- [ ] Analytics integration

## Troubleshooting

### Contact form not sending emails?
- Check if you've configured `.env` correctly
- Verify Gmail App Password is correct
- Check Flask-Mail configuration in `app/__init__.py`

### Images not loading?
- Ensure images are in `app/static/images/` folder
- Use correct path: `{{ url_for('static', filename='images/image.jpg') }}`

### Port already in use?
- Change port in `run.py`: `app.run(port=5001)`

### CSS not loading?
- Clear browser cache (Ctrl+Shift+Delete)
- Hard refresh (Ctrl+Shift+R)

## License

This project is open source and available under the MIT License.

## Support

For questions or issues, feel free to reach out through the contact form on the website or create an issue in the repository.

---

**Happy coding! 🚀**
