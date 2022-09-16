t=int(input())
for i in range(1,t+1):
  a=input()
  b=""
  result=0
  for j in range(len(a)-1,-1,-1):
    b+=a[j]
  if a==b: result=1
  print("#"+str(i),result)