test_case=int(input())
for t in range(1,test_case+1):
  s=input()
  result=0
  a=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN' ]
  today=a.index(s)
  if today==6: result=7 
  else:
    for i in range(today,6): 
      result+=1
  print(f"#{t} {result}")
