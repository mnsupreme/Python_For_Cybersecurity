import shelve
email_db = shelve.open('../Scripts/emails')
arr =['sswitsur5@ebay.co', 'Shep']
print(email_db['Shep'],arr[0])