import os, random

input = "C:/bin/LatWorks/latin_adjectives.txt"

python_input = open(input, "r")
adjlist = python_input.read()
python_input.close()


eachadj = adjlist.split("\n")

mascdict = {}
femdict = {}
neutdict = {}
englishdict = {}

for adjdef in eachadj:
	adjdefsplit = adjdef.split("\t")
	latin = adjdefsplit[0]
	gender = latin.split(",")
	
#	print gender
	
	masc = gender[0]
	fem = gender[1]
	neut = gender[2]
	allenglish = adjdefsplit[1]
	english = allenglish.split(",")
	#masclist.append(masc)
	#append adds new items to lists without overwriting anything
	#neutlist.append(gender.pop())
	#pop returns the last string item in a list
	
	mascdict[masc] = [fem, neut, english]
	#This inserts each element into its place into the dictionary
	femdict[fem] = [masc, neut, english]
	neutdict[neut] = [masc, fem, english]
	
"""for key in femdict:
	print key + ", " +femdict[key][0] + ", " + femdict[key][1] + ", " + str(femdict[key][2])"""

genderchoice=raw_input("Which gender would you like to be the given form?   ")
if genderchoice=="masculine"or "Masculine":
	print "\n okay then. let's begin."
	masckeys = mascdict.keys()
	random.shuffle(masckeys)

	for mascadj in masckeys:
		x = 0
		print "\n" + mascadj
		guess = "empty string: I have to call it something"
		while guess != mascdict[mascadj][0] and x < 3:
			guess = raw_input("feminine? \n")
			if guess == mascdict[mascadj][0]:
				print "te laudo \n"
			elif x<2:
				print "probably a typo. I believe in you."
				x = x + 1
				print "\n" + (str(x+1))
			else:
				x=x+1 
				print "\n This is the right answer:"
				print mascdict[mascadj][0]
				print " "
		x=0
		guess = "whatever"
		while guess != mascdict[mascadj][1] and x<3:
			guess = raw_input(" neuter? \n")
			if guess == mascdict[mascadj][1]:
				print "te laudo \n"
			elif x<2:
				print "probably a typo. I believe in you."
				x=x+1
				print "\n" +(str(x+1)) 
			else:
				x=x+1
				print "\n This is the right answer:"
				print mascdict[mascadj][1] + "\n"
		x=0
		while x<3:
			guess = raw_input("English translation? \n")
			if guess in mascdict[mascadj][2]:
				print "te laudo \n"
				if len(mascdict[mascadj][2])>1:
					print "These translations would also work:"
					templist = mascdict[mascadj][2]
					templist.remove(guess)
					print ", ".join(templist)
				break
			elif x<2:
				print "hmm try again"
				x=x+1
				print "\n" + str(x+1)
			else:
				x=x+1
				print "\n These are acceptable translations:"
				print ", ".join(mascdict[mascadj][2])
			
			
if genderchoice == "feminine" or "Feminine":
	print "\n okay then. let's begin."
	femkeys = femdict.keys()
	random.shuffle(femkeys)

	for femadj in femkeys:
		x = 0
		print "\n" + femadj
		guess = "empty string: I have to call it something"
		while guess != femdict[femadj][0] and x < 3:
			guess = raw_input("masculine? \n")
			if guess == femdict[femadj][0]:
				print "te laudo \n"
			elif x<2:
				print "probably a typo. I believe in you."
				x = x + 1
				print "\n" + (str(x+1))
			else:
				x=x+1 
				print "\n This is the right answer:"
				print femdict[femadj][0]
				print " "
		x=0
		guess = "whatever"
		while guess != femdict[femadj][1] and x<3:
			guess = raw_input(" neuter? \n")
			if guess == femdict[femadj][1]:
				print "te laudo \n"
			elif x<2:
				print "probably a typo. I believe in you."
				x=x+1
				print "\n" +(str(x+1)) 
			else:
				x=x+1
				print "\n This is the right answer:"
				print femdict[femadj][1] + "\n"
		x=0
		while x<3:
			guess = raw_input("English translation? \n")
			if guess in femdict[femadj][2]:
				print "te laudo \n"
				if len(femdict[femadj][2])>1:
					print "These translations would also work:"
					templist = femdict[femadj][2]
					templist.remove(guess)
					print ", ".join(templist)
				break
			elif x<2:
				print "hmm try again"
				x=x+1
				print "\n" + str(x+1)
			else:
				x=x+1
				print "\n These are acceptable translations:"
				print ", ".join(femdict[femadj][2])
				
if genderchoice == "neuter" or "Neuter":
	print "\n okay then. let's begin."
	neutkeys = neutdict.keys()
	random.shuffle(neutkeys)

	for neutadj in neutkeys:
		x = 0
		print "\n" + neutadj
		guess = "empty string: I have to call it something"
		while guess != neutdict[neutadj][0] and x < 3:
			guess = raw_input("masculine? \n")
			if guess == neutdict[neutadj][0]:
				print "te laudo \n"
			elif x<2:
				print "probably a typo. I believe in you."
				x = x + 1
				print "\n" + (str(x+1))
			else:
				x=x+1 
				print "\n This is the right answer:"
				print neutdict[neutadj][0]
				print " "
		x=0
		guess = "whatever"
		while guess != neutdict[neutadj][1] and x<3:
			guess = raw_input(" feminine? \n")
			if guess == neutdict[neutadj][1]:
				print "te laudo \n"
			elif x<2:
				print "probably a typo. I believe in you."
				x=x+1
				print "\n" +(str(x+1)) 
			else:
				x=x+1
				print "\n This is the right answer:"
				print neutdict[neutadj][1] + "\n"
		x=0
		while x<3:
			guess = raw_input("English translation? \n")
			if guess in neutdict[neutadj][2]:
				print "te laudo \n"
				if len(neutdict[neutadj][2])>1:
					print "These translations would also work:"
					templist = neutdict[neutadj][2]
					templist.remove(guess)
					print ", ".join(templist)
				break
			elif x<2:
				print "hmm try again"
				x=x+1
				print "\n" + str(x+1)
			else:
				x=x+1
				print "\n These are acceptable translations:"
				print ", ".join(neutdict[neutadj][2])
		