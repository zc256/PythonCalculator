from addition import add
from subtraction import sub
from multiplication import mult
from division import divide
from squared import squared
from squareRoot import squareRoot

class Calculator:
	res = 0
	def __init__(self):
		pass

	def addRes(self, a, b):
		self.res = add(a,b)
		return self.res
	
	def subRes(self, a, b):
		self.res = sub(a,b)
		return self.res
	
	def multRes(self, a, b):
		self.res = mult(a,b)
		return self.res
	
	def divRes(self, a, b):
		self.res = divide(a,b)
		return self.res
	
	def squareRes(self, a):
		self.res = squared(a)
		return self.res
	
	def squareRootRes(self, a):
		self.res = squareRoot(a)
		return self.res