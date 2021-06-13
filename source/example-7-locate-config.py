from useful_stuff import *
from os import environ
from os import getcwd
from os.path import join

from configtools import *
from configlocator import locate
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

config = read(locate(ENVIRONMENT_LOCATION))

print("Location:  ", locate(ENVIRONMENT_LOCATION))
nl()
print("Property-1: ", config.get("section-1", "property-1"))
nl()



heading("Find In OS Location")

config = read(locate(OS_LOCATION))

print("Location:  ", locate(OS_LOCATION))
nl()
print("Property-1: ", config.get("section-1", "property-1"))
nl()



heading("Find Local File")

config = read(locate(LOCAL_LOCATION))

print("Location:  ", locate(LOCAL_LOCATION))
nl()
print("Property-1: ", config.get("section-1", "property-1"))
nl()

