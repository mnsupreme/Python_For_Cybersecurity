import shelve
email_db = shelve.open('../Scripts/emails')
arr =['lransoma@plala.or', 'Lion']
print(email_db['Lion'],arr[0])