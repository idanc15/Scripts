import os
import sys

# Execute from the Dir with the APK
# Usage:
# Android_compile_and_sign.py [compile/decompile] [file.apk]
#
# Tool in use: apktool, jar2dex, SignApk (https://github.com/techexpertize/SignApk)
# add all tools to the environment path

# TODO: verify tools
# TODO: error handling
# TODO: verify paths

# Variables
action = sys.argv[1]
apk_file = sys.argv[2]
base_name = os.path.splitext(apk_file)[0]
decompile = "apktool d -f " + apk_file
app_dir = [name for name in os.listdir(".") if os.path.isdir(name) and name == base_name]
recompile = "apktool b -f " + str(app_dir).strip('[]')
path_to_signapk = 'C:\...\Signapk\signapk.jar'
path_to_crt = 'C:\...\Signapk\certificate.pem'
path_to_key = 'C:\...\Signapk]key.pk8'
sign = "java -jar " + path_to_signapk + " " + path_to_crt + " " + path_to_key + " " + os.getcwd() + "\\" + str(app_dir).strip('[]') + "\\dist\\" + apk_file + os.getcwd() + "\\Signed.apk"


if action == 'decompile':
    os.system(decompile)
elif action == 'compile':
    os.system(recompile)
    os.system(sign)
