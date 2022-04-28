# SECRET_KEY 보호

1. secret.json 생성
2. settings.py에서 SECRET_KEY 가져와 복붙
3. settings.py에서 SECRET_KEY 있던 자리에 아래 부분 입력

```python
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
import os, json
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")
```

4. 기존에 사용했던 ''```'DIRS' = [BASE DIR / 'templates']```, ```DATATBASES = {'NAME' : BASE DIR / 'db.sqlite3'}``` 와 충돌이 발생하게 되는데, 각각 이렇게 바꿔준다.

```python
'DIRS': [os.path.join(BASE_DIR , 'templates')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```



5. .gitignore에 secrets.json 추가 (난 이미 했으니까 생략)