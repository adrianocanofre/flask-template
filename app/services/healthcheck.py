from flask_restful import Resource
import app


class HealthApi(Resource):

    def get(self):
        return "", 200
