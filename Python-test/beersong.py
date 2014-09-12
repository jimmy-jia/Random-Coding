bottles = int(99)

def ask():
	cont = input("Once more? Yes or No? ").lower()
	if cont == "yes":
		beer()
	elif cont == "no":
		print("Aww, you're no fun!")
	else:
		print("You're so drunk I can't understand you!")

def beer():
	a = bottles
	for x in range (1, bottles):
		print (a, "bottles of beer on the wall,", end=" ")
		print (a, "bottles of beer!")
		print ("Take one down, pass it around,", end=" ")
		a = a - 1
		print (a, "bottles of beer on the wall! \n")

	print ("No more bottles of beer on the wall,", end=" ")
	print ("no more bottles of beer!")
	print ("Go to the store and buy some more,", end=" ")
	print ("99 bottles of beer on the wall! \n")
	ask()

beer()