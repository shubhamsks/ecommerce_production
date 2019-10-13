import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings") 
import django
django.setup()

import accounts.signals
