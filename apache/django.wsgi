import os, sys
sys.path.append('/home/citizen')
os.environ['DJANGO_SETTINGS_MODULE'] = 'dontpaythestate.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()