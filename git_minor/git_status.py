import subprocess

loc=input('Enter the location where your repository is : ')
cd_loc='cd '+ loc
subprocess.getstatusoutput(cd_loc)
subprocess.getstatusoutput('git status')
