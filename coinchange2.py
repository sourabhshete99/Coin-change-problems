#	find total number of ways to make given sum from given coins

coins=list(map(int, input('Enter the coins (separated by space : )').split()))
w=int(input('Enter sum : '))

if min(coins)>w:
	print("Invalid data.")
	exit()

ans=[[]]

for i in coins:
	ans.append([1])
for j in range(0,w+1):
	ans[0].append(0)

for i in range(1,len(coins)+1):
	for j in range(1,w+1):
		if coins[i-1]>j:
			ans[i].append(ans[i-1][j])
		else:
			a=coins[i-1]
			ans[i].append(ans[i-1][j]+ans[i][j-a])

print(ans[-1][-1])
