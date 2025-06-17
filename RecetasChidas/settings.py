from pathlib import Path  # Asegúrate de que esto esté al principio
from decouple import config

"""
Configuración de la base de datos para una aplicación Django.

Este módulo define los parámetros de conexión para la base de datos MySQL que se
utilizará en la aplicación. Se especifica el motor de base de datos, el nombre, el usuario,
la contraseña, el host y el puerto.

Nota:
    Es importante mantener seguros estos datos de conexión para evitar accesos no autorizados.
    Las credenciales se cargan desde variables de entorno a través de un archivo .env
    utilizando la librería python-decouple.
"""

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent  # Descomentado y Path importado

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost').split(',')

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE', default='django.db.backends.mysql'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='3306', cast=int),
    }
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tienda.apps.TiendaConfig',  # Usar solo 'tienda' como nombre de la app
    # ... otras apps de terceros o personalizadas ...
]

MIDDLEWARE = [
    # ... tu middleware
]

ROOT_URLCONF = 'RecetasChidas.urls'  # Corregido al nombre del proyecto 'RecetasChidas'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'tienda' / 'presentation' / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'RecetasChidas.wsgi.application'  # Corregido al nombre del proyecto 'RecetasChidas'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'