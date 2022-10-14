test_case=int(input())
for t in range(1,test_case+1):
  n,d=map(int, input().split())
  a=d*2+1
  cnt=n//a
  if n%a!=0: cnt+=1
  print(f"#{t} {cnt}")
