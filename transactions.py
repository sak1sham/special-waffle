import datetime

'''
*	Define all different type of money flow streams
*	Take into account all important details
'''
class allTansactionsBinary():
	def __init__(self, clName, obj):
		self.className = clName
		self.obj = obj


class Income:
	def __init__(self, amt, frm, paymode, tax, dt, rep):
		self.Amount = amt
		self.From = frm
		self.PaymentMode = paymode
		self.PercentTax = tax
		self.OtherBenefits = ob
		self.date = dt
		self.repeat = rep

class Expense:
	def __init__(self, amt, frm, to):
		self.Amount = amt
		self.From = frm
		self.To = to

class Loan:
	def __init__(self, amt, frm, paymode, rt, tm):
		self.Amount = amt
		self.From = frm
		self.PaymentMode = paymode
		self.rate = rt
		self.time =  tm

class BankDeposit:
	def __init__(self, amt, ac, dt, frm):
		self.Amount = amt
		self.From = frm
		self.date = dt
		self.Account = ac

class InsurancePremium:
	def __init__(self, amt, dt, rep, paymode):
		self.Amount = amt
		self.date = dt		
		self.repeat = rep
		self.PaymentMode = paymode

class Investment:
	def __init__(self, amt, companyName, dt, paymode, tp):
		self.CompanyName = companyName
		self.Amount = amt
		self.date = dt	
		self.PaymentMode = paymode
		self.Type = tp

class OtherIncome:
	def __init__(self, amt, frm, dt, paymode):
		self.Amount = amt
		self.PaymentMode = paymode
		self.From = frm
		self.date = dt

class OtherExpenses:
	def __init__(self, amt, to, dt, paymode):
		self.Amount = amt
		self.To = to
		self.date = dt
		self.PaymentMode = paymode