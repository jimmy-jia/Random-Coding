print("This program checks if your input is a palindrome or now!")
input = input("Type in your string here! \n").lower()
reverse = ""
len = len(input)
for i in range(len-1,-1,-1):
	reverse += input[i]
if input == reverse:
	print("Yes!", input, "is a palindrome!")
else:
	print("Sorry!", input, " is not a palindrome!")