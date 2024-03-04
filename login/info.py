
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_HOST_USER ='loginpage.django@gmail.com'
EMAIL_HOST_PASSWORD = '@login1010'
EMAIL_PORT = 587


DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
