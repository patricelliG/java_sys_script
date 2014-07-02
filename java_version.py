import subprocess


def run_java_version (output):
    output.write(subprocess.check_output(["java", "-version"], stderr=subprocess.STDOUT))

