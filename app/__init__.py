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

logging.config.dictConfig(yaml.load(open('logging.conf')))
log = logging.getLogger(__name__)

api = Api(app, prefix="/api")
swagger = Swagger(app)

# dependency_api = DependencyApi(app.config['DEPENDENCY_API_A_URL'])
# another_dependency_api = DependencyApi(app.config['DEPENDENCY_API_B_URL'])

api.add_resource(ServiceApi, "/service")
api.add_resource(HealthApi, "/healthcheck")
api.add_resource(WorkApi, "/working")
api.add_resource(InfoApi, "/info")
