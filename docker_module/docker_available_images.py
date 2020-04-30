import subprocess

print("_______________________________________________Available Docker images________________________________________________\n\n")
b=subprocess.getstatusoutput("docker images")
#print()
print(b[1])
