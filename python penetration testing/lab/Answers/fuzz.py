#This script does not yield a successful fuzz attack

#This script is using seclists as its word list https://github.com/danielmiessler/SecLists
#This target attacks the Damn Vulnerable Web App Login Page

#By default this script does notprint any output because it only yields 302 results which are being filtered out
#delete the "hc=[302]" part if you want to see printed results.



import wfuzz
#Start a wfuzz session with url pointed at the Login page. It is very important you set it to the same url that the Login form submits to.
s=wfuzz.FuzzSession(url='http://10.50.1.78/dvwa/login.php')
#Try each entry in the word list. the word FUZZ in our postdata field will be replaced with entries from our wordlist. We send the a POST request to the url with the fuzzed post data. We are filtering out 302 responses.	 													#url encoded form fields. fields need to have the same name as the form fields. Don't forget the Login button value!			
for r in s.fuzz(hc=[302],payloads=[('file',dict(fn='/usr/share/seclists/Fuzzing/big-list-of-naughty-strings.txt'))], postdata='username=FUZZ&password=FUZZ&Login=Login'):
	#delete this ^^^^^  to see all results
	#print all responses from the target machine.
	print(r)