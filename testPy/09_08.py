__metaclass__ = type
class Rectangle:
	def __init__(self):
		self.height = 0
		self.width = 0
	def __setattr__(self, name, value):
		if name=="size":
			self.height, self.width = value
		else:
			self.__dict__[name] = value
	def __getattr__(self, name):
		if name == "size":
			return self.height, self.width
		else:
			raise AttributeError

ra = Rectangle()
print ra.__getattr__("size")
ra.__setattr__("size",(1,2))
print ra.__getattr__("size")
ra.__setattr__("abc",1)