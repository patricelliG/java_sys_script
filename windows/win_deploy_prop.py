import os
import re
from lib import extract_from_file

def run_win_deploy_prop (output):
    # Get User Level Java Settings
    usr = os.path.expanduser("~")
    path_deployment_prop = "AppData\LocalLow\Sun\Java\Deployment"
    config_deployment_prop = "deployment.properties"
    filename = usr+"\\"+path_deployment_prop+"\\"+config_deployment_prop
    
    if(os.path.exists(filename)):
        file_deployment_prop = open(filename)
        for line in file_deployment_prop:
            output.write(line), #this is the weirdest syntax to removetrailing newlines
        file_deployment_prop.close()
    else:
        output.write("WARNING: User level deployment.properties file not found. Attempted to read from "+filename+"\n")
 
    # Get Admin Level Java Settings 
	config_deployment_conf = "deployment.config"
	filename = usr+"\\"+path_deployment_prop+"\\"+config_deployment_conf
	if os.path.exists(filename):
		output.write("WARNING: Advanced Administrator settings indicated. For settings location see "+filename+"\n")

