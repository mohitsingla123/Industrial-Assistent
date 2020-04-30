import subprocess
import os
print("Enter the full image name you want start")
image = str(input())

print(image)

os.system("docker run -it "+image)
#a = subprocess.call(['image'])
	

