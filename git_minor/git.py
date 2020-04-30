import subprocess
import os
ip = input('Enter the IP adderess : ')
loc=input('Enter the location where you would make the repository : ')
os.system('ssh root@'+ip)
cd_loc='cd '+ loc
subprocess.getstatusoutput(cd_loc)
subprocess.getstatusoutput('git init')
