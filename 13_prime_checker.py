# 13_prime_checker.py - by Aneesha Ali
# Check Prime Number

num = int(input("Enter a number: "))

if num <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num} is Prime")
    else:
        print(f"{num} is NOT Prime")
