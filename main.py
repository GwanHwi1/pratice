for _ in range(1,11):
  t=int(input())
  check=input()
  s=input()
  cnt=0
  for i in range(len(s)):
    if s[i:i+len(check)]==check: cnt+=1
  print(f"#{t} {cnt}")