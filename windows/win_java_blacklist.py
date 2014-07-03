import os
import re

'''
Reads Java Blacklist file and writes its contents to the output file taken
as a parameter
'''

def run_win_java_blacklist(output):

    usr = os.path.expanduser("~")

    '''Pull Data for Exception Sites'''
    path_blacklist = "AppData\\LocalLow\\Sun\\Java\\Deployment\\security"
    config_blacklist = "blacklist.dynamic"
    filename = usr + "\\" + path_blacklist+"\\"+config_blacklist
    if os.path.exists(filename):
        file_blacklist = open(filename)
        blacklist = file_blacklist.read()
        file_blacklist.close()
        if blacklist == '':
            output.write("NONE")
        else:
            output.write(blacklist)
    else:
        output.write("No blacklisted sites found\n")
