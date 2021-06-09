from shared import *

from configparser import ConfigParser


title ('ConfigParser')


highlight('Read File')

config = ConfigParser()
config.read('sample.ini')



highlight('Show Properties')

for name in config.sections():

    section = config[name]

    for key, value in section.items():
        print_indent(1, name + ' ' + key, value)

    nl()

