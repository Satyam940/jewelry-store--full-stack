# import os
# import sys
# from pathlib import Path

# # Add the project root directory to the Python path
# root_dir = Path(__file__).resolve().parent.parent.parent
# sys.path.append(str(root_dir))

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.store.settings')

# application = get_wsgi_application()


import os
import sys
from pathlib import Path

# Add the project root directory and its parent to the Python path
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
grandparent_dir = parent_dir.parent
sys.path.insert(0, str(grandparent_dir))
sys.path.insert(0, str(parent_dir))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.store.settings')

application = get_wsgi_application()