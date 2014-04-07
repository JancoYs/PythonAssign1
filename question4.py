DnaString = raw_input("Please input a DNA string: ")

nn = 0
counter = 0
while counter < len(DnaString):
    if DnaString[counter] in "ACGTacgt":
	counter += 1
    else:
	counter += 1
	nn += 1

if nn > 0:
  print "Please enter a DNA string containing only A, C, G, T and a, c, g, t"
else:
  reverse = DnaString[::-1]
  print "The Reverse is : ", reverse
