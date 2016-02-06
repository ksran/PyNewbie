def Fib(x):
	if x == 1 or x == 2:
		return 1
	return Fib(x - 1) + Fib(x - 2)

x = int(input())
print(Fib(x))
