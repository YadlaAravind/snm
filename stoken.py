
from itsdangerous import URLSafeTimedSerializer

secret_key = 'appcode123'
TOKEN_MAX_AGE_SECONDS = 86400

def endata(data):
    serializer = URLSafeTimedSerializer(secret_key)
    return serializer.dumps(data, salt='extra')

def dedata(data):
    serializer = URLSafeTimedSerializer(secret_key)
    return serializer.loads(data, salt='extra', max_age=TOKEN_MAX_AGE_SECONDS)