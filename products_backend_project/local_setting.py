# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w3z=)e3#7s7x+&@#qo^m-3a4f0z_0a6xz#u5@*osf@bkc#^5ww'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'products_database',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}