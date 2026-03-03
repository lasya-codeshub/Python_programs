
# Jumping Statements in Python
# break, continue, return

print("===== 1. Break Statement =====")
for i in range(1, 11):
    if i == 5:
        print("Break executed at", i)
        break
    print(i)

#continue:
for i in range(1, 11):
    if i == 5:
        print("Skipping", i)
        continue
    print(i)


#return

def check_number(num):
    if num % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

result = check_number(7)
print("Result:", result)
