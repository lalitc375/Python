#SLAYERS+SLAYERS+SLAYERS=LAYERS
#project 3 of msu.cse
slayers=int(input('Enter the Six Digit Number \t'))
if(slayers//100000!=0 and slayers//1000000==0):
	if (((slayers%100000)*10+slayers//100000)==3*slayers):
		print ('SLAYERS+SLAYERS+SLAYERS=LAYERS')
		print (slayers,'+',slayers,'+',slayers,'=',((slayers%100000)*10+slayers//100000))
	else:
		print('Incorrect guess')
else:
	print('Number should of six digit')

#print ((slayers%100000)*10+slayers//100000)


