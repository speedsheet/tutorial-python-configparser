from configparser import ConfigParser

config_1 = ConfigParser()
config_1.read('sample.ini')

property_1 = config_1['section-1']['property-1']
property_2 = config_1.get('section-1', 'property-2')


# Doesn't Exist?

try:

	# non_property = config['section-1']['not-a-property']              # Raises NameError
	# non_property = config['section-1']['not-a-property']              # Raises NameError

	# non_property = config_1.get('not-a-section', 'not-a-property')    # Raises NoSectionError
	non_property = config_1.get('section-1', 'not-a-property')        # Raises NoOptionError

except Exception as error:

	print (type(error))


if config_1.has_option('section-1', 'property-1'):
	print('section-1 property-1.... Exists 👍')


property_3 = config_1.get('section-1', 'not-a-property', fallback = 'default-value')


# Data Types:

int_property = config_1.getint('types', 'int-property')
float_property = config_1.getfloat('types', 'float-property')
boolean_property = config_1.getboolean('types', 'boolean-property')

try:
	boolean_property = config_1.getboolean('types', 'boolean-property')
except Exception as error:
	print (type(error))


# By Section:

section_2 = config_1['section-2']

property_4 = section_2['property-3']
property_5 = section_2.get('property-4')


# Section Property Exists?

try:

	# non_property = section_2['not-a-property']				        # Raises Key Error
	non_property = section_2.get('not-a-property')                    # Returns None

except Exception as error:

	print (type(error))


if 'property-3' in section_2:
	print('section-2 property-3... Exists 👍')


# Section Data Types:

types_section = config_1['types']

section_int_property = types_section.getint('int-property')
section_float_property = types_section.getfloat('float-property')
section_boolean_property = types_section.getboolean('boolean-property')


# Print All

print("")
print(f"{property_1 = }")
print(f"{property_2 = }")
print(f"{property_3 = }")
print("")
print(f"{int_property = }")
print(f"{float_property = }")
print(f"{boolean_property = }")
print("")
print(f"{property_4 = }")
print(f"{property_5 = }")
print("")
print(f"{section_int_property = }")
print(f"{section_float_property = } ")
print(f"{section_boolean_property = }")
print("")

