test_case=int(input())
for t in range(1,test_case+1):
  s=input()
  prob=0
  for i in s:
    if i=="o":prob+=1
  prob+=(15-len(s))
  if prob>=8: print(f"#{t} YES")
  else: print(f"#{t} NO")
  
