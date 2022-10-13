def color(arr,c1,c2):
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      if arr[i][j]!="?":
        if (i+j)%2==0 and arr[i][j]!=c1: return False
        if (i+j)%2==1 and arr[i][j]!=c2: return False
  return True

test_case=int(input())
for t in range(1,test_case+1):
  n,m=map(int,input().split())
  puzzle=[list(map(str,input()))for _ in range(n)]
  if color(puzzle,".","#") or color(puzzle,"#","."): print("#"+str(t),"possible")
  else: print("#"+str(t),"impossible")