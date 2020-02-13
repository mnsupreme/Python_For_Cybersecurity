import shelve
email_db = shelve.open('../Scripts/emails')
arr =['nwallwoode@imageshack.us', 'Nels']
print(email_db['Nels'],arr[0])