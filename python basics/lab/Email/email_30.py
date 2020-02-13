import shelve
email_db = shelve.open('../Scripts/emails')
arr =['abernadoni@linkedin.com', 'Avie']
print(email_db['Avie'],arr[0])