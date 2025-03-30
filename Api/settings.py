
from pathlib import Path
from datetime import timedelta
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!x#zla+*1#0-5vvh$rxl4245*712@(i4mq!=i4@dah=$7(wr#j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Rest Framework
    'rest_framework',
    'rest_framework_simplejwt',

    # Cors Headers
    'corsheaders',

    # Apps
    'categoria',
    'produto',
    'conta'
    
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Api.urls'

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

WSGI_APPLICATION = 'Api.wsgi.application'

CORS_ALLOWED_ORIGINS: True

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'projetocatalogo',           # Nome do seu banco de dados
        'USER': 'root',                     # Usuário do MySQL
        'PASSWORD': 'root',                 # Senha do MySQL
        'HOST': 'localhost',                # Ou o endereço do seu servidor MySQL
        'PORT': '3306',                     # Porta padrão do MySQL
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {    
    'DEFAULT_AUTHENTICATION_CLASSES': (
       
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )    
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),  # Token de acesso expira em 1 hora
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),  # Token de refresh expira em 7 dias
    'ROTATE_REFRESH_TOKENS': False,  # Não rotacionar os tokens de refresh
    'BLACKLIST_AFTER_ROTATION': False,  # Não adicionar tokens rotacionados à blacklist
    'ALGORITHM': 'HS256',  # Algoritmo de criptografia do JWT
    'SIGNING_KEY': 'sua_chave_secreta',  # Chave secreta para assinar os tokens
    'VERIFYING_KEY': None,  # Usado se for verificar tokens com chave pública
    'AUDIENCE': None,  # Público do token
    'ISSUER': None,  # Emissor do token
}




# Configurações para arquivos de mídia
MEDIA_URL = '/media/'  # URL pública para acessar as imagens
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Diretório onde as imagens serão armazenadas
AUTH_USER_MODEL = 'auth.User'
