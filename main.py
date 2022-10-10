def bigger(arr,result,n):
  if n>=len(arr): return result
  for i in range(len(arr)):
    if i!=n:
      if arr[n][0] > arr[i][0] and arr[n][1] > arr[i][1]:
        result[n][0]+=1
      elif arr[n][0] >=arr[i][0] and arr[n][1] <= arr[i][1]:
        result[n][1]+=1
      elif arr[n][0] <= arr[i][0] and arr[n][1] >= arr[i][1]:
        result[n][1]+=1
  bigger(arr,result,n+1)

n=int(input())
result=[[0,0]for _ in range(n)]
lst=[list(map(int, input().split()))for _ in range(n)]
bigger(lst,result,0)
result1=[]
for i in range(len(result)):
  result1.append(n-sum(result[i]))
print(' '.join(str(e) for e in result1))

