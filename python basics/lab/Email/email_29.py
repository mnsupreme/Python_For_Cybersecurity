import shelve
email_db = shelve.open('../Scripts/emails')
arr =['mlammertzh@over-blog.com', 'Maryanne']
print(email_db['Maryanne'],arr[0])