from .service import ServiceApiV3
from .healthcheck import HealthApiV3
from .working import WorkApiV3
from .info import InfoApiV3

def get_services() : 
    return [
        {'api' : ServiceApiV3, 'endpoint' : 'service'}, 
        {'api' : HealthApiV3, 'endpoint' : 'healthcheck'}, 
        {'api' : WorkApiV3, 'endpoint' : 'working'}, 
        {'api' : InfoApiV3, 'endpoint' : 'info'}
    ]
