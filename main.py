n=int(input())
for i in range(n):
  result=0
  a=str(i)
  for j in a:
    result+=int(j)
  result+=i
  if result==n:
    print(i)
    break
  elif result!=n and i==n-1:print(0)
