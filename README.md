# 🍋 Little Lemon (Django Project)

A Django web application for a fictional restaurant **Little Lemon**, allowing customers to book tables online.

This project is built with Django and demonstrates essential web development features including form handling, model relationships, template rendering, and dynamic UI with Django's built-in tools.

> 🎥 *Inspired by the YouTube tutorial from [freeCodeCamp.org](https://www.youtube.com/watch?v=0roB7wZMLqI): [Django Crash Course - Python Web Framewrok]*

---

## 🛠️ Setup Instructions
1. Clone the repo
```bash
git clone https://github.com/mahi028/littlelemon.git
cd littlelemon
```

2. Set up virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser (optional for admin)
```bash
python manage.py createsuperuser
```

6. Run the server
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser.

## For admin dashboard

Visit http://127.0.0.1:8000/admin in your browser.
username: `admin`
password: `admin`

Add Menu items and restaurent Tables there.

## Tech Stack

Python 3

Django 5.2

## 🙏 Acknowledgements
Huge thanks to [freeCodeCamp.org](https://www.youtube.com/@freecodecamp) for the comprehensive Django tutorial that inspired this project.

Django documentation: https://docs.djangoproject.com