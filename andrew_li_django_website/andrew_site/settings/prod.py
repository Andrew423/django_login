from andrew_site.settings.base import *

# override base setting here
DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']
