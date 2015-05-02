first_str='Lalit Chauhan'
second_str="Vinod Kumar Chauhan"
print(first_str.upper())  #Change all alphabets into Upper Case
print(first_str.replace('Lalit','Rohit')) #Return a New string After Replacement of String
print(first_str.split(' ')) #Return a List of String After Replacement 
print(first_str.isdigit()) #Check it is a Digit or Not
T=first_str.split(' ') 
print(T[0])
T.sort()
for x in T:
	print x
	pass
print(first_str[first_str.find('L')]) #Find Method


