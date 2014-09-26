import random
import datetime


def start():
	print("Welcome to your Tomodachi, please love me and keep me alive.")
	print("I need food, water, and attention. I also need to sleep and poo!")
	print("If you don't take good care of me, I'll die :(")
	print("Type Help in order to view various inputs.")
	global name
	name = input("Now give me a name!: ")
	global timeold
	timeold = datetime.datetime.now()
	main()

def main():
	global userinput
	userinput = input("\nWhat would you like to do?: ").lower()
	choice(userinput)


def timecheck():
	global hour
	global minute
	global now
	now = datetime.datetime.now()
	hour = now.hour
	minute = now.minute
	mytimedelta()

def mytimedelta():
	global timedif
	timedif = now - timeold
	global cdiff
	cdiff = divmod(timedif.days*86400 + timedif.seconds, 60)

def choice(userinput):

	if userinput == "help":
		help()
	if userinput == "timecheck":
		timecheck()
		print ("Current time is: "+str(hour)+":"+str(minute))
		print ("The last time you checked on", name, "was at", str(hour)+":"+str(minute)+ ".")
		print ("Time difference is", timedif.minutes, "minutes and", timedif.seconds, "seconds.")
		main()
	if userinput == "name":
		print ("Your pet's name is", name +",","how could you forget!")
		main()
	if userinput == "sleep":
		timecheck()
		mytimedelta()
	if userinput == "hunger"
		hunger()
	if userinput == "1":
		mytimedelta()
		print(timedif)
	print("Sorry, I don't recognize that input, please try again! \nIf you don't remember the inputs, please type help!")
	main()



def help():
	print("\nWhat would you like help with?")
	print("1: Inputs, 2: Gameplay, 3: Credits, 4: Return to Game")
	helpchoice = str(input("Choice?: ")).lower()
	if helpchoice == "1" or helpchoice == "inputs":
		print("Inputs are:")
		print("Timecheck = Current time")
		print("Name = Your pet's name")
		print("Hunger = Your current pet hunger")
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

def hunger():

	if fed <25:
		print("Your pet is nearly dead! You need to feed him!")
	elif fed <50:
		print("Your pet is hungry! You should feed him!")
	elif fed <100:
		print("Your pet is ok! He is satisfied with his tumtum!")
	elif fed =100:
		print("Wow you just fed him! Great job!")
	elif fed >100:
		print("You overfed him :( be careful!")
	main()



start()