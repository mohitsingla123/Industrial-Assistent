import subprocess

#subprocess.getstatusoutput('time')
#subprocess.getstatusoutput('ssh root@10.12.22.130')
subprocess.getstatusoutput('yum install docker-ce')
subprocess.getstatusoutput('systemctl restart docker')
subprocess.getstatusoutput('systemctl enable docker')
print("Docker is runing succesfully on your system now")
#systemctl enable docker

