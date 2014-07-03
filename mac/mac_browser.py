import lib
import os
import re

def mac_browser_version(output):
    '''
    Reads the machine's current browsers' versions and writes them to the output
    file given as a parameter
    '''

    usr = os.path.expanduser("~")

    '''Pull Data for Safari Verson'''
    path_safari = "/Applications/Safari.app/Contents"
    config_safari = "version.plist"
    filename = path_safari+"/"+config_safari
    if os.path.exists(filename):
        regex = re.compile("<key>CFBundleShortVersionString</key>\n[\s+]<string>([\d|.]+)")
        version = lib.extract_from_file(filename, regex)
        output.write("Safari "+ ''.join(version) + "\n")


    '''Pull Data for Firefox Version'''
    #Firefox is dumb and creates a subfolder from a random string.
    #Let's grab that string first'''
    path_ff_lay_1 = "Library/Application Support/Firefox"
    get_folder = "profiles.ini"
    filename = usr+"/"+path_ff_lay_1+"/"+get_folder
    if os.path.exists(filename):
        regex = re.compile("Path=(.+)")
        lay_2 = lib.extract_from_file(filename, regex)
        path_ff_lay_2 = ''.join(lay_2)

    #now do same as ie
    config_ff="compatibility.ini" 
    filename = usr+"/"+path_ff_lay_1+"/"+path_ff_lay_2+"/"+config_ff
    if os.path.exists(filename):
        regex = re.compile("LastVersion=(.+)")
        version = lib.extract_from_file(filename, regex)
        output.write("Firefox " + ''.join(version) + "\n")
    

    '''Pull Data for Chrome Version'''
    path_chrome = "Library/Application Support/Google/Chrome"
    config_chrome = "Local State"
    filename = usr+"/"+path_chrome+"/"+config_chrome
    if os.path.exists(filename):
        regex = re.compile("\"stats_version\": \"([\d|.]+)\"")
        version = lib.extract_from_file(filename, regex)
        output.write("Chrome "+ ''.join(version) + "\n")

