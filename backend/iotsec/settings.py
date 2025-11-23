import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'unsafe-secret-for-dev')

DEBUG = os.getenv('DEBUG','0') == '1'

ALLOWED_HOSTS = ['192.168.1.2', 'localhost', '127.0.0.1']
MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MOSQUITTO_PASS = os.getenv("MOSQUITTO_PASS", "devpass")
MOSQUITTO_USER = os.getenv("MOSQUITTO_USER", "device1")
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'rest_framework',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'iotsec.urls'

TEMPLATES = [{
    'BACKEND':'django.template.backends.django.DjangoTemplates',
    'DIRS':[],
    'APP_DIRS':True,
    'OPTIONS':{'context_processors':[
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
    ],},
}]

WSGI_APPLICATION = 'iotsec.wsgi.application'
ASGI_APPLICATION = "iotsec.asgi.application"
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'HOST': os.getenv('MYSQL_HOST','db'),
        'PORT': int(os.getenv('MYSQL_PORT','3306')),
        'NAME': os.getenv('MYSQL_DATABASE','iotdb'),
        'USER': os.getenv('MYSQL_USER','iotuser'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD','iotpass'),
        'OPTIONS': {'charset':'utf8mb4'},
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
    },
}

