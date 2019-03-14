# 杨辉三角
def ok():
	n = int(input("请输入杨辉三角的行数："))
	a = []
	for x in range(n):
		for k in range(1,n-x):
			print(' ',end='')
		b = []
		b.insert(0,1)
		for y in range(x-1):
			b.insert(y + 1, (a[x - 1][y] + a[x - 1][y + 1]))
		if x!=0:
			b.insert(x,1)
		a.append(b)
		for i in b:
			print(i,end=" ")
		print()
ok()
