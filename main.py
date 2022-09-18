def solution(arr):
  students=[]
  for i in arr:
    countA=i.count('A')
    countP=i.count('P')
    countL=i.count('L')
    score=10
    if countP+(countL//2)>=3:
      score=0
    else:
      score+=countA-(countL//2)-countP
    students.append(score)
  studentsGrade=students.copy()
  studentsGrade.sort(reverse=True)
  grade=[]
  for i in range(len(studentsGrade)):
    if i==0:
      grade.append(students.index(studentsGrade[i])+1)
    else:
      if studentsGrade[i]==studentsGrade[i-1]:
        grade.append(students.index(studentsGrade[i],students.index(studentsGrade[i])+1,len(students))+1)
      else: grade.append(students.index(studentsGrade[i])+1)
  return grade

a=list(map(str, input().split()))
print(solution(a))
