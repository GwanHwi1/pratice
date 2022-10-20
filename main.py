def check(a):
  global tf,k,arr
  if k>=len(arr): k=len(arr)
  for i in range(k):
    if m*a>arr[i]: 
      tf=False
      break
  if not tf or len(arr)==0: return
  else: 
    arr=arr[k:]
    check(a+1)

test_case=int(input())
for t in range(1,test_case+1):
  n,m,k=map(int,input().split())
  arr=list(map(int,input().split()))
  arr.sort()
  tf=True
  check(1)
  if tf: print(f"#{t} Possible")
  else: print(f"#{t} Impossible")
