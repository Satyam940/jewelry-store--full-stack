import os
import sys
from pathlib import Path

# Add the project root directory to the Python path
root_dir = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(root_dir))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.store.settings')

application = get_wsgi_application()