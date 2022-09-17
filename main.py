t=int(input())
for i in range(1,t+1):
  a,b,c,d=map(int,input().split())
  hour=0
  minute=0
  minute=(b+d)%60
  if b+d>59: hour=(a+c+1)%12
  else: hour=(a+c)%12
  if hour==0: hour=12
  print("#"+str(i),hour,minute)