import os
import re
from lib import extract_from_file

def run_win_deploy_prop (output):
    # Get User level Java Settings
    usr = os.path.expanduser("~")
    path_deployment_prop = "AppData\LocalLow\Sun\Java\Deployment"
    config_deployment_prop = "deployment.properties"
    filename = usr+"\\"+path_deployment_prop+"\\"+config_deployment_prop
    
    if(os.path.exists(filename)):
        file_deployment_prop = open(filename)
        for line in file_deployment_prop:
            output.write(line), #this is the weirdest syntax to remove newlines
    else:
        output.write("ERROR: User level deployment.properties file not found.\n")
 
    # Get Admin Level Settings 
	config_deployment_conf = "deployment.config"
	filename = usr+"\\"+path_deployment_prop+"\\"+config_deployment_conf
	if os.path.exists(filename):
		output.write("WARDNING: Advanced Administrator settings indicated. For settings location see "+filename+"\n")

