for t in range(1,11):
  n=int(input())
  buildings=list(map(int, input().split()))
  result=0
  for i in range(2,len(buildings)-2):
    a=max(buildings[i-2],buildings[i-1],buildings[i+1],buildings[i+2])
    if a<buildings[i]:
      result+=buildings[i]-a
  print(f"#{t} {result}")

  

