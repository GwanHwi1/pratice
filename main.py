from itertools import combinations

n,m=map(int,input().split())
nums=list(map(int,input().split()))
data=list(combinations(nums,3))
result=0
for i in data:
  a=sum(i)
  if a<=m:
    result=max(result,a)

print(result)