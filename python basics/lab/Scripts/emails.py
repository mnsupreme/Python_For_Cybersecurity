import os
import pprint
import shelve
import re
import fileinput

#write email.py folder
email_db = shelve.open('emails')
email_regex = re.compile(r'[^@\s]+@[^\.]+\.[a-z]+')
name_regex = re.compile(r'[A-Za-z]+')
with fileinput.input(files=('../data.txt', '../data2.txt')) as lines:
	for line in lines:
		filename = '../Email/email_' +  str(lines.lineno()) + '.py'
		email = email_regex.search(line)
		name = name_regex.search(line)
		if not email:
			continue
		email_file = open(filename, 'w+')
		email_db[name.group()] = email.group()
		email_file.write("import shelve\n" + "email_db = shelve.open(\'../Scripts/emails\')\n" +"arr =" + pprint.pformat([email.group(),name.group()]) + "\n"+ "print(email_db[\'" + name.group() + "\'],arr[0])" )
		email_file.close()
email_db.close()
fileinput.close()
