import os

def createDirectory():
	os.makedirs('Lab/Scripts')
	os.makedirs('Lab/Email')
	os.makedirs('Lab/Numbers')

createDirectory()
print(os.getcwd())