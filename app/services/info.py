import app
from flask_restful import Resource
from app.common import check_exceptions, last_tag
from datetime import datetime


class InfoApi(Resource):

    endpoint = 'info'

    def get(self):
        version = self.get_service_version()
        app.log.info('realizado um get no info')
        return {
                   "version": version,
                   "server_datetime": self.get_server_datetime()
               }, 200

    def get_server_datetime(self):
        return str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def get_service_version(self):
        return last_tag()
