import shelve
email_db = shelve.open('../Scripts/emails')
arr =['rcicullo8@go.com', 'Renata']
print(email_db['Renata'],arr[0])