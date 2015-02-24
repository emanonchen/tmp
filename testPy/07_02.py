class Calculator:
	def calculator(self, expression):
		self.value = eval(expression)

class Talker:
	def talk(self):
		print "The result is %s." % self.value

class TalkingCalculator(Calculator,Talker):
	pass

tc=TalkingCalculator()
tc.calculator('1+2+3')
tc.talk()