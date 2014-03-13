import os
import sys  
sys.path.append('/home/kevin/documents/record/tango_with_django_project')
os.environ['DJANGO_SETTINGS_MODULE'] = 'tango_with_django_project.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
