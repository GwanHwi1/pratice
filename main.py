def change(arr,n):
  global result
  if n==0:
    a=int("".join(s for s in arr))
    if a>result: result=a
    return
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      arr[i],arr[j]=arr[j],arr[i]
      change(arr,n-1)
      arr[i],arr[j]=arr[j],arr[i]

test_case=int(input())
for t in range(1,test_case+1):
  a,b=map(int, input().split())
  lst=list(str(a))
  result=0
  if b>6: b=6
  change(lst,b)
  print(f"#{t} {result}")