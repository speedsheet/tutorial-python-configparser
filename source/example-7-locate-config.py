from shared import *
from os import environ
from os import getcwd
from os.path import join

from configtools import *
from configlocator import find
from configlocator import Location



# Settings

CONFIG_FILE_NAME = "Test-Config"

ENVIRONMENT_DIRECTORY = join(getcwd(), "test-environment-config")
ENVIRONMENT_VARIABLE = "TEST_CONFIG_PATH"
environ[ENVIRONMENT_VARIABLE] = ENVIRONMENT_DIRECTORY

ENVIRONMENT_LOCATION = Location(CONFIG_FILE_NAME + "-Env.ini", ENVIRONMENT_VARIABLE)
LOCAL_LOCATION = Location(CONFIG_FILE_NAME + "-Local.ini")
OS_LOCATION = Location(CONFIG_FILE_NAME + "-OS.ini")



heading("Find Using Environment")

config = read(find(ENVIRONMENT_LOCATION))

print("Location:  ", find(ENVIRONMENT_LOCATION))
nl()
print("Property-1: ", config.get("section-1", "property-1"))
nl()



heading("Find In OS Location")

config = read(find(OS_LOCATION))

print("Location:  ", find(OS_LOCATION))
nl()
print("Property-1: ", config.get("section-1", "property-1"))
nl()



heading("Find Local File")

config = read(find(LOCAL_LOCATION))

print("Location:  ", find(LOCAL_LOCATION))
nl()
print("Property-1: ", config.get("section-1", "property-1"))
nl()

