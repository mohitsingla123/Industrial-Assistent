import subprocess

loc=input('Enter location where you want to clone the remote repository locally : ')
cd_loc='cd '+ loc
subprocess.getstatusoutput(cd_loc)
url=input('Enter url of the remote repository : ')
c='git clone '+ url + '.'
subprocess.getstatusoutput(c)