from behave import *
from mock import MagicMock
from app.services.info import InfoApi
from app.common import last_tag


@Given('I mock server datetime to {date_time}')
def mock_server_datetime(context, date_time):
    context.server_date_time = InfoApi.get_server_datetime
    InfoApi.get_server_datetime = MagicMock(return_value=date_time)


@Given('I mock service version to {version}')
def mock_commit_datetime(context, version):
    context.get_service_version = InfoApi.get_service_version
    InfoApi.get_service_version = MagicMock(return_value=version)
