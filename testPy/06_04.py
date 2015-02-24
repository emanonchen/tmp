def change(x):
	x[0] = "Enhen"
names = ["No.1", "No.2"]
change(names[:])
print(names)