counter = 1
row = int(input("Input Row Number: "))
while row>26:
	row = row-26
	counter += 1
print(chr(ord('A')+row-1)*counter)