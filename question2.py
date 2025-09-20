numbers = []
for i in range(5):
    n = int(input(f"Enter number {i+1}: "))
    numbers.append(n)

largest = max(numbers)
smallest = min(numbers)

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")