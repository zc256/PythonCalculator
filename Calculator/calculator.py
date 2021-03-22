from Calculator.addition import add
from Calculator.subtraction import sub
from Calculator.multiplication import mult
from Calculator.division import divide
from Calculator.squared import squared
from Calculator.squareRoot import squareRoot
from Calculator.addSub import addSub
from Calculator.sqrtSquared import sqrtSquared
from Calculator.multAdd import multAdd
from Calculator.addSubDiv import addSubDiv

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

	def addSub(self,a,b,c,d):
		self.res = addSub(a,b,c,d)
		return self.res

	def sqrtSquared(self, a):
		self.res = sqrtSquared(a)
		return self.res

	def multAdd(self,a,b,c,d):
		self.res = multAdd(a,b,c,d)
		return self.res

	def addSubDiv(self,a,b,c,d,e):
		self.res = addSubDiv(a,b,c,d,e)
		return self.res