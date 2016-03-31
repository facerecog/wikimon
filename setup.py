#!/usr/bin/env python
#
# Python Installer
#
import subprocess
import sys
import os
import platform
import getpass

if platform.system() == "Linux":
    # Check user ID
    if os.getuid() != 0:
        print("Are you root? Please execute as root")
        exit()

    try:
        # if our command option is true then install dependencies
        if sys.argv[1] == "install":
            installer = True
            if os.path.isfile("/etc/apt/sources.list"):
                subprocess.Popen("bash setup.sh", shell=True).wait()

                print "Please follow the setup instructions at https://github.com/tgalal/yowsup"
                print "Please enter the phone number you used:",
                phone = raw_input()
                password = getpass.getpass(prompt="Please enter the password you received upon registration:")

                config_file = open("src/config.py", "r")
                lines = config_file.readlines()
                config_file.close()


                auth_line = 0

                for line in lines:
                    if line.startswith("auth = "):
                        break
                    auth_line += 1

                lines[auth_line] = "auth = ('" + phone + "', '" + password + "')\n"

                config_file = open("src/config.py", "w")
                config_file.write("".join(lines))
                config_file.close()


        # if index is out of range then flag options
    except IndexError:
        print("** Wikimon by Facerecog Asia **")
        print("** Written by: Muhd Amrullah (Facerecog Asia) **")
        print("** Visit: https://github.com/facerecog **")
        print("\nTo install: sudo setup.py install")





