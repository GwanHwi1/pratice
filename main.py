t=int(input())
for test in range(1,t+1):
  p,q,r,s,w=map(int, input().split())
  a=p*w
  b=q
  if w>r: b+=(w-r)*s
  print("#"+str(test),min(a,b))