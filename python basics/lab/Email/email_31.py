import shelve
email_db = shelve.open('../Scripts/emails')
arr =['bploverj@gnu.org', 'Benjie']
print(email_db['Benjie'],arr[0])