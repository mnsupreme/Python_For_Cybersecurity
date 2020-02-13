import shelve
email_db = shelve.open('../Scripts/emails')
arr =['mbramah3@etsy.com', 'Mia']
print(email_db['Mia'],arr[0])