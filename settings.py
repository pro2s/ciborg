# -*- coding: utf-8 -*-
from localsettings import *

MENU = [
    {'name': 'Компьютеры', 'url': '/','tag':'index'},
    {'name': 'Обслуживание', 'url': '/service/', 'tag':'service'},
    {'name': 'Договора', 'url': '/contract/', 'tag': 'contracts'}
]

ADMINS = (
     ('Protasov S.S.', 'protasov.s.s@gmail.com'),
)

MANAGERS = ADMINS



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True


# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/images/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xtatia%_u2$v852_cq7@l373&q@!x33v2z65ijp9$9!9=y)r_l'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'djprj.urls'

TEMPLATE_DIRS = (
    "/home/protasov/djprj/tpl"
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
#    'django.contrib.sites',
    'django.contrib.admin',
    'contracts',
    'devices',
    'jobs',
)

#DATE_FORMAT = 'd.m.Y'
#DATETIME_FORMAT = 'd.m.Y H:i'

DATE_FORMAT = ("d.m.Y", "%d.%m.%Y")
DATETIME_FORMAT = ("d.m.Y H:i:s", "%d.%m.%Y %H:%M:%S")

