try:
	1/0
except ZeroDivisionError as e:
	print(e)
else:
	print("That went well")
finally:
	print("Cleaning up")