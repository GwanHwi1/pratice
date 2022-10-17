def checking(a):
  global cnt
  if len(arr)==n: 
    cnt+=1
    return
  for i in range(n):
    if exclude(a,i):
      arr.append([a,i])
      checking(a+1)
      arr.pop()
      
def exclude(x,y):
  tf=True
  for i in range(len(arr)):
    if arr[i][0]==x or arr[i][1]==y or abs(x-arr[i][0])==abs(y-arr[i][1]):
      tf=False
      break
  return tf
    
test_case=int(input())
for t in range(1,test_case+1):
  n=int(input())
  cnt=0
  arr=[]
  checking(0)
  print(f"#{t} {cnt}")

