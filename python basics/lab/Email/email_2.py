import shelve
email_db = shelve.open('../Scripts/emails')
arr =['gstaines1@usnews.com', 'Gustave']
print(email_db['Gustave'],arr[0])