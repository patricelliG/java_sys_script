import re
import os

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
