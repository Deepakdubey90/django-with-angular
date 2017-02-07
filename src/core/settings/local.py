# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mp#6zm!kuakjln$_5kts5fyq5%z16z$mj6bt0n58)wr!^#z^hb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django-angular',
    }
}
