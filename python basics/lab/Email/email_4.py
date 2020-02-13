import shelve
email_db = shelve.open('../Scripts/emails')
arr =['aleahair3@hhs.gov', 'Agustin']
print(email_db['Agustin'],arr[0])