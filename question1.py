num = int(input("Enter a three digit number: "))

sum_of_cubes = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_cubes += digit ** 3
    temp //= 10

if sum_of_cubes == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
