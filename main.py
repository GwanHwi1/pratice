n,m=map(int,input().split())
arr=[]

def permutate(n,m):
  if len(arr)==m:
    result= " ".join(map(str,arr))
    print(result) 
    return  
  for i in range(1,n+1):
    if i in arr: continue
    arr.append(i)
    permutate(n,m)
    arr.pop()

permutate(n,m)