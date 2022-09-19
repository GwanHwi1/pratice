t=int(input())
for test in range(1,t+1):
  n=(input())
  count=0
  for i in range(len(n)):
    if n[i]=="(": count+=1
    elif n[i]==")":
      if n[i-1]=="(": continue
      else: count+=1
  print("#"+str(test),count)