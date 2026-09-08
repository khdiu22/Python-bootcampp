"""
Django settings for mini_instagram project.
Lab 3: Mini Instagram Clone
"""

from pathlib import Path

# BASE_DIR points to the project root (where manage.py lives)
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------------------------------------------
# SECURITY
# ------------------------------------------------------------------
SECRET_KEY = 'django-insecure-lab3-mini-instagram-clone-change-me'

# Keep True for local development/lab work only
DEBUG = True

ALLOWED_HOSTS = ['*']

# ------------------------------------------------------------------
# APPLICATION DEFINITION
# ------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local app
    'feed',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mini_instagram.urls'

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

WSGI_APPLICATION = 'mini_instagram.wsgi.application'

# ------------------------------------------------------------------
# DATABASE (simple SQLite for the lab)
# ------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ------------------------------------------------------------------
# PASSWORD VALIDATION
# ------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------------------------------------------------
# INTERNATIONALIZATION
# ------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------------------------------------------------
# STATIC FILES  (requirement 8: static/css/feed.css)
# ------------------------------------------------------------------
STATIC_URL = 'static/'

# Where Django looks for static files during development
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Where `collectstatic` copies everything to for production
# Exit ticket requires feed.css to appear inside STATIC_ROOT after collectstatic
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ------------------------------------------------------------------
# MEDIA FILES  (requirement 2: store images under media/posts/)
# ------------------------------------------------------------------
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Max upload size accepted in memory before Django writes a temp file (5 MB)
FILE_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024
