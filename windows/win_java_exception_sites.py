import os
import re


def run_win_java_exception_sites(output):
    '''
Reads Java Exception Sites and writes those sites to the output file given
as a parameter
'''

    usr = os.path.expanduser("~")

    '''Pull Data for Exception Sites'''
    path_exception_sites = "AppData\\LocalLow\\Sun\\Java\\Deployment\\security"
    config_exception_sites = "exception.sites"
    filename = usr + "\\" + path_exception_sites+"\\"+config_exception_sites
    if os.path.exists(filename):
        file_exception_sites = open(filename)
        exception_sites = file_exception_sites.read()
        file_exception_sites.close()
        if exception_sites == '':
            output.write("None")
        else:
            output.write(exception_sites)
    else:
        output.write("No whitelisted sites found.\n")
