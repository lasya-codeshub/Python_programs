# Conditional Statements Demonstration Program

print("===== Simple if Statement =====")
num = 10
if num > 5:
    print("Number is greater than 5")

print("\n===== if - else Statement =====")
num = 4
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

print("\n===== if - elif - else Statement =====")
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

print("\n===== Nested if Statement =====")
age = 20
if age >= 18:
    if age >= 21:
        print("Eligible for voting and driving")
    else:
        print("Eligible for voting only")
else:
    print("Not eligible")

print("\n===== if Ladder Example =====")
number = 0
if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")
