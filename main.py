data=input()
a=[]
totalstr=""
total=0
for i in range(len(data)):
  if ord('A')<=ord(data[i])<=ord('Z'):
    a.append(data[i])
  else: total+=int(data[i]) 
a.sort()
for i in a:
  totalstr+=i
print(totalstr+str(total))