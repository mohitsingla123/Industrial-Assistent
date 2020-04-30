import subprocess

i=input('If you want to add a perticular file to the staging area the press y and if you want to add all the files in the staging area the press n : ')
if(i=='y'):
    f=input('Enter the file name which you want to add : ')
    add='git add '+ f
    subprocess.getstatusoutput(add)
elif(i=='n'):
    subprocess.getstatusoutput('git add -A')