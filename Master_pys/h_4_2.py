a = []
for x in range(0,1001):
	a.append(True)
a[1] = False

x = 2
while x < pow(1000,0.5):
	if(a[x]):
		for i in range(2,1000//x + 1):
			a[x*i] = False
	x = x + 1

count = 0
for x in range(1,1001):
	if(a[x]):
		print(str(x) ,end=" ")
		count = count + 1
		if(count % 20 == 0):
			print("")
print("")
