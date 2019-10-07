import app
from time import sleep
from flask import request
from flask_restful import Resource
from app.common import check_exceptions, ValidateInput
from app.common import POST_INPUT_SCHEMA
from flasgger import swag_from


class ServiceApi(Resource):
    endpoint = 'service'
    data = {"table_id": 123, "bill_price": 50.00, "valor" : "valor1"}

    @swag_from('../../docs/post.yml')
    def get(self):
        app.log.info('Realizado um get.')
        return self.data, 200

    @check_exceptions
    @ValidateInput(POST_INPUT_SCHEMA)
    def post(self):
        response = request.json
        app.log.info('Realizado um POST.')
        return {}

    def put(self):
        app.log.info('Realizado um PUT.')
        return {}
