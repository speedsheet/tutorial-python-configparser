from useful_stuff import *
from configtools import *


heading("Read Sectionless")

config = read_sectionless("sectionless.ini")

print2("sectionless property-1", config['default']['property-1'])
nl()

