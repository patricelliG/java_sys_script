# A Simple script that pulls information about the host os
# The information is printed to the file object passed to the function

import platform

def run_windows_os_version (output):
    output.write('ProductName:    ' + platform.system() + ' ' + platform.release() + '\n')
    output.write('ProductVersion: ' + platform.version() + '\n')
