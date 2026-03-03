#reverse right angle

n=int(input())
for row in range(1,n+1):
  for space in range(1,n-row+1):
    print(" ",end=" ")
  num=0
  for col in range(1,row+1):
    print(num,end=" ")
    num+=1
  print()

OUTPUT:
5
        0 
      0 1 
    0 1 2 
  0 1 2 3 
0 1 2 3 4 

#reverse hallow

n=int(input())
for row in range(1,n+1):
  num=0
  for space in range(1,n-row+1):
    print(" ",end=" ")
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

#inverse right angle traingle

n=int(input())
for row in range(n,0,-1):#reversing the limits
  for space in range(1,n-row+1):
    print("",end="")
  b=ord('a')
  for col in range(1,row+1):
    print(chr(b),end=" ")
    b+=1
  print()

OUTPUT:
5
a b c d e 
a b c d 
a b c 
a b 
a 

#inverse right angle traingle reverse

n=int(input())
for row in range(n,0,-1):#reversing the limits
  for space in range(1,n-row+1):
    print(" ",end=" ")#
  b=ord('a')
  for col in range(1,row+1):
    print(chr(b),end=" ")
    b+=1
  print()
OUTPUT:

5
a b c d e 
  a b c d 
    a b c 
      a b 
        a 

#hallow inverse right angle triangle

n=int(input())
for row in range(n,0,-1):
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
0 1 2 3 4 
0     3 
0   2 
0 1 
0 
# inverse reverse hallow

n=int(input())
for row in range(n,0,-1):
  num=0
  for space in range(1,n-row+1):
    print(" ",end=" ")
  for col in range(1,row+1):
    if(col==1 or row==n or col==row):
      print(num,end=" ")
    else:
      print(" ",end=" ")
    num+=1
  print()

OUTPUT:
5
0 1 2 3 4 
  0     3 
    0   2 
      0 1 
        0 





