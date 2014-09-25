import random
import datetime


def start():
	print("Welcome to your Tomodachi, please love me and keep me alive.")
	print("I need food, water, and attention. I also need to sleep and poo!")
	print("If you don't take good care of me, I'll die :(")
	print("Type Help in order to view various inputs.")
	global name
	name = input("Now give me a name!: ")
	main()

def main():
	global userinput
	userinput = input("\nWhat would you like to do?: ").lower()
	choice(userinput)


def timecheck():
	global hour
	global minute
	timenew = datetime.time
	now = datetime.datetime.now()
	hour = now.hour
	minute = now.minute


def choice(userinput):

	if userinput == "help":
		help()
	if userinput == "timecheck":
		timecheck()
		print ("Current time is:", hour, ":",minute)
		main()
	if userinput == "name":
		print ("Your pet's name is", name +",","how could you forget!")
		main()
	print("Sorry, I don't recognize that input, please try again!")
	main()



def help():
	print("\nWhat would you like help with?")
	print("1: Inputs, 2: Gameplay, 3: Credits, 4: Return to game")
	helpchoice = str(input("Choice?: ")).lower()
	if helpchoice == "1" or helpchoice == "inputs":
		print("Inputs are:")
		print("Timecheck = Current time")
		print("Name = Your pet's name")
		helpask()
	elif helpchoice == "2" or helpchoice == "gameplay":
		print("Play the game\n")
		helpask()
	elif helpchoice == "3" or helpchoice == "credits":
		print("Created by Jimmy Jia\n")
		helpask()
	elif helpchoice == "4" or helpchoice == "return" or helpchoice =="return to game":
		main()

def helpask():
	morehelp = input("Would you like more help? ").lower()
	if morehelp == "yes":
		help()
	elif morehelp == "no":
		main()
	else:
		print("Please type either yes or no.")
		helpask()


start()