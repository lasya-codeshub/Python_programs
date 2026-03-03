#DIAMOND PATTERN

n=int(input())
for row in range(1,n):
  for space in range(1,n-row+1):
    print(" ",end=" ")
  b=ord('a')
  for col in range(1,row+1):
    print(chr(b),end=" ")
    b+=1
  b=ord('a')
  for col in range(1,row):
    print(chr(b),end=" ")
    b+=1
  print()
for row in range(n,0,-1):
  for space in range(1,n-row+1):
    print(" ",end=" ")
  b=ord('a')
  for col in range(1,row+1):
    print(chr(b),end=" ")
    b+=1
  b=ord('a')
  for col in range(1,row):
    print(chr(b),end=" ")
    b+=1
  print()

OUTPUT:
5
        a 
      a b a 
    a b c a b 
  a b c d a b c 
a b c d e a b c d 
  a b c d a b c 
    a b c a b 
      a b a 
        a 

# butterfly

n=int(input())
for row in range(1,n):
  for space in range(1,n-row+1):
    print("",end="")
  b=ord('a')
  for col in range(1,row+1):
    print(chr(b),end=" ")
    b+=1
  for space in range(1,(2*n)-row*2+1):
    print(" ",end=" ")
  b=ord('a')
  for col in range(1,row+1):
    print(chr(b),end=" ")
    b+=1
  print()
for row in range(n,0,-1):
  for space in range(1,n-row+1):
    print("",end="")
  b=ord('a')
  for col in range(1,row+1):
    print(chr(b),end=" ")
    b+=1
  for space in range(1,(2*n)-row*2+1):
    print(" ",end=" ")
  b=ord('a')
  for col in range(1,row+1):
    print(chr(b),end=" ")
    b+=1
  print()
  
  OUTPUT:

5
a                 a 
a b             a b 
a b c         a b c 
a b c d     a b c d 
a b c d e a b c d e 
a b c d     a b c d 
a b c         a b c 
a b             a b 
a                 a 

  


