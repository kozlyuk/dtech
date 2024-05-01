"""
Django personal settings for dtech project.
"""

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@g8qo$y-#30&*%m1lq(mfg=rhi6iih--9uiy%#de$8#faa_-u='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_URL = 'http://127.0.0.1:3000'
ADMIN_SITE_URL = 'http://127.0.0.1:8000'

ALLOWED_HOSTS = ['*']

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dtech',
        'USER': 'dtech',
        'PASSWORD': '33kUK%DD',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Email related settings
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'mail.optidea.com.ua'
EMAIL_HOST_PASSWORD = 'L0i0K1u6'
EMAIL_HOST_USER = 'envista@optidea.com.ua'
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = 'enVista messaging <envista@optidea.com.ua>'

# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_PASSWORD = 'LR5KF=TW' #my gmail password
# EMAIL_HOST_USER = 'info@itel.rv.ua' #my gmail username
# EMAIL_PORT = 587
# DEFAULT_FROM_EMAIL = 'Адміністратор проектів Ітел-Сервіс <erp@itel.rv.ua>'

# Logging settings
ADMINS = [
    ('Sergii Kozliuk', 'sergey.kozlyuk@gmail.com'),
]

# Sentry settings
# SENTRY_DSN = "https://2dadf6505b3747a1a7f33f992c35d266@o475557.ingest.sentry.io/5520488"
