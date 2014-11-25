import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'ymk)fztl!nec&8yql&ij&o_*n7p$5j3#nbjz*p31wrin3n!rp('

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party apps

    # local apps
    'blongo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blongo_project.urls'

WSGI_APPLICATION = 'blongo_project.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

AUTHENTICATION_BACKENDS = ('mongoengine.django.auth.MongoEngineBackend', )

SESSION_ENGINE = 'mongoengine.django.sessions'

MONGO_DATABASE_NAME = 'blongo'

from mongoengine import connect
connect(MONGO_DATABASE_NAME)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
