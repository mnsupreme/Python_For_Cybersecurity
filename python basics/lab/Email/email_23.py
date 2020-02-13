import shelve
email_db = shelve.open('../Scripts/emails')
arr =['lbillieb@mail.ru', 'Lira']
print(email_db['Lira'],arr[0])