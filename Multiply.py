def Multiply(A,B):
	if(B==0):
		return 0
	elif (B<0):
		return -1*A-Mulpliply(A,-1*B+1)
	else:
		return A+Multiply(A,B-1)
print (Multiply(10,20))
