import os
import re

from lib import extract_from_file


def run_win_deploy_prop (output):
    # Get User level Java Settings
    
    # Check if the file exists
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
    
'''Admin Lvl'''
'''config_deployment_conf = "deployment.config"
filename = usr+"\\"+path_deployment_prop+"\\"+config_deployment_conf
print(filename)
regex = re.compile("deployment.system.config=file\\\\:(.+)")
path_unformatted = extract_from_file(filename, regex)
path_formatted = ''.join(path_unformatted).replace('/','\\').replace('C\\','C')
print(path_formatted)
if os.path.exists(path_formatted):
    print("yes")
'''

