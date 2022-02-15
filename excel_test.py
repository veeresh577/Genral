import openpyxl
import os
from configparser import ConfigParser
import re


config = ConfigParser()
config.read("setting.ini")
ip = config.get("configuration","target_ip")

book = openpyxl.load_workbook(r'D:\OXpecker\security\docker_with_nmap\Nmap-test-plan.xlsx')
sheet = book.active
sheet2 = book["test_sample"]

file = open("report.txt", 'w')

command = ""
print("the given target ip address is {0}".format(ip))

# iterating thoriugh the commands
for row in sheet2.values:
    for value in row:

        if row.index(value) == 2 :
            file.write("command --> "+ value + "\n")
            value = re.sub("<IP_ADDRESS>",ip,value)
            os.system("echo" +" command_is ----"+ str(value) )
            os.system(value)
        else:
            file.write(value + "\n")

    file.write("--------------------------------------------------------------------------------")
    file.write("\n")
           		
           	

