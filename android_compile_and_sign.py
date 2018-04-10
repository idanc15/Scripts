import os
import sys

# Make sure that the path to the .apk have no spaces
# Usage:
# Android_compile_and_sign.py [compile/decompile] file.apk]
#
# Tools in use: apktool, jar2dex, SignApk
# add all tools to the environment path

# TODO: verify tools
# TODO: error handling
# TODO: verify paths
# TODO: support dir with spaces

# Variables
action = sys.argv[1]
apk_file = sys.argv[2]
base_name = os.path.splitext(apk_file)[0]
decompile = "apktool d -f " + apk_file
app_dir = [name for name in os.listdir(".") if os.path.isdir(name) and name == base_name][0]
recompile = "apktool b -f " + os.getcwd() + "\\" + app_dir
path_to_signapk = 'C:\users\env\desktop\mobile\Signapk\signapk.jar'
path_to_crt = 'C:\users\env\desktop\mobile\Signapk\certificate.pem'
path_to_key = 'C:\users\env\desktop\mobile\Signapk\key.pk8'
sign = "java -jar " + path_to_signapk + " " + path_to_crt + " " + path_to_key + " " + os.getcwd() + "\\" + app_dir + "\\dist\\" + apk_file + " " + os.getcwd() + "\\Signed.apk"


if action == 'decompile':
    os.system(decompile)
elif action == 'compile':
    print "Compiling..." + recompile
    os.system(recompile)
    print "Signing..." + sign
    os.system(sign)
