from .service import ServiceApiV2
from .healthcheck import HealthApiV2
from .working import WorkApiV2
from .info import InfoApiV2

def get_services() : 
    return [
        {'api' : ServiceApiV2, 'endpoint' : 'service'}, 
        {'api' : HealthApiV2, 'endpoint' : 'healthcheck'}, 
        {'api' : WorkApiV2, 'endpoint' : 'working'}, 
        {'api' : InfoApiV2, 'endpoint' : 'info'}
    ]
