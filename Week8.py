#!/usr/bin/env python

#Enter in the DnaSeq in all caps.
complement = []
dnaSeq = input ("Enter dnaSeq here in all caps: ")
dnaSeq = dnaSeq.upper()

dnaSeq = dnaSeq[::-1]
print (dnaSeq)

for i  in dnaSeq: 
	if i == "A":
		complement.append("T")
	elif i == "T":
		complement.append("A")
	elif i == "G":
		complement.append("C")
	elif i == "C":
		complement.append("G")

str2 = ''.join(complement)
print (str2) 

# DB: Good! If you want to avoid the requirement for the user to use all caps, you could
#     add .upper() after you read in the sequence (see above).