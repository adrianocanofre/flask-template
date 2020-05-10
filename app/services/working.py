import app
import requests
from flask_restful import Resource
from app.common import build_working_response

class WorkApi(Resource):

    endpoint = 'working'

    def get(self):

        work_list = []
        if requests.get('http://www.google.com'):
            work_list.append(build_working_response('google', 'working'))
        else:
            work_list.append(build_working_response('google',
                                                    'error', 'another_dependency-api offline.', 'CODE02'))

        try:
            if requests.get('http://localhost:8000') == 200:
                work_list.append(build_working_response('localhost', 'working'))
            else:
                work_list.append(build_working_response('localhost',
                                                        'error', 'another_dependency-api offline.', 'CODE02'))
        except requests.ConnectionError as e:
            work_list.append(build_working_response('localhost',
                                                    'error', str(e), 'CODE04'))
        return work_list, 200
