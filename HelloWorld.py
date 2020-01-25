#Quite possibly the best program to print "Hello World" ever.
from random import randint
from random import seed
import time
x = "Hello World" 
temp = ""
count = 0
time0 = time.time()
totalGuesses = 0
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
	currTime = "{:.0f}".format(time.time() - time0)
	totalGuesses += 1
	prettyTotalGuesses = "{:,d}".format(totalGuesses)
	if totalGuesses % 76820 == 0:
		print(currTime, "second(s) and a total of", prettyTotalGuesses, "guesses.")
	
