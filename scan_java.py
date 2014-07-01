import os 
#baseDir = os.path.expanduser("~")
#file = baseDir+"/Documents"
#print(file)
#if(os.path.exists(file)):

# Get Java Settings
baseDir = os.path.expanduser("~")
dep_prop_file = baseDir+"AppData\LocalLow\Sun\Java\Deployment\deployment.properties"
 
# Build data structure of default deployment.property values
dep_prop = { 'deployment.user.cachedir', ("\"$USER_HOME\" + File.separator + \"cache\"", "User-level cache directory."),
             'deployment.system.cachedir', ("null", "\"System-level cache directory.\"") }




