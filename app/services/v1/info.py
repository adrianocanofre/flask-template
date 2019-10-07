import app
from app.services.info import InfoApi
from flask_restful import Resource
from app.common import check_exceptions, last_tag
from datetime import datetime


class InfoApiV1(InfoApi):
    pass
