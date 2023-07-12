# Shellingham detects what shell the current Python executable is running in.

import shellingham

# Check the current shell
shell = shellingham.detect_shell()

if shell:
    print("Current shell:", shell)
else:
    print("Unable to detect the shell.")


cpu_count = shellingham.os.cpu_count()
print(cpu_count)

login_cred = shellingham.os.getlogin()
print(login_cred)

cwd = shellingham.os.getcwd()
print(cwd)

env = shellingham.os.environ()
print(env)