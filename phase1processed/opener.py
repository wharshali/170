import os
import glob
largeList = []
files = []
for i in range(1, 493):
	s = str(i)
	s += ".in"
	files.append(s)

for filename in files:
	f = open(filename, 'r')
	size = int(f.readline())
	children = list(map(int, f.readline().split()))
	matrix = [[0 for elm in range(size)] for elm in range(size)]
	row = f.readline()
	i = 0
	while (row and i < size):
		r = map(int, row.split())
		for j in range(size):
			matrix[j][i] = r[j]
		row = f.readline()
		i += 1
	largeList.append((size, children, matrix))
print(len(largeList))



