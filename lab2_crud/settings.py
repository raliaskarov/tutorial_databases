# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '#strong_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django_extensions', # used to visualise database with graphviz
    'crud',
)

SECRET_KEY = 'SECRET KEY for this Django Project'
