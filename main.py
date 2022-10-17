test_case=int(input())
for t in range(1,test_case+1):
  n=input()
  result=0
  tf=-1
  for i in n:
    if tf==-1 and i=="1":
      result+=1
      tf=1
    if tf==1 and i=="0":
      result+=1
      tf=0
    if tf==0 and i=="1":
      result+=1
      tf=1
  print(f"#{t} {result}")