def process(string):
	print('Processing:', string)

f=open('/Users/Emanon/testDir/testPy/tmp.txt')

for line in f:
	process(line)

f.close