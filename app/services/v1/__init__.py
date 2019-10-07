from .service import ServiceApiV1
from .healthcheck import HealthApiV1
from .working import WorkApiV1
from .info import InfoApiV1

def get_services() : 
    return [
        {'api' : ServiceApiV1, 'endpoint' : 'service'}, 
        {'api' : HealthApiV1, 'endpoint' : 'healthcheck'}, 
        {'api' : WorkApiV1, 'endpoint' : 'working'}, 
        {'api' : InfoApiV1, 'endpoint' : 'info'}
    ]
