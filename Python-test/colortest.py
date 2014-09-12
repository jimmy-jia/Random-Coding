print("Welcome to my program! If you put in 2 colors I will combine them for you!")

def color():
	color1 = input("What is the first color?: ").lower()
	color2 = input("What is the second color?: ").lower()

	colorlist = ["red","orange","yellow","green","blue","purple","white","black","brown","grey"]

	if color1 in colorlist:
		if color2 in colorlist:
			print ("Result...")
			if color1 == color2:
				print (color1)
			elif color1 == "red":
				if color2 =="yellow":
					print (colorlist[1])
				elif color2 =="blue":
					print (colorlist[5])
				elif color2 =="red":
					print (colorlist[0])
				elif color2 =="white":
					print ("pink")
				elif color2 =="black":
					print (colorlist[7])
				else:
					print ("Combine primary colors only please!")
					color()
			elif color1 == "blue":
				if color2 =="yellow":
					print (colorlist[3])
				elif color2 =="red":
					print (colorlist[5])
				elif color2 =="blue":
					print (colorlist[4])
				elif color2 =="white":
					print ("sky blue")
				elif color2 =="black":
					print (colorlist[7])
				else:
					print ("Combine primary colors only please!")
					color()
			elif color1 =="yellow":
				if color2 =="yellow":
					print (colorlist[2])
				elif color2 =="red":
					print (colorlist[1])
				elif color2 =="blue":
					print (colorlist[3])
				elif color2 =="white":
					print ("light yellow")
				elif color2 =="black":
					print (colorlist[7])
				else:
					print ("Combine primary colors only please!")
					color()
			elif color1 == "white":
				if color2 =="yellow":
					print ("light yellow")
				elif color2 =="red":
					print ("pink")
				elif color2 =="blue":
					print ("sky blue")
				elif color2 =="white":
					print (colorlist[6])
				elif color2 =="black":
					print (colorlist[9])
				else:
					print ("Combine primary colors only please!")
					color()
			elif color1 == "black":
				if color2 =="white":
					print (colorlist[9])
				else:
					print ("Combine primary colors only please!")
					color()
			else:
				print ("Combine primary colors only please!")
				color()
		else:
			print ("I'm sorry,", color2, "is not in my database!")
			print ("Please try again!")
			color()
	
	elif color2 in colorlist:
		print ("I'm sorry,", color1, "is not in my database!")
		print ("Please try again!")
		color()

	else:
		print ("I'm sorry,", color1, "and", color2, "are not colors in my database!")
		print ("Please try again!")
		color()
		
color()