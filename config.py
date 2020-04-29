import os

CELERY_RESULT_BACKEND = F"db+postgresql://{os.environ.get('USER_NAME')}:{os.environ.get('USER_PASSWORD')}@{os.environ.get('HOST')}:{os.environ.get('DATABASE_PORT')}/{os.environ.get('DATABASE_NAME')}"
CELERY_BROKER_URL = 'sqs://aws_access_key_id:aws_secret_access_key@'