checkP = input("Please input number to check if it is prime: ")

# I know this is late, but we did not discuss it in class.

p=0
if (checkP % 2) == 0:
    print checkP, "is not prime."
    p=1
    
if (p == 0):
  n = 3
  while n ** 2 < checkP:
      if (checkP % n) == 0:
	  print checkP, "is not prime"
	  p=1
      n +=2

if (p == 0):
    print checkP, "is prime"
