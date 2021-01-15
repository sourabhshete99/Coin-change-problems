#find min number of coins from given coins to make given sum

coins=list(map(int, input('Enter coins (separated by space) : ').split()))
w=int(input('Enter sum/amount : '))

if min(coins)>w:
	print("Invalid data.")
	exit()

ans=[[]]

for i in range(0,len(coins)):
	ans.append([0])
for j in range(0,w+1):
	ans[0].append(j)

for i in range(1,len(coins)+1):
	for j in range(1,w+1):
		if coins[i-1]>j:
			ans[i].append(ans[i-1][j])
		else:
			t=coins[i-1]
			a=min(j,(1+(ans[i][j-t])))
			ans[i].append(a)
			
print(ans[-1][-1])
