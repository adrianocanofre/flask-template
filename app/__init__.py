from flask import Flask
from flasgger import Swagger
from flask_restful import Api
from config import config
from .services import versions
import logging
import logging.config
import yaml
import os, sys

config_name = os.environ.get('ENVIRONMENT')

app = Flask(__name__)
app.config.from_object(config[config_name])

if app.config['ENV'] != 'production':
    logging.config.dictConfig(yaml.load(open('conf/logging_dev.conf')))
else:
    logging.config.dictConfig(yaml.load(open('conf/logging.conf')))

log = logging.getLogger(__name__)

api = Api(app, prefix="/api")
swagger = Swagger(app)

#versions ends up being a list of versions as such:  (check services/__init__.py)
#[app.services.v1, app.services.v2, ...]
#For each one of these, the __name__() method returns this string, so we get the name by splitting this by '.' and taking the last substring
#Each version needs to define a services list which returns a list of all the APIs to be registered.
#In order for these apis to have their endpoints added, they need to define an `endpoint` variable. For instance, `ServiceApiv3.endpoint` returns 'service'. 
#If these classes inherit the base classes in services/*.py, then this is already handled. 

for version in versions:
    version_name = version.__name__.split('.')[-1]
    for service in version.services:
        api.add_resource(service, '/%s/%s' % (version_name, service.endpoint))

