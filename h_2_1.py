num = input()
l = len(num) - 1
num = int(num)
ans = 0
con = 0
index = 0
while l >= 0:
	index = num // (10 ** l)
	ans = ans + index * (10 ** con)
	num = num - index * (10 ** l)
	con = con + 1
	l = l - 1
print(ans)
