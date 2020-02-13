import shelve
email_db = shelve.open('../Scripts/emails')
arr =['fmaestrini7@earthlink.net', 'Fredrika']
print(email_db['Fredrika'],arr[0])