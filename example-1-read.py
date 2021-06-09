from shared import *

from configparser import ConfigParser


title ('ConfigParser')


highlight('Read File')

config = ConfigParser()
config.read('sample.ini')



highlight('Get Property')

property_1 = config.get('section-1', 'property-1')
# non_property = config.get('not-a-section', 'not-a-property')      # Throws NoSectionError
# non_property = config.get('section-1', 'not-a-property')          # Throws NoOptionError

property_2 = config['section-1']['property-2']
# non_property = config['not-a-section']['not-a-property']          # Throws KeyError
# non_property = config['section-1']['not-a-property']              # Throws KeyError

property_3 = config.get('section-1', 'not-a-property', fallback = 'value 1.3')



highlight('Exists?')

if config.has_option('section-1', 'property-1'):

    print_indent(1, 'section-1 property-1', 'Exists 👍')
    nl()



heading('Conversion')

int_property = config.getint('types', 'int-property')
float_property = config.getfloat('types', 'float-property')
boolean_property = config.getboolean('types', 'boolean-property')

# True Values: 'true', 'yes', 'on', 1
# False Values: 'false', 'no', 'off', 0

# non_int_property = config.getint('section-1', 'property-1')       # Throws ValueError



heading ('Sections')

section = config['section-1']

section_property_1 = section.get('property-1')
section_property_2 = section['property-2']

types_section = config['types']

types_int_property = types_section.getint('int-property')

if 'property-2' in section:

    print_indent(1, 'section property-2', 'Exists 👍')
    nl()




heading ('Results')


print2('section-1 property-1', property_1)
print2('section-1 property-2', property_2)
print2('section-1 property-3', property_3)
nl()

print2('type int-property', int_property)
print2('type float-property', float_property)
print2('type boolean-property', boolean_property)
nl()

print2('section property-1', section_property_1)
print2('section property-2', section_property_2)
nl()

print2('types int-property', types_int_property)
nl()



