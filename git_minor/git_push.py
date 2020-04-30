import subprocess

subprocess.getstatusoutput('git add -A')
com=input('Enter the comment you wish to display for the commit : ')
commit='git commit -m '+ com
subprocess.getstatusoutput(commit)
subprocess.getstatusoutput('git pull origin master')
subprocess.getstatusoutput('git push origin master')