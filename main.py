test_case=int(input())
lst=[]
for i in range(97,123):
  lst.append(chr(i))
for t in range(1,test_case+1):
  s=input()
  cnt=0
  for i in range(len(s)):
    if s[i]==lst[i]: cnt+=1
    else: break
  print("#"+str(t),cnt)
