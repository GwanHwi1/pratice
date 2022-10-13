test_case=int(input())
for t in range(1,test_case+1):
  nums=list(input())
  minNums=int("".join(s for s in nums))
  maxNums=int("".join(s for s in nums))
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      nums[i],nums[j]=nums[j],nums[i]
      if nums[0]!='0':
        k=int("".join(s for s in nums))
        minNums=min(minNums,k)
        maxNums=max(maxNums,k)
      nums[i],nums[j]=nums[j],nums[i]
  print(f"#{t} {minNums} {maxNums}")

