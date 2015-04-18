import sae
from delicious import wsgi

application = sae.create_wsgi_app(wsgi.application)