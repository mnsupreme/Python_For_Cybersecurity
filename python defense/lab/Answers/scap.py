from scapy.all import *


#Task 1
capture = sniff(offline='cap.pcap')
for pkt in capture:
	pkt.show()
capture.hexdump()
capture[5].pdfdump('five.pdf')

#Task 2
trace = traceroute("8.8.8.8")
trace[0].graph(target="traceroute.svg")

#Task 3
packets = [fuzz(IP(dst='8.8.8.8')/TCP()) for i in range(100)]
send(packets)

#Task 4
packets = [IP(dst='192.168.1.1')/TCP() for i in range(10)]
a = sr(packets)
#send and receive returns a tuple of two arrays. One is an array of unanswered packets. 
#The other is an array of tuples consisting of sent packets and their repsonse packets 
a[0].conversations(target='conversations.svg')
#access packet info
a[0][1]