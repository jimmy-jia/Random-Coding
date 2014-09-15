print("\nLets see what homework you have coming up!\n")
import datetime
now = datetime.datetime.now()
now = now.strftime("%A")
print ("Today is", now, "\n")
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekday = 0
for i in range(0, 6):
	if now == days[i]:
		weekday = i

work = ["Work Due Monday: \nJapanese\n", "Work Due Tuesday: \nPhysics \nMath \n", "Work Due Wednesday: \nECE \n", "Work Due Thursday: \nMath \nPhysics \n", "Work Due Friday: \nNothing! \n", "Work Due Saturday: \nMath \n", "Work Due Sunday: \nNothing! \n"]
for i in range(0, 4):
	print(work[int(weekday)-1+i])