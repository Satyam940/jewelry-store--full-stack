import os
from django.core.wsgi import get_wsgi_application
import sys


project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.store.settings')

application = get_wsgi_application()
