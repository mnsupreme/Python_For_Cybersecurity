import shelve
email_db = shelve.open('../Scripts/emails')
arr =['rsheppardd@msu.edu', 'Rollie']
print(email_db['Rollie'],arr[0])