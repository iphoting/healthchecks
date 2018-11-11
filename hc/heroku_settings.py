import os
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REGISTRATION_OPEN = os.getenv('REGISTRATION_OPEN', True)

ANYMAIL = {}
ANYMAIL["MAILGUN_API_KEY"] = os.getenv('MAILGUN_API_KEY', None)
ANYMAIL["MAILGUN_SENDER_DOMAIN"] = os.getenv('MAILGUN_DOMAIN', None)
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"

if os.getenv('FORCE_HTTPS', "off") == "on":
    SECURE_SSL_REDIRECT = True
else:
    SECURE_SSL_REDIRECT = False

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

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
