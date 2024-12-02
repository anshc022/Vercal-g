
from telusko.wsgi import application
from whitenoise import WhiteNoise

application = WhiteNoise(application)
application.add_files('static/', prefix='static/')