#Peak finding problem in mit lecture
#implementation in Python
A=[10,25,16,5,25,60,100,200,400,100,1600]
n =len(A)-1
high=n;
low=0
mid=(high+low)//2;
while( mid-1 >= 0 and mid+1 <= n ):
	if(A[mid]<A[mid-1]):
		high=mid-1
	elif (A[mid]<A[mid+1]):
		low=mid+1
	else:
		break
	mid=(high+low)//2
print (A[mid])