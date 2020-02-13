import pyshark

# Task 1

def read(file):
	capture = pyshark.FileCapture(input_file=file)
	for pkt in capture:
		pkt.pretty_print()




#read('cap.pcap')

#Task 2
f = 'tcp.port==80 or tcp.port==443'
bpf = 'tcp port 80 or port 443'
def read2(file,filt=None):
	capture = pyshark.FileCapture(input_file=file,display_filter=filt)
	for pkt in capture:
		pkt.pretty_print()


#read2('cap.pcap',f)

#Task 3

def read3(file, tcp_stream):
	counter = 0
	greatest = 0
	capture = pyshark.FileCapture(input_file=file)
	for pkt in capture:
		try:
			if int(pkt.tcp.stream) > greatest:
				greatest = int(pkt.tcp.stream)
			print(pkt.tcp.stream)
			if pkt.tcp.stream == str(tcp_stream):
				counter += 1
		except:
			pass
	print("the amount of packets in stream 2 ", counter)
	print("biggest stream ", greatest)


#read3('cap.pcap',2)


#Task 4
live = pyshark.LiveCapture(interface="en0",bpf_filter='tcp port 80 or tcp port 443',output_file='shark.pcap')
live.sniff(timeout=10)