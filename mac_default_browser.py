#Mac OS Default Browser

import os.path

def mac_default_browser(output):
    '''
    Pulls the file and prints the default browser for various file types
    '''
    user = os.path.expanduser('~')
    filename = user + '/Library/Preferences/com.apple.LaunchServices.plist'
    if not (os.path.exists(filename)):
        output.write(filename + " does not exist, so we could not get the current browser")
        return
    preferences_file = open(filename, 'r')
    preferences = preferences_file.read()
    preferences_file.close()
    #print preferences.split('\xd2')

    #Thttp
    type_idx = preferences.find('Thttp')
    if type_idx == -1:
        output.write("Thttp: Default browser not found" + "\n")
    else:
        this_preference = preferences[type_idx:]
        start = this_preference.find('com') + 4
        end = this_preference.find ('\xd2')
        output.write("Thttp: " + this_preference[start:end] + "\n")

    #Uhttps
    type_idx = preferences.find('Uhttps')
    if type_idx == -1:
        output.write("Uhttps: Default browser not found" + "\n")
    else:
        this_preference = preferences[type_idx:]
        start = this_preference.find('com') + 4
        end = this_preference.find ('\xd2')
        output.write("Uhttps: " + this_preference[start:end] + "\n")

    #public.html
    type_idx = preferences.find('public.html')
    if type_idx == -1:
        output.write("Public html: Default browser not found" + "\n")
    else:
        this_preference = preferences[type_idx:]
        start = this_preference.find('com') + 4
        end = this_preference.find ('\xd2')
        output.write("Public html: " + this_preference[start:end] + "\n")

    #public.url
    type_idx = preferences.find('public.url')
    if type_idx == -1:
        output.write("Public url: Default browser not found" + "\n")
    else:
        this_preference = preferences[type_idx:]
        start = this_preference.find('com') + 4
        end = this_preference.find ('\xd2')
        output.write("Public url: " + this_preference[start:end] + "\n")

    #public.xhtml
    type_idx = preferences.find('public.xhtml')
    if type_idx == -1:
        output.write("Public xhtml: Default browser not found" + "\n" +"\n")
    else:
        this_preference = preferences[type_idx:]
        start = this_preference.find('com') + 4
        end = this_preference.find ('\xd3')
        output.write("Public xhtml: " + this_preference[start:end] +"\n" +"\n")
    
