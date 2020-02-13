import shelve
email_db = shelve.open('../Scripts/emails')
arr =['msiret4@google.ru', 'Marion']
print(email_db['Marion'],arr[0])