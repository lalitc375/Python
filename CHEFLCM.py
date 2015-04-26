# cook your dish here
import math
T=int(input())
while(T>0):
	N=int(input())
	s=int(math.sqrt(N))
	sum=0;
	for i in range(1,s+1):
		if(N%i==0):
			#print (i)
			n=N/i
			
			
			if(n==i):
				sum=sum+n
			else:
				sum=sum+n+i
			
	print(int(sum))
	T=T-1
