from envparse import env

env.read_envfile('.env')

DEBUG = env.bool('DEBUG', default=False)
CONSUMER_KEY = env.str('CONSUMER_KEY', default='__consumer_key_not_set__')
CONSUMER_SECRET = env.str('CONSUMER_SECRET', default='__consumer_secret_not_set__')
ACCESS_TOKEN = env.str('ACCESS_TOKEN', default='__access_token_not_set__')
ACCESS_TOKEN_SECRET = env.str('ACCESS_TOKEN_SECRET', default='__access_token_secret_not_set__')
