#We are using seclists as our wordlist library https://github.com/danielmiessler/SecLists
#We are targeting the Damn Vulnerable Web Application

#we import the wfuzz library
import wfuzz
#We will traverse the dvwa application. Note the word FUZZ will be replaced by entries in our wordlist
s=wfuzz.FuzzSession(url='http://10.50.1.78/dvwa/FUZZ')
#We replace the word FUZZ for each entry in our wordlist and make a GET request to the address. We filter out all 404 reponses
for r in s.fuzz(hc=[404],payloads=[('file',dict(fn='/usr/share/seclists/Discovery/Web-Content/common.txt'))]):
	#we print reponses from the target machine.
	print(r)