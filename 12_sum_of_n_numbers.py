# 12_sum_of_n_numbers.py - by Aneesha Ali
# Sum of first N numbers

n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total = total + i

print(f"Sum of 1 to {n} is {total}")
