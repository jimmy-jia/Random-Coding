def fizzbuzz():
	count = int(input("What number do you want to count up to?"))
	for x in range (1, count+1):
		if x%3 ==0 and x%5 == 0:
			print ("FIZZBUZZ")
		elif x%3==0:
			print ("FIZZ")
		elif x%5==0:
			print ("BUZZ")
		else:
			print (x)
fizzbuzz()