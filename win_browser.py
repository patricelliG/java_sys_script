
'''Pull Data for IE Version'''
import os
import re
usr = os.path.expanduser("~")
path_ie = "AppData\\Local\\Microsoft\\Internet Explorer"
config_ie = "brndlog.txt"
filename = usr+"\\"+path_ie+"\\"+config_ie
if os.path.exists(filename):
    file_ie = open(filename).read()
    regex = re.compile("Inf Version is set to \"([\d|,]+)\"")
    version = regex.findall(file_ie)
    print("IE " + ''.join(version).replace(",", "."))
else:
    print("IE not found in generic location.")



'''Pull Data for Firefox Version'''
#Firefox is dumb and creates a subfolder from a random string.
#Let's grab that string first'''
path_ff_lay_1 = "AppData\\Roaming\\Mozilla\\Firefox"
get_folder = "profiles.ini"
filename = usr+"\\"+path_ff_lay_1+"\\"+get_folder
if os.path.exists(filename):
    file_lay_2 = open(filename)
    regex = re.compile("Path=(.+)")
    lay_2 = regex.findall(file_lay_2.read())
    path_ff_lay_2 = ''.join(lay_2).replace("/","\\")
    #now do same as ie
    config_ff="compatibility.ini"
    filename = usr+"\\"+path_ff_lay_1+"\\"+path_ff_lay_2+"\\"+config_ff
    if os.path.exists(filename):
        file_ff = open(filename).read()
        regex = re.compile("LastVersion=(.+)")
        version = regex.findall(file_ff)
        print("Firefox " + ''.join(version))
    else:
        print("Firefox not found in generic location.")
else:
    print("Firefox not found in generic location.")

'''Pull Data for Chrome Version'''
path_chrome = "AppData\\Local\\Google\\Chrome\\User Data"
config_chrome = "Local State"
filename = usr+"\\"+path_chrome+"\\"+config_chrome
if os.path.exists(filename):
    file_chrome = open(filename).read()
    regex = re.compile("\"stats_version\": \"([\d|.]+)\"")
    version = regex.findall(file_chrome)
    print("Chrome "+ ''.join(version))
else:
    print("Chrome not found in generic location.")

