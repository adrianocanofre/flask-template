from flask_restful import Resource
import app


class HealthApi(Resource):
    endpoint = 'healthcheck'

    def get(self):
        return "", 200
