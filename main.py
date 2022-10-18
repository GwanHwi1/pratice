for _ in range(1,11):
  t=int(input())
  lst=[list(map(str, input()))for _ in range(100)]
  lst1=[[""]*100 for _ in range(100)]
  for i in range(100):
    for j in range(100):
      lst1[i][j]=lst[j][i]
  result=0
  s1,s2="",""
  for i in range(100,-1,-1):
    for j in range(100):
      for k in range(100-i+1):
        s1="".join(s for s in lst[j][k:k+i])
        s2="".join(s for s in lst1[j][k:k+i])
        tf=True
        tf2=True
        for l in range(len(s1)):
          if s1[l]!=s1[-1-l]: 
            tf=False
            break
        for m in range(len(s2)):
          if s2[m]!=s2[-1-m]: 
            tf2=False
            break
        if tf: result=i
        if tf2: result=i
        tf=True
        tf2=True  
        if result!=0: break
      if result!=0: break
    if result!=0: break
  print(f"#{t} {result}")
            




  