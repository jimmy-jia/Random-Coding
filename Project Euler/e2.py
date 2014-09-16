a = 1
b = 2
sum = 2

def fib():
	global a
	global b
	global sum
	if b < 4000000:
		a = a + b
		if a % 2 == 0:
			sum = a + sum
		b = a + b
		if b % 2 == 0:
			sum = b + sum
		fib()
		
fib()
print (sum)