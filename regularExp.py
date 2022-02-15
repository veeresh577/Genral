import timeit

clk = timeit.default_timer()

data = {'mac_address': '84:24:8D:80:36:DF', 'tag_reads': [
    {'epc': 'B22FBEDDDECABEDDDECADDBE', 'pc': '3000', 'antennaPort': '2', 'peakRssi': '-38', 'seenCount': '1',
     'timeStamp': '20/3/2019 14:40:35:385', 'phase': '0.00', 'channelIndex': '2', 'isHeartBeat': 'false'},
    {'epc': 'B22FBEDDDECABEDDDECADDBE', 'pc': '3000', 'antennaPort': '2', 'peakRssi': '-38', 'seenCount': '1',
     'timeStamp': '20/3/2019 14:40:35:385', 'phase': '0.00', 'channelIndex': '2', 'isHeartBeat': 'false'},
    {'epc': 'B22FBEDDDECABEDDDECADDBE', 'pc': '3000', 'antennaPort': '2', 'peakRssi': '-38', 'seenCount': '1',
     'timeStamp': '20/3/2019 14:40:35:385', 'phase': '0.00', 'channelIndex': '2', 'isHeartBeat': 'false'},
    {'epc': 'B22FBEDDDECABEDDDECADDBE', 'pc': '3000', 'antennaPort': '2', 'peakRssi': '-38', 'seenCount': '1',
     'timeStamp': '20/3/2019 14:40:35:385', 'phase': '0.00', 'channelIndex': '2', 'isHeartBeat': 'false'},
    {'epc': 'B22FBEDDDECABEDDDECADDBE', 'pc': '3000', 'antennaPort': '2', 'peakRssi': '-38', 'seenCount': '1',
     'timeStamp': '20/3/2019 14:40:35:385', 'phase': '0.00', 'channelIndex': '2', 'isHeartBeat': 'false'},
    {'epc': 'B22FBEDDDECABEDDDECADDBE', 'pc': '3000', 'antennaPort': '2', 'peakRssi': '-38', 'seenCount': '1',
     'timeStamp': '20/3/2019 14:40:35:385', 'phase': '0.00', 'channelIndex': '2', 'isHeartBeat': 'false'},
    {'epc': 'B22FBEDDDECABEDDDECADDBE', 'pc': '3000', 'antennaPort': '2', 'peakRssi': '-38', 'seenCount': '1',
     'timeStamp': '20/3/2019 14:40:35:385', 'phase': '0.00', 'channelIndex': '2', 'isHeartBeat': 'false'},
    {'epc': 'A22F382CC4BA3A498429C884', 'pc': '3400', 'antennaPort': '2', 'peakRssi': '-58', 'seenCount': '1',
     'timeStamp': '20/3/2019 14:40:35:389', 'phase': '0.00', 'channelIndex': '2', 'isHeartBeat': 'false'},
    {'epc': '111122223333444455556666', 'pc': '3000', 'antennaPort': '2', 'peakRssi': '-35', 'seenCount': '1',
     'timeStamp': '20/3/2019 14:40:35:393', 'phase': '0.00', 'channelIndex': '2', 'isHeartBeat': 'false'},
    {'epc': 'BEDDDDDDDDDD000044445555', 'pc': '3400', 'antennaPort': '2', 'peakRssi': '-41', 'seenCount': '1',
     'timeStamp': '20/3/2019 14:40:35:398', 'phase': '0.00', 'channelIndex': '2', 'isHeartBeat': 'false'},
    {'epc': 'E2C06F9200000000', 'pc': '2404', 'antennaPort': '2', 'peakRssi': '-65', 'seenCount': '1',
     'timeStamp': '20/3/2019 14:40:35:427', 'phase': '0.00', 'channelIndex': '2', 'isHeartBeat': 'false'}]}
listdata = data["tag_reads"]
tag = {}
for single_entry in listdata:
    if single_entry['epc'] in tag.keys():
        tag[single_entry['epc']] = str(int(tag[single_entry['epc']]) + int(single_entry['seenCount']))
    else:
        tag[single_entry['epc']] = single_entry["seenCount"]

for key, value in tag.items():
    print("tagID and SeenCount: " + key, " : " + value)

print("__________________________________________________________________________")
print("total observed tag ids: " + str(len(tag)))
stop = timeit.default_timer()
print(stop - clk)
