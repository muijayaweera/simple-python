def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Input list of numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Filter prime numbers
primes = [n for n in numbers if is_prime(n)]

print(f"Prime numbers: {primes}")