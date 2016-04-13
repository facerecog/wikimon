#!/usr/bin/env python
#
# Python Installer
#
import subprocess
import sys
import os
import platform
import getpass

if __name__ == "__main__":
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

                    # insert the phone number and pw into config.py

                    print "Please follow the setup instructions at https://github.com/tgalal/yowsup"
                    print "Please enter the phone number you used:",
                    phone = raw_input()
                    password = getpass.getpass(prompt="Please enter the password you received upon registration:")

                    config_file = open("src/config.py", "r")
                    lines = config_file.readlines()
                    config_file.close()


                    login_line = 0
                    pw_line = 0

                    i = 0
                    for line in lines:
                        if line.startswith('    "WHATSAPP_LOGIN":'):
                            login_line = i
                        elif line.startswith('    "WHATSAPP_PW":'):
                            pw_line = i

                        i += 1

                    lines[login_line] = '    "WHATSAPP_LOGIN": "' + phone + '",\n'
                    lines[pw_line] = '    "WHATSAPP_PW": "' + password + '",\n'

                    config_file = open("src/config.py", "w")
                    config_file.write("".join(lines))
                    config_file.close()


            # if index is out of range then flag options
        except IndexError:
            print("** Wikimon by Facerecog Asia **")
            print("** Written by: Muhd Amrullah (Facerecog Asia) **")
            print("** Visit: https://github.com/facerecog **")
            print("\nTo install: sudo setup.py install")





