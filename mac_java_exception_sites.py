import os
import re


def exception_sites(output)
    '''
    Reads Java Exception Sites and writes those sites to the output file given
    as a parameter
    '''

    usr = os.path.expanduser("~")

    '''Pull Data for Exception Sites'''
    path_exception_sites = "Library/Application Support/Oracle/Java/Deployment/security"
    config_exception_sites = "exception.sites"
    filename = usr + "/" + path_exception_sites+"/"+config_exception_sites
    if os.path.exists(filename):
        file_exception_sites = open(filename)
        exception_sites = file_exception_sites.read()
        file_exception_sites.close()
        if exception_sites == '':
            output.write("NONE")
        else:
            output.write(exception_sites)
    else:
        output.write("Java Exception Sites not found in generic location.")
