import app
from flask_restful import Resource
from app.common import check_exceptions, build_working_response


class WorkApi(Resource):

    @check_exceptions
    def get(self):

        work_list = []

        if app.dependency_api.healthcheck():
            work_list.append(build_working_response('dependency-api', 'working'))
        else:
            work_list.append(build_working_response('dependency-api', 'error',
                                                    'dependency-api offline.', 'CODE01'))

        if app.another_dependency_api.healthcheck():
            work_list.append(build_working_response('another_dependency-api', 'working'))
        else:
            work_list.append(build_working_response('another_dependency-api',
                                                    'error', 'another_dependency-api offline.', 'CODE02'))

        return work_list, 200
