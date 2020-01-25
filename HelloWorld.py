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
	if count >= len(x): # If the length is longer than the string x then it will reset and try again.
		temp = ""
		count = 0
	currTime = "{:.0f}".format(time.time() - time0) # The time since the first call on line 8 limited to whole numbers.
	totalGuesses += 1
	prettyTotalGuesses = "{:,d}".format(totalGuesses) # Turns a hard to read number into a number seperated by commas!
	if totalGuesses % 76820 == 0: # A decent guestimate of 1 second. Its not really accurate and it can deviate but it works.
		print(currTime, "second(s) and a total of", prettyTotalGuesses, "guesses.")
	
