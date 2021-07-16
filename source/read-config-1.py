from configparser import ConfigParser

config = ConfigParser()
config.read('settings.ini')
property = config.get('main-section', 'property')
print(property)
