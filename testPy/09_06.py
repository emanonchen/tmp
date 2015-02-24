__metaclass__ = type

class MyClass:
	@staticmethod
	def smeth():
		print "this is a static method."
	@classmethod
	def cmeth(cls):
		print "this is a class method of %s" % cls

mc = MyClass()
mc.smeth()
mc.cmeth()