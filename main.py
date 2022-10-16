test_case=int(input())
for t in range(1,test_case+1):
  n=int(input())
  a=list(map(int, input().split()))
  cnt=0
  total=-1
  for i in a:
    if i==1: cnt+=1
  for i in range(len(a)):
    if a[i]==1:
      result=0
      x=0
      y=0
      for j in range(i,len(a)):
        y+=1
        if a[j]==1: x+=1
        if x==n: break        
      result+=y
      rest=n-x
      if rest!=0:
        k = (rest//cnt) 
        if rest%cnt==0 : k-=1
        rest-=(cnt*k)
        result+=(k*7)
        for j in a:
          result+=1
          if j==1: rest-=1
          if rest==0: break
      if total==-1: total=result
      else: total=min(total,result)
  print(f"#{t} {total}")  