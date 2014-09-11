width = int(input("How wide is the pit? "))
depth = int(input("How deep is the pit? "))
a = width
b = depth
c = 1
for x in range (1, (depth+1)):
	print("|", end="")

	if x<(width+1):
		print(" "*(width-a) , end="")
		print("*", end="")
		print(" "*(width-x), end="")
		a -= 1
	elif x>=(width):
		print(" "*(width-a-2) , end="")
		print("*", end="")
		print(" "*(c), end="")
		a += 1
		c += 1
		if c>(width-1):
			c -= 1
	print("|")
	b -= 1

	