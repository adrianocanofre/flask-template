from .service import ServiceApiV2
from .healthcheck import HealthApiV2
from .working import WorkApiV2
from .info import InfoApiV2

services = [ServiceApiV2, HealthApiV2, WorkApiV2, InfoApiV2,]
