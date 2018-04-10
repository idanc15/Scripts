import os
import sys

# Uninstall package and install the new version
# TODO: check if device is connected
# TODO: error handling

PackageName = sys.argv[1]
APK = sys.argv[2]

uninstallCMD = "adb uninstall " + PackageName
installCMD = "adb -d install " + APK
available = "adb shell pm list packages | grep " + PackageName

try:
    result = os.system(available)

    if result == 0:
        # uninstall the package
        result = os.system(uninstallCMD)

        if result == 0:
            # install the new apk
            result = os.system(installCMD)
    else:
        # install the package
        result = os.system(installCMD)

except Exception as e:
    print e
