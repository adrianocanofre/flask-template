import requests
import app
from time import sleep
from flask_restful import Resource
from app.common import check_exceptions, ValidateInput
from app.common import POST_INPUT_SCHEMA
from flasgger import swag_from

data = {"table_id": 123, "bill_price": 50.00}


class ServiceApi(Resource):

    @swag_from('../../docs/post.yml')
    def get(self):
        data['tip'] = self.calculate_tip(100, 0.1)
        app.log.info('Realizado um get.')
        return data, 200

    @check_exceptions
    @ValidateInput(POST_INPUT_SCHEMA)
    def post(self):
        response = requests.post('http://0.0.0.0:3000/api/remote', json={})
        app.log.info('Realizado um POST.')
        return {}, response.status_code

    def calculate_tip(self, bill_price, tip_percent):
        return int(bill_price) * (int(tip_percent) / 100)

    @check_exceptions
    def threaded_function(self):
        for i in range(10):
            print("Async function is running!")
            sleep(1)

    def put(self):
        app.log.info('Realizado um PUT.')
        return {}, 200
