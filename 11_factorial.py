# 11_factorial.py - by Aneesha Ali
# Find factorial of a number e.g. 5! = 120

num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print(f"Factorial of {num} is {fact}")
