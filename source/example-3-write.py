from configparser import ConfigParser

config_1 = ConfigParser()


# Add Section, Then Property

config_1.add_section('section-1')
config_1.set('section-1', 'property-1', 'value 1.1')


# Add Using Section

section_1 = config_1['section-1']
section_1['property-2'] = 'value 1.2'


# Add Using Dict

config_1['section-2'] = {
    'property-3': 'value 2.3',
    'property-4': 'value 2.4'
}


# Write

with open('sample-2.ini', 'w') as file:
    config_1.write(file)


# Print Values

print()

for section_name in config_1.sections():
    section = config_1[section_name]
    for property_name, value in section.items():
        print(section_name, property_name, "=", value)
    print()
