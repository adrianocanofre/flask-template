import app
from app.services.working import WorkApi
import requests
from flask_restful import Resource
from app.common import build_working_response

class WorkApiV2(WorkApi):
    pass
