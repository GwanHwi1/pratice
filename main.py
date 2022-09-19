t=int(input())
for i in range(1,t+1):
  n=int(input())
  count=0
  result=""
  for j in range(n):
    alp,num=map(str, input().split())
    for k in range(int(num)):
      result+=alp
      count+=1
      if count%10==0: result+="\n"
  print("#"+str(i))
  print(result)
