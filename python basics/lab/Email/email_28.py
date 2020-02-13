import shelve
email_db = shelve.open('../Scripts/emails')
arr =['kaxtensg@eepurl.com', 'Kari']
print(email_db['Kari'],arr[0])