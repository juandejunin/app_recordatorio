from pathlib import Path
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Cree rutas dentro del proyecto de esta manera: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# Configuraciones de desarrollo de inicio rápido: no aptas para producción

# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# ADVERTENCIA DE SEGURIDAD: ¡mantenga en secreto la clave secreta utilizada en la producción!


SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
#ADVERTENCIA DE SEGURIDAD: ¡no ejecute con la depuración activada en producción!
#DEBUG = True
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = []


# Application definition
# Definición de la aplicación

ALLOWED_HOSTS = ['*']


# Application definition

DJANGO_APPS =  [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
]
PROJECT_APPS=['user']


THIRD_PARTY_APPS=[
    'corsheaders',
    'rest_framework',
    'djoser',
    # 'social_django',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    # 'ckeditor',
    # 'ckeditor_uploader',
]
INSTALLED_APPS= DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app_recordatorio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'app_recordatorio.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
if not DEBUG:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('NAME'),
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
        'HOST': config('HOST'),
        'PORT': config('PORT'),
    }
}




# Password validation
# Validación de contraseña
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# Internacionalización
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# Archivos estáticos (CSS, JavaScript, Imágenes)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# Tipo de campo de clave principal predeterminado
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL="user.UserAccount"

# La siguiente configuracion hace que usemos el correo por consola durante la etapa de desarrollo.
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

# Ya en la etapa de produccion se utiliza un servicio de correo externo.
if not DEBUG:
    EMAIL_BACKEND = config('EMAIL_BACKEND')
    EMAIL_HOST = config('EMAIL_HOST')
    EMAIL_USE_TLS = config('EMAIL_USE_TLS')
    EMAIL_PORT = config('EMAIL_PORT')
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
    


 