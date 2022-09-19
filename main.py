t=int(input())

def binaryN(num):#이진수 만들기 함수
  res=bin(num)
  result=res[2:]
  while(len(result)<6):
    result="0"+result    
  return result

data=dict() #encoding표 
for i in range(26): data[chr(65+i)]=binaryN(i)
for i in range(26): data[chr(97+i)]=binaryN(i+26)
for i in range(10): data[chr(48+i)]=binaryN(i+52)
data['+']=binaryN(62)
data['/']=binaryN(63)

for test in range(1,t+1): #decoding
  a=input()
  string=""
  result=""
  for i in range(len(a)):
    string+=data[a[i]]
  for i in range(0,len(string)-8,8):
    con="0b"+string[i:i+8]
    decimal=int(con,2)
    result+=chr(decimal)

  if (len(string)%8)!=0:
    con="0b"+string[len(string)-8:]
    decimal=int(con,2)
    result+=chr(decimal)
  print("#"+str(test),result+'.')