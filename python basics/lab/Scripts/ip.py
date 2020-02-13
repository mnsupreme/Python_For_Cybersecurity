import os
import re

#print the secret string
data1 = open('../data.txt', 'r')
data1_string = data1.read()
secret_string = re.compile(r'[0-9]{2}[^\w]\.[A-Z]{3}[0-9]{2}')
secret = secret_string.search(data1_string)
print(secret.group())

#write all phone numbers to a file
IP = open('../IP/ip.txt','w+')
only_ip = re.compile(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
ip_array = only_ip.findall(data1_string)
for ip in ip_array:
	IP.write(ip + '\n')

data1.close()
IP.close()

