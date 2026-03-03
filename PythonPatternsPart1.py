#PRINTING  PATTERNS

n=int(input())
b=ord('a')
for row in range(1,n+1):
  for col in range(1,n+1):
    print(chr(b),end=" ")
  b+=1
  print()

OUTPUT:
5
a a a a a 
b b b b b 
c c c c c 
d d d d d 
e e e e e 

# HALLOW PATTERN
n=int(input())
for row in range(0,n):
  b=ord('a')
  for col in range(0,n):
    if(col==0 or col==n-1 or row==0 or row==n-1):
     print(chr(b),end=" ")
    else:
       print(" ",end=" ")
    b+=1
  print()

OUTPUT:
5
a b c d e 
a       e 
a       e 
a       e 
a b c d e 

#right angle triangle

n=int(input())
for row in range(1,n+1):
  for space in range(1,n-row+1):
    print("",end="")
  b=ord('a')
  for col in range(1,row+1):
    print(chr(b),end=" ")
    b+=1
  print()
  
OUTPUT:

5
a 
a b 
a b c 
a b c d 
a b c d e 

#HALLOW PATTERN
n=int(input())
for row in range(1,n+1):
  num=0
  for space in range(1,n-row+1):
    print("",end="")
  for col in range(1,row+1):
    if(col==1 or row==n or col==row):
      print(num,end=" ")
    else:
      print(" ",end=" ")
    num+=1
  print()

OUTPUT:
5
0 
0 1 
0   2 
0     3 
0 1 2 3 4 








