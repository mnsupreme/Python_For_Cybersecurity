import shelve
email_db = shelve.open('../Scripts/emails')
arr =['rshevlan2@nhs.uk', 'Ryon']
print(email_db['Ryon'],arr[0])