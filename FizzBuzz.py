#FizzBuzz
#July 19th, 2019

x = 5
y = 3
xy = x * y

maxRange = 101

word1 = "Fizz"
word2 = "Buzz"
combinedWord = word1 + word2

for i in range(maxRange):
	if i % xy == 0:
		print(combinedWord)
	elif i % x == 0:
		print(word2)
	elif i % y == 0:
		print(word1)
	else:
		print(i)
	
