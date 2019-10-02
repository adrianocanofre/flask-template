from flask import Flask
from flasgger import Swagger
from flask_restful import Api
from config import config
from .services import *
import logging
import logging.config
import yaml
import os

config_name = os.environ.get('ENVIRONMENT')

app = Flask(__name__)
app.config.from_object(config[config_name])

if app.config['ENV'] != 'production':
    print(app.config)
    logging.config.dictConfig(yaml.load(open('conf/logging_dev.conf')))
else:
    logging.config.dictConfig(yaml.load(open('conf/logging.conf')))

log = logging.getLogger(__name__)

api = Api(app, prefix="/api")
swagger = Swagger(app)

api.add_resource(ServiceApi, "/service")
api.add_resource(HealthApi, "/healthcheck")
api.add_resource(WorkApi, "/working")
api.add_resource(InfoApi, "/info")
