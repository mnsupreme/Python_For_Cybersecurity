import shelve
email_db = shelve.open('../Scripts/emails')
arr =['vdukelow6@mayoclinic.com', 'Vidovic']
print(email_db['Vidovic'],arr[0])