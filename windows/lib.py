import re
import os
import subprocess

def run_java_version (output):
    version = subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT)
    if version.startswith('java version'):
        output.write(version)
    else:
        output.write('JAVA NOT INSTALLED')
    
def extract_from_file(file_path, regex):
    if os.path.exists(file_path):
        f = open(file_path)
        file_as_string = f.read()
        f.close()
        re.compile(regex)
        sub_expr = regex.findall(file_as_string)
        return sub_expr
    else:
        return 
