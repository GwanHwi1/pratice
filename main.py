t=int(input())
for i in range(1,t+1):
  n=int(input())
  arr=[]
  string=""
  for j in range(n):
    arr1=[]
    for k in range(n):
      if k==0:
        arr1.append(1)
        string+=str(1)+" "
      elif k<=j:
        arr1.append(arr[j-1][k-1]+arr[j-1][k])
        string+=str(arr[j-1][k-1]+arr[j-1][k])+" "
      else: arr1.append(0)
    string+="\n"  
    arr.append(arr1)
  print("#"+str(i))
  print(string[:len(string)-1])