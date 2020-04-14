class allAccountsBinary():
	def __init__(self, clName, obj):
		self.className = clName
		self.obj = obj

class CashAtHand:
	def __init__(self, amount):
		self.amount = amount
		
# Account for this software : Folder with account name
class FinancialManagementAccount:
	def __init__(self, AccountName, password):
		self.AccountName = str(AccountName)
		self.password = str(password)

# Following accounts will be saved in a binary encoded format in folders with name = Account name for this software

# BankAccount type = [Savings, Current]		
# Rate of interest, fees and other things will be calculated from the database
class BankAccount:
	def __init__(self, AccountName, BankName, Balance, AccountType, AccountHolder):
		self.AccountName = AccountName
		self.BankName = BankName
		self.Balance = Balance
		self.AccountType = AccountType
		self.AccountHolder = AccountHolder

# Use a tree data structure between Demat ad trading accounts
# contain info of all current stocks, balance, etc.
class DematAccount:
	def __init__(self):
		pass

class TradingAccount:
	def __init__(self):
		pass		