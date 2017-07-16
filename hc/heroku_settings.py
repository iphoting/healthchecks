import os
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SITE_ROOT = os.getenv('SITE_ROOT', "https://my-monitoring-project.com")
SITE_NAME = os.getenv('SITE_NAME', "My Monitoring Project")
DEFAULT_FROM_EMAIL = os.getenv('FROM_EMAIL', "noreply@my-monitoring-project.com")
PING_ENDPOINT = os.getenv('PING_ROOT', SITE_ROOT) + "/ping/"
PING_EMAIL_DOMAIN = os.getenv('PING_EMAIL_DOMAIN', "example.com")
REGISTRATION_OPEN = os.getenv('REGISTRATION_OPEN', True)

# Discord integration -- override these via env
DISCORD_CLIENT_ID = os.getenv('DISCORD_CLIENT_ID', None)
DISCORD_CLIENT_SECRET = os.getenv('DISCORD_CLIENT_SECRET', None)

# Slack integration -- override these via env
SLACK_CLIENT_ID = os.getenv('SLACK_CLIENT_ID', None)
SLACK_CLIENT_SECRET = os.getenv('SLACK_CLIENT_SECRET', None)

# Pushover integration -- override these via env
PUSHOVER_API_TOKEN = os.getenv('PUSHOVER_API_TOKEN', None)
PUSHOVER_SUBSCRIPTION_URL = os.getenv('PUSHOVER_SUBSCRIPTION_URL', None)
PUSHOVER_EMERGENCY_RETRY_DELAY = os.getenv('PUSHOVER_EMERGENCY_RETRY_DELAY', 300)
PUSHOVER_EMERGENCY_EXPIRATION = os.getenv('PUSHOVER_EMERGENCY_EXPIRATION', 86400)

# Pushbullet integration -- override these via env
PUSHBULLET_CLIENT_ID = os.getenv('PUSHBULLET_CLIENT_ID', None)
PUSHBULLET_CLIENT_SECRET = os.getenv('PUSHBULLET_CLIENT_SECRET', None)

# Telegram integration -- override these via env
TELEGRAM_BOT_NAME = os.getenv('TELEGRAM_BOT_NAME', None)
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', None)

# SMS (Twilio) integration -- override in local_settings.py
TWILIO_ACCOUNT = os.getenv('TWILIO_ACCOUNT', None)
TWILIO_AUTH = os.getenv('TWILIO_AUTH', None)
TWILIO_FROM = os.getenv('TWILIO_FROM', None)

import herokuify
from herokuify.common import *
from herokuify.mail.mailgun import *

DATABASES = herokuify.get_db_config()

DEBUG = False
SECRET_KEY = os.getenv('SECRET_KEY', "---")

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

import sys
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'stream': sys.stdout,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}
