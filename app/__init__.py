from flask import Flask
from flasgger import Swagger
from flask_restful import Api
from config import config
from .services import *
import os
from .dependencies_api import DependencyApi


config_name = os.environ.get('ENVIRONMENT')

app = Flask(__name__)
app.config.from_object(config[config_name])

api = Api(app, prefix="/api")
swagger = Swagger(app)

dependency_api = DependencyApi(app.config['DEPENDENCY_API_A_URL'])
another_dependency_api = DependencyApi(app.config['DEPENDENCY_API_B_URL'])

api.add_resource(ServiceApi, "/service")
api.add_resource(HealthApi, "/healthcheck")
api.add_resource(WorkApi, "/working")
api.add_resource(InfoApi, "/info")
