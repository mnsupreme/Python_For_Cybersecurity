import shelve
email_db = shelve.open('../Scripts/emails')
arr =['mdivine2@aboutads.info', 'Merrily']
print(email_db['Merrily'],arr[0])