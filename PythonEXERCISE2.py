# Looping Exercises Programs

# 1️⃣ Multiplication Table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 2️⃣ Sum of N Natural Numbers
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum is:", total)

# 3️⃣ Reverse a Number
num = int(input("Enter a number: "))
reverse = 0
temp = num
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
print("Reversed number is:", reverse)

# 4️⃣ Palindrome Number
num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

# 5️⃣ Armstrong Number
num = int(input("Enter a number: "))
order = len(str(num))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")

# 6️⃣ Factors of a Number
num = int(input("Enter a number: "))
print("Factors are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)

# 7️⃣ Fibonacci Series
n = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# 8️⃣ Perfect, Abundant or Deficient Number
num = int(input("Enter a number: "))
sum_of_divisors = 0

for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i

if sum_of_divisors == num:
    print("Perfect Number")
elif sum_of_divisors > num:
    print("Abundant Number")
else:
    print("Deficient Number")
