from shared import *
from configparser import ConfigParser


highlight('Define')

config = ConfigParser()

# Using Config Directly:

config.add_section('section-1')
config.set('section-1', 'property-1', 'value-1')

# Using Section:

section_1 = config['section-1']
section_1['property-2'] = 'valua-2'

# Create Section and Properties Together:

config['section-2'] = {
    'property-1': 'value-1',
    'property-2': 'value-2'
}



highlight ('Write')

with open('sample-created.ini', "w") as file:
    config.write(file)


for name in config.sections():
    section = config[name]
    for key, value in section.items():
        print_indent(1, name + " " + key, value)
    nl()


