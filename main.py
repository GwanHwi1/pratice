for t in range(1,11):
  n=int(input())
  lst=[list(map(str,input()))for _ in range(8)]
  cnt=0
  s=""
  s1=""
  for i in range(8):
    for j in range(8-n+1):
      s="".join(a for a in lst[i][j:j+n])
      for k in range(j+n-1,j-1,-1):
        s1+=lst[i][k]
      if s==s1: cnt+=1
      s=""
      s1=""
  for i in range(8):
    for j in range(8-n+1):
      for k in range(j,j+n):
        s+=lst[k][i]
      for k in range(j+n-1,j-1,-1):
        s1+=lst[k][i]
      if s==s1: cnt+=1
      s=""
      s1=""
  print(f"#{t} {cnt}")

