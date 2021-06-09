from shared import *

from configparser import ConfigParser
from os import environ
from os import getcwd


## Read ####################################################

def read(file_name):
    """ Read a file and
        return it's configuration
    """
    config = ConfigParser()
    config.read(file_name)
    return config

def read_string(string_1):
    """ Parse a string and
        retun it's configuration
    """
    config = ConfigParser()
    config.read_string(string_1)
    return config

def read_sectionless(file_name, sectionless_name = 'default'):
    """ Reads a configuration file including
        properties without a section.
    """
    with open(file_name,'r') as file:
        contents = file.read()
        return read_string(f'[{sectionless_name}]\n{contents}')

## Validation ##############################################

def _validate_section(errors, config, section_name, section_properties):
    section = config[section_name]
    for property_name in section_properties:
        if property_name not in section:
            errors.append(f"Section [{section_name}] is missing property '{property_name}'")

def validate(config, required_properties):
    """ Validates that the configuration
        contains all the required sections
        and properties.
    """
    errors = []
    for section_name, section_properties in required_properties:
        if not config.has_section(section_name):
            errors.append(f"Section [{section_name}] is missing. Also requires properties {', '.join(section_properties)}.")
        else:
            _validate_section(errors, config, section_name, section_properties)
    if errors:
        raise ValueError('\n'.join(errors))
