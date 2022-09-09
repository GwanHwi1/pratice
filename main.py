s= input()
def solution(s):
  result=len(s)
  if len(s)==1: result=1
  for i in range(1,len(s)//2+1):
    arr=[]
    a=0
    while(a<len(s)):
      if len(s)-a<i: 
        arr.append(s[a:])
        a+=i
      else: 
        arr.append(s[a:a+i])
        a+=i
    count=1
    b=[]
    for j in range(len(arr)):
      if j==len(arr)-1:
        if count != 1: b.append(str(count))
        b.append(arr[j])
        break
      if arr[j]==arr[j+1]: count+=1
      else:
        if count!=1:
          b.append(str(count))
          count=1
        b.append(arr[j])
    leng=(''.join(b))
    result=min(result,len(leng))
  return result