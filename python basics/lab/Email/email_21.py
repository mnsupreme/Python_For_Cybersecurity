import shelve
email_db = shelve.open('../Scripts/emails')
arr =['lmeritt9@taobao.com', 'Lula']
print(email_db['Lula'],arr[0])