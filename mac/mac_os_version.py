import subprocess

def mac_os_version(output):

    '''Writes the version of Mac OS running to the output file taken as a parameter'''

    output.write(subprocess.check_output('sw_vers'))

