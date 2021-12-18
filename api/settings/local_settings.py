from .settings import *

DEBUG = True

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'my_db',
        'USER': 'postgres',
        'PASSWORD': 'jonin123',
        'HOST': 'localhost',
        'PORT': 5433
    }
}