class Fibs:
	def __init__(self):
		self.a = 0
		self.b = 1
	def next(self):
		self.a, self.b = self.b, self.a+self.b
		return self.a
	def __iter__(self):
		return self

f = Fibs()
for i in f:
	if i>1000:
		print i
		break