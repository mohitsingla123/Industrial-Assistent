import os
import subprocess
import time

print("__________________________________________________Welcome to Indutrial assistant__________________________________________________\n\n\n")
3

print("press 1 for Docker \n")
print("press 2 for AWS \n")
print("press 3 for Git \n")

a = int(input())
	
if a==1:
    subprocess.getstatusoutput("clear")
    print("select required option")
    print("1: To set-up docker on your system")
    print("2: Available docker images on your system")
    print("3: Currently running Docker container")
    print("4: Start Docker container")
    print("5: Stop Docker container")
    check = int(input())
    if check==1:
        p=subprocess.getstatusoutput("python36 /root/Desktop/docker_module/docker_setup.py")
        print(p)
    elif check==2:
        p=subprocess.getstatusoutput("python36 /root/Desktop/docker_module/docker_available_images.py")
        print(p[1])
    elif check==3:
        p=subprocess.getstatusoutput("python36 /root/Desktop/docker_module/docker_running.py")
        print(p[1])
    elif check==4:
        p=subprocess.getstatusoutput("python36 /root/Desktop/docker_module/StartDockerImage.py")
        print(p[1])
    elif check==3:
        p=subprocess.getstatusoutput("python36 /root/Desktop/docker_module/StopDocker.py")
        print(p[1])
    else:
        subprocess.getstatusoutput("clear")
        print("invalid choise")
        print("loading back to main menu...")
        subprocess.getstatusoutput("python36 /root/Desktop/docker_module/menu.py")
