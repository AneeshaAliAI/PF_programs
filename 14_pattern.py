# 14_patterns.py - by Aneesha Ali - BS AI 1st Semester
# Patterns using nested loops

n = int(input("Enter number of rows: "))

print("\nPattern 1: Star Triangle")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

print("\nPattern 2: Number Triangle")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nPattern 3: Number Pyramid - Same Number")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()
