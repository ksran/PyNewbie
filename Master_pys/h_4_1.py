def isPrime(x):
	if x <= 2:
		return x == 2
	for i in range(2,x):
		if x % i == 0:
			return False
	return True

while True:
	x = int(input())
	if isPrime(x):
		print('Yes')
	else:
		print('No')
