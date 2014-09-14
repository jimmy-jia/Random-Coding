import random

rand = random.randint(0, 999)

print("\nThis program generates a random number between 0 and 999")
print("Please try and guess it!")
b = 0
def guess():
	global b
	global rand
	d = input("\nWhat is your guess? \n \n")
	b = b+1
	strcheck(d)
	a = int(d)
	if a == rand:
		print("\nGood Job, you did it!")
		print("You took", b, "guesses to find it! \n")
		play = input("Would you like to play again? \n \n").lower()
		if play == "yes":
			b = 0
			rand = random.randint(0,999)
			guess()
		else:
			print("\nSorry to see you go, come back again soon!")
			exit()
	elif a > 999:
		print("\nThats higher than the max! Try again!")
		guess()
	elif a < 0:
		print("\nThe number isn't negative! Try again!")
		guess()
	elif a > rand:
		print("\nToo high! Try again!")
		guess()
	elif a < rand:
		print("\nToo low! Try again!")
		guess()
	else:
		print("\nI'm not sure how you got here, but please try again!")
		guess()

def strcheck(d):
	try:
		float(d)
		return True
	except ValueError:
		print ("\nThats not a number, please try again!")
		guess()
		return False
guess()