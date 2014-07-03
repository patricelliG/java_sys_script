'''
Master file for the java_sys_script
Handles initial setup for the script
Also calls each subscan
'''

import mac_os_version
import mac_browser
import mac_default_browser
import mac_java_blacklist
import mac_java_exception_sites
import mac_deploy_prop
import lib
import os

border = ('=' * 20 + '\n')

# Create the output file
usr = os.path.expanduser('~')
output = open(usr + '/' 'Desktop' + '/' + 'SCAN_RESULTS.txt', 'w')

#### Scan for OS details ###
output.write('\n' + border + "OPERATING SYSTEM\n" + border)
mac_os_version.mac_os_version(output)

#### Scan for Browser Info ###
output.write('\n' + border + "INTERNET BROWSER\n" + border)
output.write("DEFAULT BROWSERS:\n\n")
# Get default browser
mac_default_browser.mac_default_browser(output)
output.write("BROWSER VERSION:\n\n")
# Get additional browser information
mac_browser.mac_browser_version(output)

### Scan Java Version ###
output.write('\n' + border + "JAVA VERSION\n" + border)
lib.run_java_version(output)

### Scan deployment.properties file ###
output.write('\n' + border + "JAVA SETTINGS\n" + border)
mac_deploy_prop.mac_scan_java(output)

### Scan Whitelist ### 
output.write('\n' + border + "JAVA WHITELIST\n" + border)
mac_java_exception_sites.exception_sites(output)

### Blacklist information ### 
output.write('\n' + border + "JAVA BLACKLIST\n" + border)
mac_java_blacklist.blacklist(output)

# Close java_sys_scan.txt 
output.close()

print 'Your report is on your DESKTOP in file: SCAN_RESULTS.txt'

