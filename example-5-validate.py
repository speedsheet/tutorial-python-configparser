from shared import *
from configtools import *


heading('Validate')


required =(
    ('section-1',('property-1', 'property-2')),
    ('section-2',('property-1', 'property-2', 'property-3')),
    ('section-3',('property-3',)))

try:

    config = read('sample.ini')
    validate(config, required)

except ValueError as error:

    print('Invalid Configuration File:')
    nl()
    print(error.args[0])
    nl()

