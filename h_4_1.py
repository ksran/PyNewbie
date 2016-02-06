def isPrime(x):
	if x == 1:
		return False
	for i in range(2,x):
		if x % i == 0:
			return False
	return True

for i in range(1,1000):
	if isPrime(i):
		print(i)
