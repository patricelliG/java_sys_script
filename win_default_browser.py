try :
	from _winreg import HKEY_CURRENT_USER, OpenKey, QueryValue
	throwError=False
except:
	throwError=True
def run_win_default_browser(output):
	if not throwError:
		try:
			path = r"Software\Classes\http\shell\open\command"
			with OpenKey(HKEY_CURRENT_USER, path) as key:
				cmd = QueryValue(key, None)
            output.write("Default Browser: "+cmd+'\n')
		except:
			report_error(output) #Likely cause: default browser was uninstalled but it still marked as the default
	else:
		report_error(output) #Likely cause: not on windows

def report_error(output):
	output.write("ERROR: Could not get the current browser.\n")
