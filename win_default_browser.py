try :
	from _winreg import HKEY_CURRENT_USER, OpenKey, QueryValue
	throwError=False
except:
	throwError=True
def run_default_browser(output):
	if not throwError:
		path = r"Software\Classes\http\shell\open\command"
		with OpenKey(HKEY_CURRENT_USER, path) as key:
			cmd = QueryValue(key, None)
		#output.write(cmd)
		output.write(cmd)
	else:
		output.write("ERROR: Could not get the current browser")
