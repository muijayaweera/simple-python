numbers = input("Enter numbers: ").split()
numbers = [int(n) for n in numbers]


unique_numbers = sorted(set(numbers))

print(f"List after removing duplicates and sorting: {unique_numbers}")