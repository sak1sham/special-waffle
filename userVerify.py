import pickle
import os
import accounts

def add_to_pickle(path, item):
    with open(path, 'ab') as file:
        pickle.dump(item, file, pickle.HIGHEST_PROTOCOL)

def read_from_pickle(path):
    with open(path, 'rb') as file:
        try:
            while True:
                yield pickle.load(file)
        except EOFError:
            pass

def userAccountNameFound(account):
	for item in read_from_pickle('./_data/accountDetails.dat'):
		#acc = repr(item)
		acc = item
		if(acc.AccountName == account.AccountName):
			return 1
	return 0    	

def checkLoginCredentials(account):
	for item in read_from_pickle('./_data/accountDetails.dat'):
		#acc = repr(item)
		#print(repr(item))
		acc = item
		if(acc.AccountName == account.AccountName and acc.password == account.password):
			print(str(acc.AccountName) + " logged in successfully")
			return 1
	return 0    	

def addAccountDetails(account):
	add_to_pickle('./_data/accountDetails.dat', account)
	print("Account details added")  
	username = str(account.AccountName)
	if not os.path.exists('./_data/' + username):
		os.makedirs('./_data/' + username)
	open('./_data/' + username + '/accounts.dat', "a")
	open('./_data/' + username + '/transactions.dat', "a")
	