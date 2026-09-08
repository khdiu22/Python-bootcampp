import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dyanamic_multi_page_ui.settings')

application = get_wsgi_application()
