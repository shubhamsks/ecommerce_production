import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings") 
import django
django.setup()

import accounts.signals
