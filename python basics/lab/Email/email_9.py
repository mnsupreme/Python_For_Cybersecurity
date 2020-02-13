import shelve
email_db = shelve.open('../Scripts/emails')
arr =['cranaghan8@aboutads.info', 'Camellia']
print(email_db['Camellia'],arr[0])