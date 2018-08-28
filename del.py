import random
p1=str(random.randint(1000,9999))
print "The computer has selected a 4 digit number "
game=True
while game:
	guess=0
	cow=0
	bull=0	
	i=0
	wanaplay=raw_input("Wana Play?")
	if wanaplay.lower()=="yes":
		p2=raw_input("Number")
		while len(p1)!=len(p2):
			print "enter a 4 digit number bro :\n"
			p2=raw_input("Number: ")
		if len(p1)==len(p2):
			for i in range(4):
				if p1[i]==p2[i]:
					cow=cow+1
				else:
					bull=bull+1
			i=i+1
	
			guess+=1
			print "guess=",guess
			print "cow=",cow
			print "bull=",bull
	else:
		print "bye"
		game=False