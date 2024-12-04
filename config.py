import os
os_name = os.name
if os_name == 'posix':
    PORT="/dev/ttyAMA0"
elif os_name == 'nt':
    PORT="COM5"
    print("Windows OS")
elif os_name == 'os2':
    print("OS/2")
elif os_name == 'ce':
    print("Windows CE")
elif os_name == 'java':
    print("JVM上で動作")
else:
    print("その他のOS")
