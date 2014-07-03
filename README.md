# java_sys_script

A python script that pulls information concerning java system configuration settings from the user's computer.

# Information Pulled

* Operating system and build version
* Default browser
* Installed browsers
* Version of java installed
* Java deployment properties
* Java whitelisted sited
* Java blacklisted sites

# Supported Archetectures 

* Windows 7 / Windows 8
* Mac OSX

# Running the program

#### Running the script

1. Run the script via python 2
2. The script will create a text file called SCAN_RESULTS.txt
    * Windows: This file will be created in the current directory
    * Mac: The file will be created on desktop

#### Running the compiled executable

1. Compile the program (see "Compiling to an Executable")
2. Double click the executable file
2. The program will create a text file called SCAN_RESULTS.txt
    * Windows: This file will be created in the current directory
    * Mac: The file will be created on desktop

# Compiling to an Executable

##### Requirements

* python version 2.7
* pyinstaller

##### Installing pyinstaller

In order to compile the script to an executable you must use pyinstaller.
Read the documentation for installation instructions. Note, this is not a trivial installation process.

http://www.pyinstaller.org/
http://pythonhosted.org/PyInstaller/#installing-pyinstaller

Please also note that in order to compile for a certain architecture you must configure pyinstaller on that machine.
You can not compile a windows executable on a mac and vice versa.

##### Compiling the program

1. Download and extract the repository
2. Open a terminal and navigate to java_sys_script directory
3. Move into the folder for your respective architecture (windows or mac)
4. Compile the program with pyinstaller with the following command
  * On windows "pyinstaller -F win_java_scan.py"
  * On mac "pyinstaller -F mac_java_scan.py"
5. Retrieve the executable which will be located in the "dist" directory created by pyinstaller

# Know Issues

* Windows
  * No support for Opera or Safari detection
* Mac
  * No support for Opera detection
