from main.settings import *

# websites/manage.py runserver --settings=config.local
print '>>>>>>>>> DEPLOY IN LOCAL'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'english_center',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}