#Quite possibly the best program to print "Hello World" ever.
from random import randint
from random import seed
x = "Hello World" 
temp = ""
count = 0
print("Starting...")

while True:
	seed()
	temp += str(x[randint(0,len(x)-1)])
	count += 1
	
	if temp == x:
		print(x)
		break
	if count >= len(x):
		temp = ""
		count = 0
