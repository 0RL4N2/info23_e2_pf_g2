from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
    
ALLOWED_HOSTS = ["matiasbadie.pythonanywhere.com"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        #engine = motor de base de datos
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'matiasbadie$default',
        'USER': 'matiasbadie',
        'PASSWORD': 'rootroot',
        'HOST': 'matiasbadie.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}