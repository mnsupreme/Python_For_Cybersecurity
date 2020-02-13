import shelve
email_db = shelve.open('../Scripts/emails')
arr =['aaddams9@weebly.com', 'Augusto']
print(email_db['Augusto'],arr[0])