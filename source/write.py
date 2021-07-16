from configparser import ConfigParser


def print_config(config):

    print()

    for name in config.sections():
        print(f"[{name}]")
        section = config[name]
        for key, value in section.items():
            print(key, "=", value)
        print()


# Setup:

config_1 = ConfigParser()


# Using Config Directly:

config_1.add_section('section-1')
config_1.set('section-1', 'property-1', 'value-1')


# Using Section:

section_1 = config_1['section-1']
section_1['property-2'] = 'value-2'


# Create Section and Properties Together:

config_1['section-2'] = {
    'property-1': 'value-1',
    'property-2': 'value-2'
}


# Write:

with open('sample-created.ini', "w") as file:
