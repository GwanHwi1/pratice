t=int(input())
for i in range(1,t+1):
  arr=list(map(int, input().split()))
  arr.sort()
  del arr[9]
  del arr[0]
  print("#"+str(i),round(sum(arr)/8))
