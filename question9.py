def matrix_sum(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

# Input two 3x3 matrices
A = [[int(input(f"A[{i+1}][{j+1}]: ")) for j in range(3)] for i in range(3)]
B = [[int(input(f"B[{i+1}][{j+1}]: ")) for j in range(3)] for i in range(3)]

sum_matrix = matrix_sum(A, B)

print("Sum of matrices:")
for row in sum_matrix:
    print(row)