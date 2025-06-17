# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS = (
    'orm',
)

DEBUG = True

ROOT_URLCONF = 'urls'

ALLOWED_HOSTS = ['*'] 

SECRET_KEY = 'SECRET KEY for this Django Project'
