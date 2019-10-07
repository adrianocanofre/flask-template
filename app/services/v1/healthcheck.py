from flask_restful import Resource
import app
from app.services.healthcheck import HealthApi

class HealthApiV1(HealthApi):
    pass
