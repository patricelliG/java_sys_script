import os 
import deploy_prop.py

#baseDir = os.path.expanduser("~")
#file = baseDir+"/Documents"
#print(file)
#if(os.path.exists(file)):

# Get User level Java Settings

# Check if the file exists
baseDir = os.path.expanduser("~")
deployment_prop_file = baseDir+"AppData\LocalLow\Sun\Java\Deployment\deployment.properties"
if(os.path.exists(deployment_prop_file)):
    # File exists, read in the settings
else
    # File not found, print error
    print("ERROR: User level deployment.properties file not found."
 





