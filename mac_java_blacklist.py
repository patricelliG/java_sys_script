import os
import re

'''
Reads Java Blacklist file and prints its contents
'''


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
        print "NONE"
    else:
        print blacklist
else:
    print("Java Blacklisted Sites not found in generic location.")
