x=1
y=1
point={'U':-1, 'D':1, 'L':-1, 'R':1}
point_key=list(point.keys())
n=int(input())
a=list(map(str, input().split()))
count1=count2=count3=count4=0
remove_set={0}
for i in range(len(a)):
  if a[i]=='U': count1+=1
  elif a[i]=='D': count2+=1
  elif a[i]=='L': count3+=1
  else : count4+=1
  if count1>count2 :
    count1-=1
    a[i] = 0
  elif count3>count4 :
    count3-=1
    a[i] = 0
result = [i for i in a if i not in remove_set]
for i in range(n):
  if result[i] == point_key[0] or result[i] == point_key[1] :
    x+=point[result[i]]
    if x<=0: x=1
  else:
    y+=point[result[i]]
    if y<=0: y=1
print(x,y)
