import os
import environ
root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env(DEBUG=(bool, False),) # set default values and casting
environ.Env.read_env()

DBUSER = os.environ['YBDBUSER']
DBPASSWORD = os.environ['YBDB_PASSWORD']
DBNAME = os.environ['YBDB_NAME']
DBHOME = os.environ['YBDB_HOST']
DBPORT = os.environ['YBDB_PORT']
EMAIL_BACKEND = os.environ['YBEMAIL_BACKEND']
EMAIL_HOST = os.environ['YBEMAIL_HOST']
EMAIL_HOST_USER = os.environ['YBEMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['YBEMAIL_HOST_PASSWORD']
EMAIL_PORT = os.environ['YBEMAIL_PORT']
EMAIL_USE_TLS = os.environ['YBEMAIL_TLS']
EMAIL_USE_SSL =os.environ['YBEMAIL_SSL']
DEFAULT_FROM_EMAIL = os.environ['YBDEFAULT_EMAIL']
SEND_TO_EMAIL = os.environ['YBSEND_TO_EMAIL']
SOCIAL_AUTH_FACEBOOK_KEY = os.environ['YBFB_KEY']
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ['YBFB_SECRET']
SECRET_KEY = os.environ['YBAPP_SECRET']
ALLOWED_HOST = os.environ['YBAH0']
ALLOWED_HOST1 = os.environ['YBAH1']
ALLOWED_HOST2 = os.environ['YBAH2']
ALLOWED_HOST3 = os.environ['YBAH3']
MERCHANT_ID = os.environ['YBMERCHANT_ID']
PUBLIC_KEY = os.environ['YBMERCHANT_PUBLIC']
PRIVATE_KEY = os.environ['YBMERCHANT_PRIVATE']
STRIPE_API_KEY = os.environ['YBSTRIPE_API_KEY']