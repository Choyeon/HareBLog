"""
HareBlog项目的Django设置。

由django-admin startproject使用Django 2.2.6生成。

有关此文件的更多信息，请参见
https://docs.djangoproject.com/en/2.2/topics/settings/

有关设置及其值的完整列表，请参见
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import datetime
import os

THEME = 'bootstrap'
# 像这样在项目内部构建路径：os.path.join（BASE_DIR，...）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 快速启动开发设置-不适合生产
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# 安全警告：请将生产中使用的密钥保密！
SECRET_KEY = '+-b6jxj9&hpseim9n!4ybot(()hd-7*2e7^8r&j(m!2e1&m!zx'

ALLOWED_HOSTS = ['192.168.71.71', '127.0.0.1', '0.0.0.0']

# 应用定义


INSTALLED_APPS = [
    'xadmin',
    "blog",
    "config",
    "comment",
    'HareBlog',
    "user",
    'ckeditor',
    'ckeditor_uploader',
    'corsheaders',
    'crispy_forms',
    'rest_framework',
    "rest_framework.authtoken",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


MIDDLEWARE = [
    'blog.middleware.user_id.UserMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HareBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'themes', THEME, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'HareBlog.wsgi.application'

# 密码验证
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 国际化
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# 静态文件（CSS，JavaScript，图像）
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/tmp/static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'themes', THEME, 'static'),
]

XADMIN_TITLE = "HareBlog后台管理"
XADMIN_FOOTER_TITLE = 'power by choyeon.cn'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 800,
        'tabSpaces': 4,
        'extraPlugins': 'codesnippet',
    },
}

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
CKEDITOR_UPLOAD_PATH = "article_images"

DEFAULT_FILE_STORAGE = 'HareBlog.storage.WatermarkStorage'

# 跨域头
CORS_ORIGIN_ALLOW_ALL = True  # 允许所有的请求，或者设置CORS_ORIGIN_WHITELIST，二选一
CORS_ALLOW_HEADERS = ('*',)  # 允许所有的请求头
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie，前端需要携带cookies访问后端时,需要设置withCredentials: true

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (  # 权限认证类
        # 'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'user.views.jwt_response_payload_handler'
}
