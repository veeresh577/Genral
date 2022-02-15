
import json
import time
import socket
import logging


buffer = 1024*100
host = "10.17.131.147"  #input("Enter the server ip:")
port = 4444           #int((input("enter the port")))
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error %s" % (err))
    exit()

tag = {}
while 1:
    try:

        data = s.recv(buffer)

        time.sleep(1)

        data1 = data.decode('utf-8')
        print(data1)
        '''data2 = '{'+data1
        data3 = json.loads(data2)
        #print(data3)
        data1 = json.loads(('{'+data.decode('utf-8')))
        listdata = data1["tag_reads"]

        for single_entry in listdata:
            if single_entry['epc'] in tag.keys():
                tag[single_entry['epc']] = str(int(tag[single_entry['epc']]) + int(single_entry['seenCount']))
            else:
                tag[single_entry['epc']] = single_entry["seenCount"]

        for key, value in tag.items():
            print("tagID and SeenCount: " + key, " : " + value)
        print("total observed tag ids: " + str(len(tag)))
        print("__________________________________________________________________________")'''


    except KeyboardInterrupt:
        print("keyboard interrupt has occured: ctrl + C is excd")
        exit()
        break
    except socket.error as msg:
        print(str(msg))
        exit()
        break
    except Exception:
        continue

