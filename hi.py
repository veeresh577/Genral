import os
import time

path = r"C:\TouchGFXProjects\sianaLatest\Tools"

os.chdir(path)
print(os.getcwd())


for i in range(20,1,40):
    os.system("invoke create-application -a demoapp"+str(i)+" -d demoapp"+str(i) )
    time.sleep(4)
    print("counter value : {0}".format(i))


print(os.listdir())
