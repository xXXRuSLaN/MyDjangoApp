SECRET_KEY = 'django-insecure-_8!>_<potemkin!u=xxonlh7k7ioa&w&uk@y+s#u=vnnmmf%(lf8+rgz12323423+wqo5epoap9'
DEBUG = True
ALLOWED_HOSTS = ['176.124.199.217', 'testoza.ru']

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangopulse',
        'USER': 'djangopulse_admin',
        'PASSWORD': 'billy_bounce21#',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
