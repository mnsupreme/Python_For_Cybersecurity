#import the nmap library
import nmap 
import pprint


#We create a new port scanner
nm=nmap.PortScanner()
# we run the port scanner on our target machine with the command line flags -sV (get open ports with the services they are running) and -O flag (enables os fingerprinting)
nm.scan(hosts='10.50.1.78', arguments='-sV -O')
#print the results
pprint.pprint(nm['10.50.1.78'])