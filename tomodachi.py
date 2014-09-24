import random
import timedate


def start():
	print("Welcome to your Tomodachi, please love me and keep me alive.")
	print("I need food, water, and attention. I also need to sleep and poo!")
	print("If you don't take good care of me, I'll die :(")
	print("Type Help in order to view various inputs.")
	global name = input("Now give me a name! \n")

def main():
	userinput = input("What would you like to do?: ").lower()
	choice(userinput)

def choice(userinput):

	if userinput = help:
		help()




def help():
	print("What would you like help with?")
	print("1: Inputs, 2: Gameplay, 3: Credits")
	helpchoice = input("Choice?: ").lower()
	if helpchoice = 1 or helpchoice = "inputs" 