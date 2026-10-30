# Largest of All - Short Method - by Aneesha Ali
numbers = input("Enter numbers separated by space: ")
# Example: 5 20 3 99 12

num_list = [float(x) for x in numbers.split()]

largest = max(num_list)
print(f"Numbers are: {num_list}")
print(f"Largest is: {largest}")
