DnaString = raw_input ("Please input a DNA string: ")
nn = 0
counter = 0
while counter < len(DnaString):
    if DnaString[counter] in "ACGTacgt":
	counter += 1
    else:
	counter += 1
	nn += 1
	
print "The number of non-nucleotides is: ", nn
