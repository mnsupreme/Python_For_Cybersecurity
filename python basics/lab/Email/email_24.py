import shelve
email_db = shelve.open('../Scripts/emails')
arr =['ddrayec@disqus.com', 'Devi']
print(email_db['Devi'],arr[0])