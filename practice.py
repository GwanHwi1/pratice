n=int(input())
for i in range(1,n+1):
  count=0
  for j in str(i):
    if j =='3' or j=='6' or j=='9': count+=1
  if count!=0:
    print('-'*count,end=" ")
  else: print(i,end=" ")