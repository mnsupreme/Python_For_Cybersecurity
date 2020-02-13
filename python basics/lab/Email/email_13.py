import shelve
email_db = shelve.open('../Scripts/emails')
arr =['bsoulsby1@opera.com', 'Britt']
print(email_db['Britt'],arr[0])