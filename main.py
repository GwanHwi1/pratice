n=int(input())
arr = [[" "for _ in range(n)]for _ in range(n)]

def sol(x,y,n):
  if n==1:
    arr[x][y]="*"
    return
  for i in range(3):
    for j in range(3):
      if (i==1 and j==1): continue
      else: sol(x+i*(n//3), y+j*(n//3), n//3)

sol(0,0,n)
for i in range(n):
  arr[i].append("\n")
result=""
for i in range(n):
  for j in range(n+1):
    result+=arr[i][j]
result=result[:-1]
print(result)