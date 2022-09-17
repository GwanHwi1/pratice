t=int(input())
for i in range(1,t+1):
  money=int(input())
  count=0
  arr=[50000,10000,5000,1000,500,100,50,10]
  balance=[]
  for j in range(len(arr)):
    cal=money//arr[j]
    balance.append(cal)
    if cal>0: money-=arr[j]*cal
  print("#"+str(i))
  print(*balance)
