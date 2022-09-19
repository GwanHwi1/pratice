t=int(input())
for i in range(1,t+1):
  n=int(input())
  arr=[2,3,5,7,11]
  result=[0,0,0,0,0]
  while(n!=1):
    for j in range(len(arr)):
      if n%arr[j]==0:
        n/=arr[j]
        result[j]+=1
      else:
        continue
  print("#"+str(i),*result)
