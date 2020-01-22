matrix = []

row = 0
column = 0
with open("save_master_yoda_ascii.txt") as fileobj:
	for line in fileobj:  
		matrix.append(line.split('c'))
	



matrix2 = []

row = 0
column = 0
with open("yoda_ascii.txt") as fileobj:
	for line in fileobj:  
		matrix2.append(line.split('\n'))
	
	
matrix3 = [[" " for i in range(141)]for j in range(30)]

for i in range(17):
	for j in range(74):
		matrix3[i][j] = matrix[i][0][j]

for i in range(20):
	for j in range(74,119):
		matrix3[i][j] = matrix2[i][0][j - 74]

st = ''
for i in range(30):
	for j in range(141):
		st+=matrix3[i][j]
	st+='\n'

print(st)		


