import os
import re
from lib import extract_from_file

def mac_scan_java(output):
    '''
    Looks for the file containing user level Java settings and if found, writes
    the content to the output file taken as a parameter
	'''

    # Check if the file exists
    usr = os.path.expanduser("~")
    path_deployment_prop = "Library/Application Support/Oracle/Java/Deployment"
    config_deployment_prop = "deployment.properties"
    filename = usr+"/"+path_deployment_prop+"/"+config_deployment_prop

    if(os.path.exists(filename)):
        file_deployment_prop = open(filename)
        for line in file_deployment_prop:
            output.write(line), #this is the weirdest syntax to remove newlines
    else:
        output.write("User level deployment.properties file not found.")


