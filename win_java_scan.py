# Master file for the java_sys_script
# Handles initial setup for the script
# Also calls each subscan

from win_os_version import run_win_os_version
from lib import run_java_version
from win_browser import run_win_browser
from win_deploy_prop import run_win_deploy_prop
from win_java_exception_sites import run_win_java_exception_sites
from win_java_blacklist import run_win_java_blacklist
from win_default_browser import run_win_default_browser

border = ('=' * 20 + '\n')

# Create the output file
output = open('SCAN_RESULTS.txt', 'w')

#### Scan for OS details ###
output.write('\n' + border + "OPERATING SYSTEM\n" + border)
run_win_os_version(output)

#### Scan for Browser Info ###
output.write('\n' + border + "INTERNET BROWSER\n" + border)
# Get default browser
run_win_default_browser(output)
# Get additional browser information
run_win_browser(output)

### Scan Java Version ###
output.write('\n' + border + "JAVA VERSION\n" + border)
run_java_version(output)

### Scan deployment.properties file ###
output.write('\n' + border + "JAVA SETTINGS\n" + border)
run_win_deploy_prop(output)

### Scan Witelist ### 
output.write('\n' + border + "JAVA WHITELIST\n" + border)
run_win_java_exception_sites(output)

### Blacklist information ### 
output.write('\n' + border + "JAVA BLACKLIST\n" + border)
run_win_java_blacklist(output)

# Close java_sys_scan.txt 
output.close()

