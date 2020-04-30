import subprocess
import os

a = subprocess.getstatusoutput("docker ps")
print(a)
