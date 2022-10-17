a=[[1,2,3],[1,2,3],[1,2,3]]
b=[[0]*3 for _ in range(3)]
for i in range(3):
  for j in range(3):
    b[i][j]=a[j][i]

print(b)