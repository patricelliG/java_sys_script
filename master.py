# Master file for the java_sys_script
# Handles initial setup for the script
# Also calls each subscan

from windows_os_version import run_windows_os_version
from java_version import run_java_version

border = ('=' * 20 + '\n')

# Create the output file
output = open('java_sys_scan.txt', 'w')

#### Scan for OS details ###
output.write(border + "OPERATING SYSTEM\n" + border)
run_windows_os_version(output)

#### Scan for Browser Info ###
output.write(border + "INTERNET BROWSER\n" + border)
# Get default browser
# Get additional browser information

### Scan Java Version ###
output.write(border + "JAVA VERSION\n" + border)
run_java_version(output)

### Scan deployment.properties file ###
output.write(border + "JAVA SETTINGS\n" + border)

### Scan Witelist ### 
output.write(border + "JAVA WHITELIST\n" + border)

### Blacklist information ### 
output.write(border + "JAVA BLACKLIST\n" + border)

# Close java_sys_scan.txt 
output.close()

