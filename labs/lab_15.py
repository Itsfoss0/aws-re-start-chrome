#!/usr/bin/env python3

"""
Module to demonstrate  using python
for sysadmin tasks
"""

# using the os module

# import os

# os.system('ls')

# using the subprocess module

import subprocess

# subprocess.run(['ls', '-la'])

# subprocess.run(["python3", "--version"])

# subprocess.run(["ls", "-la", "README.md"])

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])