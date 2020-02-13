import shelve
email_db = shelve.open('../Scripts/emails')
arr =['lgrimwoodf@upenn.edu', 'Lawton']
print(email_db['Lawton'],arr[0])