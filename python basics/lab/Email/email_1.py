import shelve
email_db = shelve.open('../Scripts/emails')
arr =['ctuxill0@yellowpages.com', 'Carson']
print(email_db['Carson'],arr[0])