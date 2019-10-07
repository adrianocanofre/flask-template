import app
from app.services.service import ServiceApi
from time import sleep
from flask import request
from flask_restful import Resource
from app.common import check_exceptions, ValidateInput
from app.common import POST_INPUT_SCHEMA
from flasgger import swag_from

class ServiceApiV1(ServiceApi):
    @swag_from('../../docs/post.yml')
    def get(self):
        self.data['valor'] = ['valor1']
        return super(ServiceApiV1, self).get()

