n = int(input())
sum = 0
while n > 0:
	m = n
	mul = 1
	while m > 0:
		mul = mul * m
		m = m - 1
	sum = sum + mul
	n = n -1
print(sum)
