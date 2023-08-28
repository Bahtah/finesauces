# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@2do4*d3_0)75b59+k66d3f@1ik8n*181n3f5_+%@hm810fvvi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'finesauces',
        'USER': 'finesaucesadmin',
        'PASSWORD': 'bahadyr',
        'HOST': 'localhost'
    }
}