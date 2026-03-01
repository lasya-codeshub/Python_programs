# Python Operators Demonstration Program
a = 10
b = 3
print(" Arithmetic Operators")
print("addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("Floor Division:", a // b)

print("\n Comparison Operators ")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\nLogical Operators")
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

print("\n Assignment Operators ")
c = 5
c += 2
print("c += 2:", c)
c *= 3
print("c *= 3:", c)
c -= 4
print("c -= 4:", c)

print("\n Bitwise Operators ")
print("a & b:", a & b)      # AND
print("a | b:", a | b)      # OR
print("a ^ b:", a ^ b)      # XOR
print("~a:", ~a)            # NOT
print("a << 1:", a << 1)    # Left shift
print("a >> 1:", a >> 1)    # Right shift

print("\n Membership Operators ")
my_list = [1, 2, 3, 4, 5]
print("3 in my_list:", 3 in my_list)
print("10 not in my_list:", 10 not in my_list)

print("\n Identity Operators")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is not list2:", list1 is not list2)

print("\n Ternary Operator ")
num = 15
result = "Even" if num % 2 == 0 else "Odd"
print("Number is:", result)
