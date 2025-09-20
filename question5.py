numbers = input("Enter numbers separated by space: ").split()
numbers = [int(n) for n in numbers]

# Remove duplicates using set and sort
unique_numbers = sorted(set(numbers))

print(f"List after removing duplicates and sorting: {unique_numbers}")