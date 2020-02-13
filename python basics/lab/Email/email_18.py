import shelve
email_db = shelve.open('../Scripts/emails')
arr =['fbiggins6@bravesites.com', 'Fanchette']
print(email_db['Fanchette'],arr[0])