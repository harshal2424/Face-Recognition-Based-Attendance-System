import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
DEBUG = True
INSTALLED_APPS = [ 'myapp',]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # For SQLite
        'NAME': BASE_DIR / 'db.sqlite3',         # Database file
    }
}
ROOT_URLCONF = 'myproj.urls'
SECRET_KEY = 't15bHcGYNCr_KbcroWb4qzgi_hizeQUaQEVbE7h79VVX856_9UlcTwGugjCA5uVKaLg'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'myapp/templates')],  # Update the path to your templates folder
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
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',  # This is the key app that should be included
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Your app here
    'myapp',  # or whatever your app's name is
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # This one is missing
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # This one is missing
    'django.contrib.messages.middleware.MessageMiddleware',  # This one is missing
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware', 
]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = '/static/'
X_FRAME_OPTIONS = 'SAMEORIGIN' # <-- ADD THIS LINE


