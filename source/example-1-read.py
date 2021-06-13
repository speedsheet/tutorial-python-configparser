from configparser import ConfigParser

print()

# Read

config_1 = ConfigParser()
config_1.read('sample.ini')


# Get

property_1 = config_1['section-1']['property-1']
property_2 = config_1.get('section-1', 'property-2')


# Missing

# non_property = config_1['not-a-section']['property-1']  # Throws KeyError
# non_property = config_1['section-1']['not-a-property']  # Throws KeyError

# non_property = config_1.get('not-a-section', 'property-1')  # Throws NoSectionError
# non_property = config_1.get('section-1', 'not-a-property')  # Throws NoOptionError


# Has Property?

if config_1.has_option('section-1', 'not-a-property'):
    print('Present and accounted for, sir! 🙂')
else:
    print('Not present 🙁')
print()


# Default Value

default_value = config_1.get('section-1', 'missing-property',
        fallback = 'the fallback value')


# Data Types

int_property = config_1.getint('types', 'int-property')
float_property = config_1.getfloat('types', 'float-property')
boolean_property = config_1.getboolean('types', 'boolean-property')


# By Section

section_2 = config_1["section-2"]

property_3 = section_2["property-3"]
property_4 = section_2.get("property-4")


# Has Property?

if 'property-3' in section_2:
    print('Present and accounted for, sir! 🙂')
else:
    print('Not present 🙁')
print()


# Section Data Types

types = config_1['types']

int_property_2 = types.getint('int-property')
float_property_2 = types.getfloat('float-property')
boolean_property_2 = types.getboolean('boolean-property')



print()
print('section-1, property-1 :', property_1)
print('section-1, property-2 :', property_2)
print('section-1, missing-property :', default_value)

print()
print('types, int-property :', int_property)
print('types, float-property :', float_property)
print('types, boolean-property:', boolean_property)

print()
print('section-2, property-3 :', property_3)
print('section_2, property-4 :', property_4)

print()
print('types, int-property (2) :', int_property_2)
print('types, float-property (2) :', float_property_2)
print('types, boolean-property (2):', boolean_property_2)


