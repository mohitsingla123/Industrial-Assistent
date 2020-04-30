import subprocess
import os
print("Enter the Docker_ID or Docker_Name to stop container")
image = str(input())

#print(image)

os.system("docker stop "+image)

print(image + " container is Powered Down")
