from shared import *

from configparser import ConfigParser
from os import environ
from os import getcwd
from os.path import *
from platform import system

LINUX_CONFIG_LOCATION = 'HOME'
WINDOWS_CONFIG_LOCATION = 'HOMEPATH'

class Location:

    def __init__(self, config_file_name, environment_name = None):
        if not config_file_name:
            raise ValueError("Missing config_file_name.")
        self.config_file_name = config_file_name
        self.environment_name = environment_name

def _default_directory_name(config_location):
    return "." + splitext(basename(config_location.config_file_name))[0].lower()

def _default_location(config_location, root_directory):
    return join(
        root_directory,
        _default_directory_name(config_location),
        config_location.config_file_name)

def _in_current_directory(config_location):
    return exists(current_directory_location(config_location))

def _in_environment_location(config_location):
    if not config_location.environment_name:
        return False
    if config_location.environment_name not in environ:
        return False
    return exists(environment_location(config_location))

def _in_os_location(config_location):
    return exists(os_location(config_location))

def _is_windows_os():
    return system() == 'Windows'

def _linux_location(config_location):
    return _default_location(config_location, environ['HOME'])

def _windows_location(config_location):
    return _default_location(config_location, environ['HOMEPATH'])

def find(config_location):

    if _in_environment_location(config_location):
        return environment_location(config_location)

    if _in_os_location(config_location):
        return os_location(config_location)
        
    if _in_current_directory(config_location):
        return current_directory_location(config_location)

    raise FileNotFoundError(f"Could not find '{config_location.config_file_name}'")

def current_directory_location(config_location):
    return join (getcwd(), config_location.config_file_name)

def environment_location(config_location):
    return join(
        environ[config_location.environment_name],
        config_location.config_file_name)

def os_location(config_location):
    if _is_windows_os():
        return _windows_location(config_location)
    return _linux_location(config_location)

