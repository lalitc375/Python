#Peak finding problem in mit lecture
A=[[10,25,16],[5,25,60],[100,200,40],[200,400,100],[400,10,1000]]
n =len(A)-1
print(n)
high=n;
low=0
mid=(high+low)//2;
while( mid-1 >= 0 and mid+1 <= n ):
	if(max(A[mid])<max(A[mid-1])):
		high=mid-1
	elif (max(A[mid])<max(A[mid+1])):
		low=mid+1
	else:
		break
	mid=(high+low)//2
print (max(A[mid]))