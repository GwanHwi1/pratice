t=int(input())
for test in range(1,t+1):
  n=int(input())
  score=list(map(int,input().split()))
  result=0
  maxValue=0
  for i in range(100,-1,-1):
    count=score.count(i)
    if maxValue<count:
      maxValue=count
      result=i
  print("#"+str(n),result)
      