N = int(input("Enter the number of terms: "))

a, b = 0, 1
fibonacci = []

for _ in range(N):
    fibonacci.append(a)
    a, b = b, a + b

print(f"First {N} Fibonacci terms: {fibonacci}")