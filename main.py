t=int(input())
for i in range(1,t+1):
  m1,d1,m2,d2=map(int, input().split())
  day31=[1,3,5,7,8,10,12]
  day30=[4,6,9,11]
  day=1
  while(True):
    d1+=1
    day+=1
    if m1 in day31:
      if d1>31:
        m1+=1
        d1=1
    elif m1 in day30:
      if d1>30:
        m1+=1
        d1=1
    else: #2월
      if d1>28:
        m1+=1
        d1=1
    if m1>12: m1-=12
    if m1==m2 and d1==d2:
      break
  print("#"+str(i),day)