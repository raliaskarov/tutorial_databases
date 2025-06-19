# settings.py
"""
default django database setup
"""

# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'stong_password',
        'HOST': 'localhost',
        'PORTS': '5432',
    }
}

INSTALLED_APPS = (
    'standalone',
)

SECRET_KEY = 'SECRET KEY for this Django Project'