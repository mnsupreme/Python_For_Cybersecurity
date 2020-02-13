import shelve
email_db = shelve.open('../Scripts/emails')
arr =['adacks5@freewebs.com', 'Adrian']
print(email_db['Adrian'],arr[0])