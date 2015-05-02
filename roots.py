def roots(N,n):

	eps=0.0000001
	qlow=min(-1,N)
	high=max(1,N)
	ans=(qlow+high)/2.0
	while(abs(ans**n-N)>eps):
		if(ans**n<N):
			qlow=ans
		else:
			high=ans
		ans=(high+qlow)/2.0

	return ans
A=float(input('Enter the Number of which u want to Root\n'));
B=float(input('which root u want to find\n'));

print roots(A,B)



