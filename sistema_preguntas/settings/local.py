from .base import *

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sistemas_prueba',
        'USER': 'prueba_django',
        'PASSWORD':'123456',
        'HOST': 'localhost',
        'PORT':'5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/home/yitmar/sistema_preguntas/static',
]

#STATICFILES_DIRS=[BASE_DIR.child('static')]


EMAIL_USE_TLS= True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER='yitmar.14151819@gmail.com'
EMAIL_HOST_PASSWORD='nion1415'
EMAIL_BACKEND= 'django.core.mail.backends.smtp.EmailBackend'