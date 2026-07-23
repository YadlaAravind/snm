
from itsdangerous import URLSafeTimedSerializer

secret_key = 'appcode123'

def endata(data):
    serializer = URLSafeTimedSerializer(secret_key)
    return serializer.dumps(data, salt='extra')

def dedata(data):
    serializer = URLSafeTimedSerializer(secret_key)
    return serializer.loads(data, salt='extra', max_age=180)