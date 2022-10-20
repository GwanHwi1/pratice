lst=[[]]
# def makeList(a,b,c):
#   if a==0: return
#   if c==0: b,c=c+1,b  
#   lst.append([b,c])
#   makeList(a-1,b+1,c-1)
# makeList(10000,1,1)
a=50000
c=1
b=1
while a>0:
  if c==0: b,c=c+1,b
  lst.append([b,c])
  a-=1
  b+=1
  c-=1

test_case=int(input())
for t in range(1,test_case+1):
  p,q=map(int,input().split())
  w,x=map(int,lst[p])
  y,z=map(int,lst[q])
  w+=y
  x+=z
  for i in range(len(lst)):
    if lst[i]==[w,x]: print(f"#{t} {i}")