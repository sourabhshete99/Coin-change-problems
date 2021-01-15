#	find min number of denominations required to make given sum, denominations such as (0,1,2,3,4,....., upto given sum)

w=int(input('Enter the number as sum : '))
rem=[]
ans=0

n=w
while n>0:
	rem.append(n%2)
	n=n//2
	ans+=1
	
print(ans)

# another method to do this is find the binary of given number, length of that binary number is answer
# and method to find binary is keep track of remainder in order which get after each division operation and then reverse the numbers we get as remainders
