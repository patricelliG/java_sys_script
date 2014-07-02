import os 
from deploy_prop import deploy_prop

# Get User level Java Settings

# Check if the file exists
usr = os.path.expanduser("~")
path_deployment_prop = "AppData\LocalLow\Sun\Java\Deployment"
config_deployment_prop = "deployment.properties"
filename = usr+"\\"+path_deployment_prop+"\\"+config_deployment_prop

if(os.path.exists(filename)):
    file_deployment_prop = open(filename)
    for line in file_deployment_prop:
        print(line), #this is the weirdest syntax to remove newlines
else:
    print("ERROR: User level deployment.properties file not found.")


