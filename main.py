a= input()
count=0
point=['a','b','c','d','e','f','g','h']
x,y=0,0

for i in range(len(point)): #입력값 좌표설정
  if a[0]==point[i]: x=i+1
y=int(a[1])

if x-2>0:
  if y+1<9: count+=1
  if y-1>0: count+=1
if x+2<9:
  if y+1<9: count+=1
  if y-1>0: count+=1
if y-2>0:
  if x+1<9: count+=1
  if x-1>0: count+=1
if y+2<9:
  if x+1<9: count+=1
  if x-1>0: count+=1
print(count)