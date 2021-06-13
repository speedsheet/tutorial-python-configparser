from configparser import ConfigParser

config_1 = ConfigParser()
config_1.read('sample.ini')

print()

for section_name in config_1.sections():

    section = config_1[section_name]

    for property_name, value in section.items():
        print(section_name, property_name, "=", value)
    print()
