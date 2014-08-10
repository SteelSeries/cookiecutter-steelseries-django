# coding: utf-8
import os

import dj_email_url
import dj_database_url
import django_cache_url
from unipath import FSPath as Path
from django.core.exceptions import ImproperlyConfigured


# Helper for env vars
def env(var, default=None):
    try:
        val = os.environ[var]
        if val.lower() == 'true':
            val = True
        elif val.lower() == 'false':
            val = False
        return val
    except KeyError:
        if default is not None:
            return default
        raise ImproperlyConfigured('Set the %s environment variable' % var)

# Paths
PROJECT_DIR = Path(__file__).absolute().ancestor(2)

# Debugging
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Security
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = []

# Middleware
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
)

# Context
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages"
)

# Urls
ROOT_URLCONF = '{{ cookiecutter.repo_name }}.urls'

# WSGI
WSGI_APPLICATION = '{{ cookiecutter.repo_name }}.wsgi.application'

# Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'south',
    'model_utils',
    # 'djcelery',
)

LOCAL_APPS = (
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Database
DATABASES = {
    'default': dj_database_url.config('DATABASE_URL')
}

# Cache
CACHES = {
    'default': django_cache_url.config()
}

# Sessions
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Email
DEFAULT_FROM_EMAIL = env('FROM_EMAIL')

email_config = dj_email_url.config()
EMAIL_FILE_PATH = email_config['EMAIL_FILE_PATH']
EMAIL_HOST_USER = email_config['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = email_config['EMAIL_HOST_PASSWORD']
EMAIL_HOST = email_config['EMAIL_HOST']
EMAIL_PORT = email_config['EMAIL_PORT']
EMAIL_BACKEND = email_config['EMAIL_BACKEND']
EMAIL_USE_TLS = email_config['EMAIL_USE_TLS']

# Dates and times
USE_TZ = True
TIME_ZONE = 'UTC'

# Internationalization
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

# Media files (Uploads)
MEDIA_URL = env('MEDIA_URL', '/media/')
MEDIA_ROOT = env('MEDIA_ROOT', PROJECT_DIR.ancestor(1).child('media'))

# Static files (CSS, JavaScript, Images)
STATIC_URL = env('STATIC_URL', '/static/')
STATIC_ROOT = env('STATIC_ROOT', PROJECT_DIR.ancestor(1).child('static'))

STATICFILES_DIRS = (
    PROJECT_DIR.ancestor(1).child('assets', '_build', 'base'),
    PROJECT_DIR.ancestor(1).child('assets', '_build', 'img'),
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

# Templates
DEFAULT_JINJA2_TEMPLATE_EXTENSION = '.jinja2'

TEMPLATE_LOADERS = (
    'django_jinja.loaders.AppLoader',
    'django_jinja.loaders.FileSystemLoader',
)

TEMPLATE_DIRS = (
    PROJECT_DIR.ancestor(1).child('templates'),
)

# Raven
if 'RAVEN_DSN' in os.environ:
    INSTALLED_APPS += ('raven.contrib.django.raven_compat',)
    RAVEN_CONFIG = {
        'dsn': env('RAVEN_DSN'),
    }

# Queue
# BROKER_URL = env('BROKER_URL')
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_ACCEPT_CONTENT = ['application/json']

# CELERY_IGNORE_RESULT = False
# CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
# CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 * 30

# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# CELERYD_HIJACK_ROOT_LOGGER = False
# CELERYD_LOG_COLOR = False
# CELERY_REDIRECT_STDOUTS = True
# CELERY_REDIRECT_STDOUTS_LEVEL = 'INFO'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'formatters': {
        'verbose': {
            '()': '{{ cookiecutter.repo_name }}.utils.log.MicrosecondFormatter',
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        },
        # 'celery': {
        #     '()': '{{ cookiecutter.repo_name }}.utils.log.MicrosecondFormatter',
        #     'format': '%(asctime)s [%(levelname)s/%(processName)s] %(name)s: %(message)s',
        # },
        # 'task': {
        #     '()': '{{ cookiecutter.repo_name }}.utils.log.TaskFormatter',
        #     'format': '%(asctime)s [%(levelname)s/%(processName)s] %(task_name)s[%(task_id)s]: %(message)s',
        # },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        # 'celery': {
        #     'level': 'INFO',
        #     'class': 'logging.StreamHandler',
        #     'formatter': 'celery',
        # },
        # 'task': {
        #     'level': 'INFO',
        #     'class': 'logging.StreamHandler',
        #     'formatter': 'task',
        # },
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'filters': ['require_debug_false'],
        },
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'sentry'],
        },

        # Celery logging
        # 'djcelery': {
        #     'handlers': ['celery', 'sentry'],
        #     'propagate': False,
        # },
        # 'celery': {
        #     'handlers': ['celery', 'sentry'],
        #     'propagate': False,
        # },
        # 'celery.task': {
        #     'handlers': ['task', 'sentry'],
        #     'propagate': False,
        # },

        # Django default logging
        'django.request': {
            'propagate': True,
        },
        'django.security': {
            'propagate': True,
        },

        # Example of overwriting annoying loggers:
        # 'urllib3.connectionpool': {
        #     'level': 'WARNING',
        # },
        # or:
        # 'urllib3.connectionpool': {
        #     'handlers': ['null'],
        # },
    }
}
