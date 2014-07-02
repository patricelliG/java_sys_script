import os
import re
usr = os.path.expanduser("~")

def extract_from_file(filename, regex):
    file_as_string = open(filename).read()
    re.compile(regex)
    version = regex.findall(file_as_string)
    return version

def get_version(browser, filename, version_regex):
    if os.path.exists(filename):
        version = extract_from_file(filename, version_regex)
        return browser + " " + ''.join(version)
    else:
        return browser+" not found in generic location."

def scan_ie():
    path_ie = "AppData\\Local\\Microsoft\\Internet Explorer"
    config_ie = "brndlog.txt"
    filename = usr+"\\"+path_ie+"\\"+config_ie
    version_regex = re.compile("Inf Version is set to \"([\d|,]+)\"")
    return get_version("IE", filename, version_regex)

def scan_firefox():
    #Firefox is dumb and creates a subfolder from a random string.
    #Let's grab that string first'''
    path_ff_lay_1 = "AppData\\Roaming\\Mozilla\\Firefox"
    get_folder = "profiles.ini"
    filename = usr+"\\"+path_ff_lay_1+"\\"+get_folder
    if os.path.exists(filename):
        path_regex = re.compile("Path=(.+)")
        lay_2 = extract_from_file(filename, path_regex)
        path_ff_lay_2 = ''.join(lay_2).replace("/","\\")
        #now do same as ie
        config_ff="compatibility.ini"
        filename = usr+"\\"+path_ff_lay_1+"\\"+path_ff_lay_2+"\\"+config_ff
        version_regex = re.compile("LastVersion=(.+)")
        return get_version("Firefox", filename, version_regex)
    else:
        return "ERROR: Could not read filesystem for Firefox settings."

def scan_chrome():
    path_chrome = "AppData\\Local\\Google\\Chrome\\User Data"
    config_chrome = "Local State"
    filename = usr+"\\"+path_chrome+"\\"+config_chrome
    version_regex = re.compile("\"stats_version\": \"([\d|.]+)\"")
    return get_version("Chrome", filename, version_regex)

def run_scan_browsers(file):
    output=""
    output += scan_ie() + "\n"
    output += scan_firefox() + "\n"
    output += scan_chrome() + "\n"
    print(output)

run_scan_browsers(0)
