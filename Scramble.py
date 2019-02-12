# Variona
saying_obj = open("sayings.txt", "r")
saying_list = []


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for line in saying_obj:
	saying_list.append(line)


for i in saying_list:
	newAscii = 0
	scramWord = ""
	for i2 in i:
		if i2 not in alphabet:
			scramWord += i2
		elif i2 == "y":
			scramWord += alphabet[1]
		elif i2 == "Y":
			scramWord += alphabet[27]
		elif i2 == "z":
			scramWord += alphabet[2]
		elif i2 == "Z":
			scramWord += alphabet[28]
		else:
			newAscii = ord(i2) + 3
			scramWord += chr(newAscii)
			

	print(scramWord,end = "\n")
