__metaclass__ = type
class Bird:
	def __init__(self):
		self.hungry = True
	def eat(self):
		if self.hungry:
			print "Aaaaah"
			self.hungry = False
		else:
			print "No, thx!"

class SongBird(Bird):
	def __init__(self):
		super(SongBird,self).__init__()
		self.sound = 'YooyoQieKeNao~'
	def sing(self):
		print self.sound

b = Bird()
sb = SongBird()

b.eat()
b.eat()

sb.sing()
sb.eat()
sb.eat()