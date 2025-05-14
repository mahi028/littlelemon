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
4. Add Environment variables
 ```bash
DB_USER=db_username
DB_PASSWORD=password
DB_HOST=host
DB_PORT=port
DB_NAME=db_name
```
`Note:` This config uses postgres database. If you want to run localy with sqlite, replace the following code in `restaurent/restaurent/settings.py`.

replace:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}
```
with:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create superuser (optional for admin)
```bash
python manage.py createsuperuser
```

7. Run the server
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser.

## For admin dashboard

Visit http://127.0.0.1:8000/admin in your browser.

Add Menu items and restaurent Tables there.

## Tech Stack

Python 3

Django 5.2

## 🙏 Acknowledgements
Huge thanks to [freeCodeCamp.org](https://www.youtube.com/@freecodecamp) for the comprehensive Django tutorial that inspired this project.

Django documentation: https://docs.djangoproject.com
