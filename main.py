t=int(input())
for i in range(1,t+1):
  n=int(input())
  a=list(map(int,input().split()))
  profit=0
  maxValue=max(a)
  for j in range(len(a)-1):
    if a[j]<maxValue: profit+=maxValue-a[j]
    else: maxValue=max(a[j+1:])
  print("#"+str(i),profit)
      