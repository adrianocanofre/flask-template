from flask import Flask
from flasgger import Swagger
from flask_restful import Api
from config import config
from .services import *
import logging
import logging.config
import yaml
import os, sys

config_name = os.environ.get('ENVIRONMENT')

app = Flask(__name__)
app.config.from_object(config[config_name])

api = Api(app, prefix="/api")
swagger = Swagger(app)

#last version
api.add_resource(ServiceApi, "/service")
api.add_resource(HealthApi, "/healthcheck")
api.add_resource(WorkApi, "/working")
api.add_resource(InfoApi, "/info")

for version in versions:
    version_name = version.__name__.split('.')[-1]
    for service in version.services:
        api.add_resource(service, '/%s/%s' % (version_name, service.endpoint))
