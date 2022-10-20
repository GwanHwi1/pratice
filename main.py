def square(a):
  if a<=0: return 1
  return n * square(a-1)

for _ in range(1,11):
  t=int(input())
  n,m=map(int,input().split())
  print(f"#{t} {square(m)}")