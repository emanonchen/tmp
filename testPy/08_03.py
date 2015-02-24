while True:
	try:
		x = input('Enter the first number: ')
		y = input('Enter the second number: ')
		print x/y
	except Exception as e:
		print "Invalid: %s" % e
		print "Plz try again"
	else:
		break