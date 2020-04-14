import webbrowser
import os
import subprocess

def openExternalHelp():
	webbrowser.open('https://sak1sham.github.io', new=2)

def createInitialRoutes():
	if not os.path.exists('./_data'):
	    os.makedirs('./_data')
	subprocess.check_call(["attrib","+H","./_data"])
	open('./_data/accountDetails.dat', "a")

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

def isTransactionsEmpty(username):
	for item in read_from_pickle('./_data/' + username + '/transactions.dat'):
		i = item
		if(i.className == i.className):
			return 0
	return 1    	

def printAccountDetails(username):
	for item in read_from_pickle('./_data/' + username + '/accounts.dat'):
		i = repr(item)
		print(i)

def isAccountEmpty(username):
	for item in read_from_pickle('./_data/' + username + '/accounts.dat'):
		i = item
		if(i.className == i.className):
			return 0
	return 1   	

def insertAccount(username, type, account):
	found = False
	open('./_data/'+ username +'/temp.dat', "a")
	for item in read_from_pickle('./_data/' + username + '/accounts.dat'):
		i = item
		if(i.className == type and found != True):
			if(type == "CashAtHand"):
				i.obj.amount += account.obj.amount
				add_to_pickle('./_data/' + username + '/temp.dat', i)
				found = True
				continue
			elif(type == "BankAccount" and i.obj.AccountName == account.obj.AccountName):
				found = True
				return 0
			elif(type == "BankAccount"):
				add_to_pickle('./_data/' + username + '/temp.dat', i)
				continue	
		add_to_pickle('./_data/' + username + '/temp.dat', i)
	
	os.remove('./_data/'+ username +'/accounts.dat')
	os.rename('./_data/'+ username +'/temp.dat', './_data/'+ username +'/accounts.dat')
	
	if(found != True):
		add_to_pickle('./_data/' + username + '/accounts.dat', account)
	
	return 1	