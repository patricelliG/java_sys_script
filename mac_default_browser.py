#Mac OS Default Browser

import os.path

def mac_browser():
    '''
    Pulls the file and prints the default browser for various file types
    '''
    user = os.path.expanduser('~')
    filename = user + '/Library/Preferences/com.apple.LaunchServices.plist'
    if not (os.path.exists(filename)):
        print filename + " does not exist"
        return
    preferences_file = open(filename, 'r')
    preferences = preferences_file.read()
    preferences_file.close()
    #print preferences.split('\xd2')

    print "Default Browsers:"
    #Thttp
    type_idx = preferences.find('Thttp')
    if type_idx == -1:
        print "Thttp: Default browser not found"
    else:
        this_preference = preferences[type_idx:]
        start = this_preference.find('com') + 4
        end = this_preference.find ('\xd2')

        print "Thttp: " + this_preference[start:end]

    #Uhttps
    type_idx = preferences.find('Uhttps')
    if type_idx == -1:
        print "Uhttps: Default browser not found"
    else:
        this_preference = preferences[type_idx:]
        start = this_preference.find('com') + 4
        end = this_preference.find ('\xd2')

        print "Uhttps: " + this_preference[start:end]

    #public.html
    type_idx = preferences.find('public.html')
    if type_idx == -1:
        print "Public html: Default browser not found"
    else:
        this_preference = preferences[type_idx:]
        start = this_preference.find('com') + 4
        end = this_preference.find ('\xd2')

        print "Public html: " + this_preference[start:end]

    #public.url
    type_idx = preferences.find('public.url')
    if type_idx == -1:
        print "Public url: Default browser not found"
    else:
        this_preference = preferences[type_idx:]
        start = this_preference.find('com') + 4
        end = this_preference.find ('\xd2')
        print "Public url: " + this_preference[start:end]

    #public.xhtml
    type_idx = preferences.find('public.xhtml')
    if type_idx == -1:
        print "Public xhtml: Default browser not found"
    else:
        this_preference = preferences[type_idx:]
        start = this_preference.find('com') + 4
        end = this_preference.find ('\xd3')
        print "Public xhtml: " + this_preference[start:end]
        

    
        
    

mac_browser()
    
    
