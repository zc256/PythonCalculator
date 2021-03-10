from Calculator.addition import add
from Calculator.subtration import sub
from Calculator.multiplication import mult
from Calculator.division import divide
from Calculator.squared import squared
from Calculator.squareRoot import squareRoot

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
	
	def squareRes(self, a, b):
		self.res = squared(a,b)
		return self.res
	
	def squareRootRes(self, a, b):
		self.res = squareRoot(a,b)
		return self.res