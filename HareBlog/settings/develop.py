from .base import *  # NOQA

# 安全警告：请勿在生产环境中启用调试的情况下运行！
DEBUG = True

# 数据库
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'AUTOCOMMIT': True,
    }
}
