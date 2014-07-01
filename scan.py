import os
baseDir=os.path.expanduser("~")
file=baseDir+"/Documents"
print(file)
if(os.path.exists(file)):
  print("yes")
