test_case=int(input())
for t in range(1,test_case+1):
  n=input()
  total=[]
  for i in range(2,10):
    s=int(n)*i
    total.append(sorted((str(s))))
  if sorted(n) in total: print(f"#{t} possible")
  else: print(f"#{t} impossible")
  
