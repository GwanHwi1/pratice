t=int(input())
for i in range(1,t+1):
  n,k=map(int, input().split())
  student=[]
  for _ in range(n):
    a=list(map(int, input().split()))
    student.append(a[0]*0.35+a[1]*0.45+a[2]*0.2)
  score=student[k-1]
  student.sort(reverse=True)
  grade=(student.index(score)+1)/len(student)*100
  if grade<=10: result="A+"
  elif 10<grade<=20: result="A0"
  elif 20<grade<=30: result="A-"
  elif 30<grade<=40: result="B+"
  elif 40<grade<=50: result="B0"
  elif 50<grade<=60: result="B-"
  elif 60<grade<=70: result="C+"
  elif 70<grade<=80: result="C0"
  elif 80<grade<=90: result="C-"
  else: result="D0"
  print("#"+str(i),result)
