n= int(input())
count1=0
count2=0
count3=0
for i in range(60): #60초
  if i<10:
    if i==3: count1+=1
  if i>=10:
    if str(i)[0]=='3' or str(i)[1]=='3': count1+=1
for i in range(60): #60분
  if i<10:
    if i==3: count2+=60
    else: count2+=count1
  if i>=10:
    if str(i)[0]=='3' or str(i)[1]=='3': count2+=60
    else: count2+=count1
for i in range(n+1): #n시간
  if i < 10:
    if i==3: count3+=3600
    else: count3+=count2
  if i >=10:
    if str(i)[0]=='3' or str(i)[1]=='3': count3+=3600
    else: count3+=count2
print(count3)

  
  