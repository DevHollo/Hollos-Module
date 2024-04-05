from hollosmodule import WinOS

os = WinOS()

os.cmd("echo Hello, World!")

os.timeout(3, hide=True)

if os.__class__:
    os.exit()
else:
    os.pause()