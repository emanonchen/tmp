def flatten(nested):
	try:
		try:
			nested+''
		except TypeError:
			pass
		else:
			raise TypeError
		for sublist in nested:
			for element in flatten(sublist):
				yield element
	except TypeError:
		yield nested

#nested = [[[1,2],3],[4],[5,6,7,8]]
nested='abc'
l=list(flatten(nested))
print l