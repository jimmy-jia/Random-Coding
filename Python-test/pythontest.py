
print ("You slowly wake... up dazed and groggy. \nYou look around and see only an unfamiliar room")
print ("You try to to think, what were you doing last night? What was your name even?")
name = input("What is your name?")
print ("Suddenly it comes to you, you remember your name to be %s." % name)
from datetime import datetime
now = datetime.now()
year = now.year
month = now.month
day = now.day
minute = now.minute
hour = now.hour
"""print (month, day, year)
print (str(month)+"/"+str(day)+"/"+str(year))
print ("%s/%s/%s" % (month, day, year))"""
print ("You look around the room once again, slowly gaining your senses.")
def game():
	def room1():
		print ("You see a clock, a mirror, and a door...")
		a1 = input("Which one do you look at? ")
		if a1 == "clock":
			print ("You go up to the clock and look at it. It seems to be digital. The time and date read:")
			print ("%s/%s/%s, %s:%s" % (month, day, year, hour, minute))
			print ("Well now you know what time it is!")
			print ("Bored of the clock, you look back up.")
			room1()
		elif a1 == "mirror":
			print ("You go up to the mirror, looking at your self. Your hair is messy and dirty")
			print ("It looks like you've been here a while.")
			print ("You mess with your hair a bit but nothing helps. You decide to look back at the room.")
			room1()
		elif a1 == "door":
			print ("You go up to the door and turn the knob... it opens and you walk into hall way.")
			room2()
		else:
			print ("You twiddle your thumbs")
			print ("You decide to look around the room again")
			room1()
	room1()

def room2():
	print ("You're in the hallway now. It is long enough so that you can't see the end.")
room2()
game()

