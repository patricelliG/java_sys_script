import os
import re

'''
Reads Java Exception Sites and print those sites
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
        print "NONE"
    else:
        print exception_sites
else:
    print("Java Exception Sites not found in generic location.")
