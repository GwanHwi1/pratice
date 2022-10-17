def flatten(n):
  global result
  boxes.sort()
  result=boxes[-1]-boxes[0]
  if result<=1 or n==0: return result
  boxes[-1]-=1
  boxes[0]+=1
  flatten(n-1)

for t in range(1,11):
  a=int(input())
  boxes=list(map(int,input().split()))
  result=0
  flatten(a)
  print(f"#{t} {result}")

  