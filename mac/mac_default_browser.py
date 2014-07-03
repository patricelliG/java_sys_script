#Mac OS Default Browser

import os.path



def mac_default_browser(output):
    '''
    Looks for the file containing the default browsers for various file types
    and, if found, writes the default browser for various file types to the
    output file taken as a parameter
    '''
    user = os.path.expanduser('~')
    filename = user + '/Library/Preferences/com.apple.LaunchServices.plist'
    if not (os.path.exists(filename)):
        output.write("All browser settings are set to default")
        return
    preferences_file = open(filename, 'r')
    preferences = preferences_file.read()
    preferences_file.close()

    #Thttp
    type_idx = preferences.find('Thttp')
    if type_idx == -1:
        output.write("Thttp: Default browser not found" + "\n")
    else:
        current_string = preferences[type_idx:]
        start = current_string.find('com') + 4
        
        #finding the next browser listed in the file
        end = helper_find_browser(current_string)
        if end == -1:
            output.write("Thttp: Default browser not found" + "\n")
        else:            
            output.write("Thttp: " + current_string[start:end] + "\n")

    #Uhttps
    type_idx = preferences.find('Uhttps')
    if type_idx == -1:
        output.write("Uhttps: Default browser not found" + "\n")
    else:
        current_string = preferences[type_idx:]
        start = current_string.find('com') + 4

        #finding the next browser listed in the file
        end = helper_find_browser(current_string)
        if end == -1:
            output.write("Uhttps: Default browser not found" + "\n")
        else:            
            output.write("Uhttps: " + current_string[start:end] + "\n")

    #public.html
    type_idx = preferences.find('public.html')
    if type_idx == -1:
        output.write("Public html: Default browser not found" + "\n")
    else:
        current_string = preferences[type_idx:]
        start = current_string.find('com') + 4
        
        #finding the next browser listed in the file
        end = helper_find_browser(current_string)
        if end == -1:
            output.write("Public html: Default browser not found" + "\n")
        else:            
            output.write("Public html: " + current_string[start:end] + "\n")

    #public.url
    type_idx = preferences.find('public.url')
    if type_idx == -1:
        output.write("Public url: Default browser not found" + "\n")
    else:
        current_string = preferences[type_idx:]
        start = current_string.find('com') + 4
        #finding the next browser listed in the file
        end = helper_find_browser(current_string)
        if end == -1:
            output.write("Public url: Default browser not found" + "\n")
        else:            
            output.write("Public url: " + current_string[start:end] + "\n")

    #public.xhtml
    type_idx = preferences.find('public.xhtml')
    if type_idx == -1:
        output.write("Public xhtml: Default browser not found" + "\n" +"\n")
    else:
        current_string = preferences[type_idx:]
        start = current_string.find('com') + 4
        
        #finding the next browser listed in the file
        end = helper_find_browser(current_string)
        if end == -1:
            output.write("Public xhtml: Default browser not found" + "\n")
        else:            
            output.write("Public xhtml: " + current_string[start:end] + "\n")
    

def helper_find_browser(current_string):
    '''
    Finding the next browser listed in the file: the file contains complicated
    text that is difficult to pull information from.  This lovely code below
    returns the end index as an integer for a string containing the name
    of the next browser in the file.  The function takes the current string as
    a parameter
    '''
    
    next_safari = current_string.find ('safari')
    next_chrome = current_string.find ('chrome')
    next_firefox = current_string.find ('firefox')
    if next_safari == -1:
        if next_chrome == -1:
            if next_firefox == -1:
                return -1
            else:
                return next_firefox + 7
        else:
            if next_firefox == -1:
                return next_chrome + 6
            else:
                next_browser = min(next_chrome, next_firefox)
    else:
        if next_chrome == -1:
            if next_firefox == -1:
                return next_safari + 6
            else:
                next_browser = min(next_safari, next_firefox)
        else:
            if next_firefox == -1:
                next_browser = min(next_safari, next_chrome)
            else:
                next_browser = min(next_safari, next_chrome, next_firefox)
    if next_browser == next_safari:
        return next_safari + 6
    elif next_browser == next_firefox:
        return next_firefox + 7
    else:
        return next_chrome + 6
