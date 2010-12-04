import os, sys
sys.path.append('/usr/share/python-support/python-django/django/')
sys.path.append('/home/protasov/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'djprj.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
