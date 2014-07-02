
import os
import re
usr = os.path.expanduser("~")

'''Pull Data for Safari Verson'''
path_safari = "/Applications/Safari.app/Contents"
config_safari = "version.plist"
filename = path_safari+"/"+config_safari
if os.path.exists(filename):
    file_safari = open(filename).read()
    regex = re.compile("<key>CFBundleShortVersionString</key>\n[\s+]<string>([\d|.]+)")
    version = regex.findall(file_safari)
    print("Safari "+ ''.join(version))
else:
    print("Safari not found in generic location.")


'''Pull Data for Firefox Version'''
#Firefox is dumb and creates a subfolder from a random string.
#Let's grab that string first'''
path_ff_lay_1 = "Library/Application Support/Firefox"
get_folder = "profiles.ini"
filename = usr+"/"+path_ff_lay_1+"/"+get_folder
if os.path.exists(filename):
    file_lay_2 = open(filename)
    regex = re.compile("Path=(.+)")
    lay_2 = regex.findall(file_lay_2.read())
    path_ff_lay_2 = ''.join(lay_2)
    #now do same as ie
    config_ff="compatibility.ini" 
    filename = usr+"/"+path_ff_lay_1+"/"+path_ff_lay_2+"/"+config_ff
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
path_chrome = "Library/Application Support/Google/Chrome"
config_chrome = "Local State"
filename = usr+"/"+path_chrome+"/"+config_chrome
if os.path.exists(filename):
    file_chrome = open(filename).read()
    regex = re.compile("\"stats_version\": \"([\d|.]+)\"")
    version = regex.findall(file_chrome)
    print("Chrome "+ ''.join(version))
else:
    print("Chrome not found in generic location.")

