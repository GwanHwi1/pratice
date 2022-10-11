n,m = map(int, input().split())
arr=[]

def combinate(a):
  if len(arr)==m:
    result=" ".join(map(str, arr))
    print(result)
    return
  for i in range(a,n+1):
    if i in arr: continue
    arr.append(i)
    combinate(i+1)
    arr.pop()

combinate(1)