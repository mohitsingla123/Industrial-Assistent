import os
import subprocess
import time
def integrate():
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
        print("6: Exit")
        check = int(input())
        if check==1:
            p=subprocess.getstatusoutput("python36 /root/Desktop/docker_module/docker_setup.py")
            integrate()
            print(p[1])
        elif check==2:
            p=subprocess.getstatusoutput("python36 /root/Desktop/docker_module/docker_available_images.py")
            print(p[1])
            integrate()
        elif check==3:
            p=subprocess.getstatusoutput("python36 /root/Desktop/docker_module/docker_running.py")
            print(p)
            integrate()
        elif check==4:
            #p=subprocess.getstatusoutput("python36 /root/Desktop/docker_module/StartDockerImage.py")
            print("Enter the full image name you want start")
            image = str(input())
            print(image)
            os.system("docker run -it "+image)
            #print(p[1])
            integrate()
        elif check==5:
            print("Enter the Docker_ID or Docker_Name to stop container")
            image = str(input())
            #print(image)
            os.system("docker stop "+image)
            print(image + " container is Powered Down")
            #p=subprocess.getstatusoutput("python36 /root/Desktop/docker_module/StopDocker.py")
            #print(p[1])
            integrate()
        elif check==6:
            p=subprocess.getstatusoutput("exit")
        else:
            subprocess.getstatusoutput("clear")
            print("invalid choise")
            print("loading back to main menu...")
            integrate()
            #subprocess.getstatusoutput("python36 /root/Desktop/docker_module/menu.py")
    if a==3:
        subprocess.getstatusoutput("clear")
        print("select required option")
        print("1: To initialsed and create repository")
        print("2: to add file in staging area")
        print("3: Clone someone repository")
        print("4: Commit our file into repository")
        print("5: Push our repository into Git")
        print("6: to Check status of repositoty")
        print("7: Exit")
        check = int(input())
        if check==1:
            #ip = input('Enter the IP adderess : ')
            loc=input('Enter the location where you would make the repository : ')
            #os.system('ssh root@'+ip)
            cd_loc='cd '+ loc
            subprocess.getstatusoutput(cd_loc)
            p=subprocess.getstatusoutput('git init')
            integrate()
            #p=subprocess.getstatusoutput("python36 /root/Desktop/git_minor/git.py")
            print(p[1])
        elif check==2:
            i=input('If you want to add a perticular file to the staging area the press y and if you want to add all the files in the staging area the press n : ')
            if(i=='y'):
                f=input('Enter the file name which you want to add : ')
                add='git add '+ f
                subprocess.getstatusoutput(add)
            elif(i=='n'):
                subprocess.getstatusoutput("git add -A")
                print[1]
            integrate()
            #p=subprocess.getstatusoutput("python36 /root/Desktop/git_minor/git_add.py")
            #print(p[1])
        elif check==3:
            loc=input('Enter location where you want to clone the remote repository locally : ')
            cd_loc='cd '+ loc
            subprocess.getstatusoutput(cd_loc)
            url=input('Enter url of the remote repository : ')
            c='git clone '+ url + '.'
            p=subprocess.getstatusoutput(c)
            print(p[1])
            integrate()
            #p=subprocess.getstatusoutput("python36 /root/Desktop/git_minor/git_clone.py")
            #print(p[1])
        elif check==4:
            com=input('Enter the comment you wish to display for the commit : ')
            commit='git commit -m '+ com
            p=subprocess.getstatusoutput(commit)
            print(p[1])
            integrate()
            #p=subprocess.getstatusoutput("python36 /root/Desktop/git_minor/git_commit.py")
            #print(p[1])
        elif check==5:
            subprocess.getstatusoutput('git add -A')
            com=input('Enter the comment you wish to display for the commit : ')
            commit='git commit -m '+ com
            subprocess.getstatusoutput(commit)
            p=subprocess.getstatusoutput('git pull origin master')
            p2=subprocess.getstatusoutput('git push origin master')
            print(p[1])
            print(p[2])
            integrate()
            #p=subprocess.getstatusoutput("python36 /root/Desktop/git_minor/git_push.py")
            #print(p[1])
        elif check==6:
            loc=input('Enter the location where your repository is : ')
            cd_loc='cd '+ loc
            subprocess.getstatusoutput(cd_loc)
            p = subprocess.getstatusoutput('git status')
            print(p[1])
            integrate()
            #p=subprocess.getstatusoutput("python36 /root/Desktop/git_minor/git_status")
        elif check==7:
            p=subprocess.getstatusoutput("exit")
        else:
            subprocess.getstatusoutput("clear")
            print("invalid choise")
            print("loading back to main menu...")
            integrate()
            #subprocess.getstatusoutput("python36 /root/Desktop/docker_module/menu.py")
            
integrate()

