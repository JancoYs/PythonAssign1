DnaString = raw_input ("Input a DNA string of at least six characters: ")
if len(DnaString) < 6:
    print "Please input a string of length six or longer"
else:
     newString = DnaString[:3] + DnaString[-3:]
     print newString
