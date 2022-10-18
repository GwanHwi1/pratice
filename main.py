from collections import deque

for _ in range(1,11):
  t=int(input())
  q=deque()
  lst=list(map(int,input().split()))
  q=deque(lst)
  
  while True:
    for i in range(1,6):
      a=q[0]
      q.append(a-i)
      q.popleft()
      if q[-1]<=0:
        q[-1]=0
        break
    if q[-1]==0:
      break
  s=""
  for i in range(8):
    s+=str(q[i])+" "
  print(f"#{t}",s.rstrip())


