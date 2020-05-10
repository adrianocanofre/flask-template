
from .service import ServiceApi
from .healthcheck import HealthApi
from .working import WorkApi
from .info import InfoApi
import os, importlib, re
from os.path import dirname, basename, isfile, join
import glob
from app.services import v1

#We get the path of the script
services_dir = os.path.dirname(os.path.realpath(__file__))

#We go through all subdirectories, mainly trying to catch directories such as v1, v2 etc.
modules = os.listdir(services_dir)

#Regex matches v<digit>, allowing us to separate out all important directories (v1, v2, v3...)
version_dir_regex = re.compile('v\d+')

#Import said directories
versions = [importlib.import_module('app.services.%s' % mod) for mod in modules if version_dir_regex.match(mod)]
