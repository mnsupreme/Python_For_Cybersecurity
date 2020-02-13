import shelve
email_db = shelve.open('../Scripts/emails')
arr =['kruddom7@flickr.com', 'Kathrine']
print(email_db['Kathrine'],arr[0])