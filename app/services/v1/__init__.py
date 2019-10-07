from .service import ServiceApiV1
from .healthcheck import HealthApiV1
from .working import WorkApiV1
from .info import InfoApiV1

services = [ServiceApiV1, HealthApiV1, WorkApiV1, InfoApiV1,]
