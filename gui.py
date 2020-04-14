import tkinter
## transactions module : do all transactions with a single file containing all classes
import transactions

## accounts module : contains classes for bank accounts, trading accounts and other accounts
import accounts

## Module to verify user details for users using this software
import userVerify

## Module that contains the main operations for the accounts window
import operations

##   IMPORTS COMPLETE



def checkLogin(username, password):
		account = accounts.FinancialManagementAccount(username, password)
		if(userVerify.checkLoginCredentials(account)):
			clearScreen()
			openAccountWindow(username)    
		else:
			clearScreen()
			loginWindow()    
			label = tkinter.Label(win, text = "Incorrect login credentials", fg='red')
			label.pack(pady = 20)	

def checkRegister(username, password):
		account = accounts.FinancialManagementAccount(username, password)
		if(userVerify.userAccountNameFound(account)):
			clearScreen()
			registerWindow()    
			label = tkinter.Label(win, text = "Try with a different Username", fg='green')
			label.pack(pady = 20)
		
		else:
			clearScreen()
			userVerify.addAccountDetails(account)
			openAccountWindow(username)    
				
def createMenuBar():
	menubar = tkinter.Menu(win)
	
	file = tkinter.Menu(menubar, tearoff = 0)
	menubar.add_cascade(label = "File", menu = file)
	file.add_command(label = "Logout", command = goToLoginScreen)
	file.add_separator()
	file.add_command(label ='Exit', command = win.destroy)

	edit = tkinter.Menu(menubar, tearoff = 0)
	menubar.add_cascade(label = "Edit", menu = edit)
	#edit.add_command(label = "Logout", command = goToLoginScreen)

	help = tkinter.Menu(menubar, tearoff = 0)
	menubar.add_cascade(label = "Help", menu = help)
	help.add_command(label = "Help..", command = operations.openExternalHelp)
	
	win.config(menu = menubar)

def firstAddAccountDetails1(username):
	clearScreen()
	textContent = "Dear " + username + ",\n\n Before preceeding, some of your following details is required: \n"
	text1 = tkinter.Label(win, text = textContent, font="Helvetica 18 bold", justify = tkinter.LEFT)
	text1.pack(pady = 20)
	frame = tkinter.Frame(win, relief = tkinter.SOLID ,borderwidth = 1)
	l1 = tkinter.Label(frame, text = "Cash at Hand:", font = ('Ubuntu', 20))
	e1 = tkinter.Entry(frame, font = ('Ubuntu', 20), fg="black", justify = tkinter.CENTER, relief = tkinter.SOLID)
	e1.focus_set()
	l1.grid(row = 0, column = 0, sticky = tkinter.W, pady = 10, padx = 15) 
	e1.grid(row = 0, column = 1, pady = 10, padx = 15) 
	frame.pack(pady = 20)
	b1 = tkinter.Button(win, text="Next (2/5)", fg='#0441cf', command = lambda: firstAddAccountDetails2(username, e1.get()),  font = ('Ubuntu', 16), relief = tkinter.GROOVE) 
	b1.pack(pady = 20)

def firstAddAccountDetails2(username, prevE1):
	clearScreen()
	if(prevE1 != ""):
		obj = accounts.CashAtHand(prevE1) 
		account = accounts.allAccountsBinary("CashAtHand", obj)
		operations.insertAccount(username, "CashAtHand", account)
	
	textContent = "Providing your account details will simplify things for you : \n"
	text1 = tkinter.Label(win, text = textContent, font="Helvetica 18 bold", justify = tkinter.LEFT)
	text1.pack(pady = 20)
	
	frame = tkinter.Frame(win, relief = tkinter.SOLID ,borderwidth = 1)
	
	l1 = tkinter.Label(frame, text = "Bank Name:", font = ('Ubuntu', 20))
	e1 = tkinter.Entry(frame, font = ('Ubuntu', 20), fg="black", justify = tkinter.CENTER, relief = tkinter.SOLID)
	e1.focus_set()
	l1.grid(row = 0, column = 0, sticky = tkinter.W, pady = 10, padx = 15) 
	e1.grid(row = 0, column = 1, pady = 10, padx = 15) 
	
	l2 = tkinter.Label(frame, text = "Balance:", font = ('Ubuntu', 20))
	e2 = tkinter.Entry(frame, font = ('Ubuntu', 20), fg="black", justify = tkinter.CENTER, relief = tkinter.SOLID)
	l2.grid(row = 1, column = 0, sticky = tkinter.W, pady = 10, padx = 15) 
	e2.grid(row = 1, column = 1, pady = 10, padx = 15) 
	
	l3 = tkinter.Label(frame, text = "Account Type:", font = ('Ubuntu', 20))
	e3 = tkinter.Entry(frame, font = ('Ubuntu', 20), fg="black", justify = tkinter.CENTER, relief = tkinter.SOLID)
	l3.grid(row = 2, column = 0, sticky = tkinter.W, pady = 10, padx = 15) 
	e3.grid(row = 2, column = 1, pady = 10, padx = 15) 
	
	l4 = tkinter.Label(frame, text = "Account Holder:", font = ('Ubuntu', 20))
	e4 = tkinter.Entry(frame, font = ('Ubuntu', 20), fg="black", justify = tkinter.CENTER, relief = tkinter.SOLID)
	l4.grid(row = 3, column = 0, sticky = tkinter.W, pady = 10, padx = 15) 
	e4.grid(row = 3, column = 1, pady = 10, padx = 15) 
	
	l5 = tkinter.Label(frame, text = "Account Name (Unique):", font = ('Ubuntu', 20))
	e5 = tkinter.Entry(frame, font = ('Ubuntu', 20), fg="black", justify = tkinter.CENTER, relief = tkinter.SOLID)
	l5.grid(row = 4, column = 0, sticky = tkinter.W, pady = 10, padx = 15) 
	e5.grid(row = 4, column = 1, pady = 10, padx = 15) 
	
	frame.pack(pady = 20)
	b1 = tkinter.Button(win, text="Next (3/5)", fg='#0441cf', command = lambda: firstAddAccountDetails3(username, e1.get(), e2.get(), e3.get(), e4.get(), e5.get()),  font = ('Ubuntu', 16), relief = tkinter.GROOVE) 
	b1.pack(pady = 20)
	b2 = tkinter.Button(win, text="Skip", fg='#0441cf', command = lambda: openAccountWindow(username),  font = ('Ubuntu', 16), relief = tkinter.GROOVE) 
	b2.pack(pady = 20)


def firstAddAccountDetails3(username, bankName, bBalance, accType, accHolder, accName):
	clearScreen()
	if(bankName != "" or bBalance != "" or accType != "" or accHolder != "" or accName != ""):
		bAcc = accounts.BankAccount(accName, bankName, bBalance, accType, accHolder)
		acc = accounts.allAccountsBinary("BankAccount", bAcc)
		if(operations.insertAccount(username, "BankAccount", acc) == 0):
			firstAddAccountDetails2(username, "")
			label = tkinter.Label(win, text = "Account name already taken :(", fg='red')
			label.pack(pady = 20)
			return

	text1 = tkinter.Label(win, text = 'We are almost done !', font="Helvetica 18 bold", justify = tkinter.LEFT)
	text1.pack(pady = 20)
	

def openAccountWindow(username):
	print(operations.isAccountEmpty(username))
	if(operations.isAccountEmpty(username)):
		firstAddAccountDetails1(username)
	else:
		createMenuBar()

def goToLoginScreen():
	clearScreen()
	loginWindow()

def goToRegisterScreen():
	clearScreen()
	registerWindow()

def clearScreen():
	def all_children(window) :
	    _list = window.winfo_children()
	    for item in _list :
	        if item.winfo_children() :
	            _list.extend(item.winfo_children())
	    return _list
	widget_list = all_children(win)
	for item in widget_list:
	    item.pack_forget()
	    
def loginWindow():
	define1 = tkinter.Label(win, text = "A Complete Financial Management Assistant", font="Helvetica 44 bold")
	define2 = tkinter.Label(win, text = "Enter your Login credentials:", font="Helvetica 25 bold")
	define1.pack(pady = 20)
	define2.pack(pady = 20)
	user = tkinter.Entry(win, font = ('Ubuntu', 16), fg="green", justify = tkinter.CENTER, relief = tkinter.SOLID)
	user.pack(pady = 20, ipadx = 30, ipady = 5, side = tkinter.TOP)
	user.focus_set()
	pswd = tkinter.Entry(win, show="*", font = ('Ubuntu', 16), fg="green", justify = tkinter.CENTER, relief = tkinter.SOLID)
	pswd.pack(pady = 20, ipadx = 30, ipady = 5, side = tkinter.TOP)
	button1 = tkinter.Button(win, text="Login", command = lambda: checkLogin(user.get(), pswd.get()), font = ('Ubuntu', 16), fg = '#0b8dd9', relief = tkinter.GROOVE)
	button1.pack(pady = 20)
	label1 = tkinter.Button(win, text = "New user? Create your account !", fg='#0441cf', command = goToRegisterScreen,  font = ('Ubuntu', 12), relief = tkinter.GROOVE)
	label1.pack(pady = 20)

def registerWindow():
	define1 = tkinter.Label(win, text = "A Complete Financial Management Assistant", font="Helvetica 44 bold")
	define2 = tkinter.Label(win, text = "Create your Account credentials:", font="Helvetica 25 bold")
	define1.pack(pady = 20)
	define2.pack(pady = 20)
	user = tkinter.Entry(win, font = ('Ubuntu', 16), fg="green", justify = tkinter.CENTER, relief = tkinter.SOLID)
	user.pack(pady = 20, ipadx = 30, ipady = 5, side = tkinter.TOP)
	user.focus_set()
	pswd = tkinter.Entry(win, show="*", font = ('Ubuntu', 16), fg="green", justify = tkinter.CENTER, relief = tkinter.SOLID)
	pswd.pack(pady = 20, ipadx = 30, ipady = 5, side = tkinter.TOP)
	button1 = tkinter.Button(win, text="Next", command = lambda: checkRegister(user.get(), pswd.get()), font = ('Ubuntu', 16), fg = '#0b8dd9', relief = tkinter.GROOVE)
	button1.pack(pady = 20)
	label1 = tkinter.Button(win, text = "Already have an Account ?", fg='#0441cf', command = goToLoginScreen,  font = ('Ubuntu', 12), relief = tkinter.GROOVE)
	label1.pack(pady = 20)


## Create space for account details
operations.createInitialRoutes()

## Start graphics coding
win = tkinter.Tk()
win.title("A Complete Financial Management Assistant")
win.geometry('500x500')
win.state('zoomed')

loginWindow()
#openAccountWindow("abc")
#firstAddAccountDetails2("abc", "")
win.mainloop()