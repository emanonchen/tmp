def faulty():
	raise Exception("Sth is wrong")

def ignore_faulty():
	faulty()

def handle_faulty():
	try:
		faulty()
	except:
		print('Exception handled')

#ignore_faulty()
handle_faulty()