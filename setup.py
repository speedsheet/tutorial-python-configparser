#!/usr/bin/env python3


from os import makedirs, remove
from os.path import *
from platform import system
from shutil import rmtree
from sys import argv

from configlocator import *
from configtools import *


CONFIG_CONTENTS = '''[section-1]
property-1 = value-1.1'''

CONFIG_FILE_NAME = "Test-Config"

ENVIRONMENT_VARIABLE = "TEST_CONFIG_PATH"
ENVIRONMENT_DIRECTORY = join(getcwd(), "test-environment-config")
environ[ENVIRONMENT_VARIABLE] = ENVIRONMENT_DIRECTORY

ENVIRONMENT_LOCATION = Location(CONFIG_FILE_NAME + "-Env.ini", ENVIRONMENT_VARIABLE)
LOCAL_LOCATION = Location(CONFIG_FILE_NAME + "-Local.ini")
OS_LOCATION = Location(CONFIG_FILE_NAME + "-OS.ini")


def create_all():
    """ Create all test config files.
    """
    print("Creating Test Files...")
    print()

    create_file(os_location(OS_LOCATION), CONFIG_CONTENTS + "-os")
    create_file(environment_location(ENVIRONMENT_LOCATION), CONFIG_CONTENTS + "-environment")
    create_file(current_directory_location(LOCAL_LOCATION), CONFIG_CONTENTS + "-local")

    print("Done.")
    print()

def create_file(path, contents):
    makedirs(dirname(path), exist_ok = True)
    with open(path, 'w') as file:
        file.write(contents)

def has_create_command(arguments):
    return in_list(arguments, ["create", "set", "setup"])

def has_help_command(arguments):
    if not arguments:
        return True
    return in_list(arguments, ["help", "-h", "--help"])

def has_remove_command(arguments):
    return in_list(arguments, ["remove", "rem", "delete", "del"])

def in_list(list_1, match_list):
    for match_item in match_list:
        if match_item in list_1:
            return True
    return False

def remove_all():
    """ Remove all test configuration files.
    """
    print("Removing Test Files...")
    print()

    remove_directory(
        dirname(os_location(OS_LOCATION)))
    remove_directory(
        dirname(environment_location(ENVIRONMENT_LOCATION)))
    remove_file(
        current_directory_location(LOCAL_LOCATION))

    print("Done.")
    print()

def remove_directory(path):
    if isdir(path):
        rmtree(path)

def remove_file(path):
    if exists(path):
        remove(path)

def show_files():
    print("  OS:          ", os_location(OS_LOCATION))
    print("  Environment: ", environment_location(ENVIRONMENT_LOCATION))
    print("  Local:       ", current_directory_location(LOCAL_LOCATION))
    print()

def show_help():
    print("Usage: setup help | create | remove")
    print()
    print("  help       Show Help(this)")
    print()
    print("  create      Creates all test config files.")
    print("  remove      Removes all test config files.")
    print()

if __name__ == '__main__':

    arguments = argv[1:]
    no_command = True

    print()

    if has_create_command(arguments):
        create_all()
        show_files()
        no_command = False

    if has_remove_command(arguments):
        remove_all()
        no_command = False

    if no_command or has_help_command(arguments):
        show_help()


