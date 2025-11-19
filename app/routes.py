import os
from flask import Blueprint, render_template, request, jsonify
from flask_mail import Message
from app import mail

main_bp = Blueprint('main', __name__)

# Sample project data
PROJECTS = [
    {
        'id': 1,
        'title': 'E-Commerce Platform',
        'description': 'A full-stack e-commerce platform with payment integration',
        'technologies': ['Python', 'Flask', 'React', 'PostgreSQL'],
        'link': '#',
        'image': 'project1.jpg'
    },
    {
        'id': 2,
        'title': 'Task Management App',
        'description': 'Collaborative task management application with real-time updates',
        'technologies': ['Python', 'Flask', 'JavaScript', 'MongoDB'],
        'link': '#',
        'image': 'project2.jpg'
    },
    {
        'id': 3,
        'title': 'Data Analytics Dashboard',
        'description': 'Interactive dashboard for data visualization and analysis',
        'technologies': ['Python', 'Pandas', 'Plotly', 'Flask'],
        'link': '#',
        'image': 'project3.jpg'
    },
    {
        'id': 4,
        'title': 'Weather Prediction API',
        'description': 'RESTful API for weather forecasting using machine learning',
        'technologies': ['Python', 'Flask', 'TensorFlow', 'Docker'],
        'link': '#',
        'image': 'project4.jpg'
    }
]

SKILLS = {
    'Backend': ['Python', 'Flask', 'Django', 'FastAPI', 'Node.js'],
    'Frontend': ['HTML/CSS', 'JavaScript', 'React', 'Vue.js', 'Bootstrap'],
    'Database': ['PostgreSQL', 'MongoDB', 'MySQL', 'Redis'],
    'Tools': ['Git', 'Docker', 'AWS', 'Linux', 'VS Code']
}

@main_bp.route('/')
def home():
    return render_template('index.html', projects=PROJECTS, skills=SKILLS)

@main_bp.route('/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        if not all([name, email, message]):
            return jsonify({'success': False, 'error': 'All fields are required'}), 400
        
        # Check if email is configured
        if not os.getenv('MAIL_USERNAME') or not os.getenv('MAIL_PASSWORD'):
            # Email not configured, just log the message
            print(f"Contact message from {name} ({email}): {message}")
            return jsonify({'success': True, 'message': 'Message received! (Email service not configured yet - check terminal for your message)'}), 200
        
        # Send email
        msg = Message(
            subject=f'New Contact from {name}',
            recipients=[os.getenv('MAIL_USERNAME', 'your-email@gmail.com')],
            body=f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
        )
        mail.send(msg)
        
        return jsonify({'success': True, 'message': 'Message sent successfully!'})
    except Exception as e:
        return jsonify({'success': False, 'error': f'Error: {str(e)}'}), 500
