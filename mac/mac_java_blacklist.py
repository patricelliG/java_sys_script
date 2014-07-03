import os
import re

'''
Reads Java Blacklist file and writes its contents to the output file taken
as a parameter
'''

def blacklist(output):

    usr = os.path.expanduser("~")

    '''Pull Data for Exception Sites'''
    path_blacklist = "Library/Application Support/Oracle/Java/Deployment/security"
    config_blacklist = "blacklist.dynamic"
    filename = usr + "/" + path_blacklist+"/"+config_blacklist
    if os.path.exists(filename):
        file_blacklist = open(filename)
        blacklist = file_blacklist.read()
        file_blacklist.close()
        if blacklist == '':
            output.write("None")
        else:
            output.write(blacklist)
    else:
        output.write("Java Blacklisted Sites not found in generic location.")

