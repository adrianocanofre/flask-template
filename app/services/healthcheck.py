from flask_restful import Resource
import app


class HealthApi(Resource):
    endpoint = 'healthcheck'

    def get(self):
        app.log.info('realizado um get no info')
        return "", 200
