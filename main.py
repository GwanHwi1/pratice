def search():
  for i in range(n):
    for j in range(n):
      if board[i][j]=="#": return [i,j]

test_case=int(input())
for t in range(1,test_case+1):
  n=int(input())
  board=[list(map(str,input()))for _ in range(n)]
  cnt=0
  tf=True
  length=0
  arr=search()
  
  for i in range(arr[1],n):
    if board[arr[0]][i]==".": break
    else: length+=1

  for i in range(n):
    for j in range(n):
      if arr[0]<=i<arr[0]+length and arr[1]<=j<arr[1]+length:
        if board[i][j]==".":
          tf=False
      else:
        if board[i][j]=="#":
          tf=False
  if tf==True: print(f"#{t} yes")
  else: print(f"#{t} no")
            