import subprocess

com=input('Enter the comment you wish to display for the commit : ')
commit='git commit -m '+ com
subprocess.getstatusoutput(commit)
