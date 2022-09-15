t=int(input())
for i in range(1,t+1):
  a=input()
  part=0
  result=0
  for j in range(1,11):
    arr=[]
    for k in range(0,len(a)-j,j):
      arr.append(a[k:k+j])
    for k in range(len(arr)):
      if k==len(arr)-1: break
      else:
        if arr[k]==arr[k+1]: result=1
        else:
          result=0
          break
    if result==1: 
      part=j
      break
  print('#'+str(i),part)