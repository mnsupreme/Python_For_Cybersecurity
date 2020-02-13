import shelve
email_db = shelve.open('../Scripts/emails')
arr =['wsalling0@cbc.ca', 'Woody']
print(email_db['Woody'],arr[0])