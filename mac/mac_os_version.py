import subprocess

def mac_os_version(output):

    '''Mac OS Version'''

    output.write(subprocess.check_output('sw_vers'))

