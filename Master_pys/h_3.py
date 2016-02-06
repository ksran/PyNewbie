def root(x,guess):
	while abs(guess**3 - x) > 0.001:
		guess = (x/(guess**2) + 2 * guess)/3
	return guess
	
guess = 1.0
x = int(input())
print(root(x,1.0))
