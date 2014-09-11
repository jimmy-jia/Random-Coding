w = int(input("Enter Width: "))
s = int(w) -1
for x in range (1, w+1):
	print (" "*(w-x), end="")
	print ("* "*x)
for x in range (1, w):
	print (" "*(x), end="")
	print ("* "*s)
	s = s-1