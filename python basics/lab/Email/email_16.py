import shelve
email_db = shelve.open('../Scripts/emails')
arr =['ccrysell4@webnode.com', 'Cazzie']
print(email_db['Cazzie'],arr[0])