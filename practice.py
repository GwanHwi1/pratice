count1=0
for i in range(60): #60초
  if i<10:
    if i==3: count1+=1
  if i>=10:
    if str(i)[0]=='3' or str(i)[1]=='3': count1+=1

print(count1)