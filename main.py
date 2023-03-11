rows = int(input("Enter the number of rows"))
columns = int(input("Enter the number of columns"))

matrix_A = [[int(input(f"Enter {i+1}, {j + 1} element:")) for j in range(columns)] for i in range(rows)]

matrix_B = [[int(input(f"Enter {i+1}, {j + 1} element:")) for j in range(columns)] for i in range(rows)]  

print()

print('Matrix-A :')
for i in matrix_A:
    print(i)

print()

print('Matrix-B :')
for i in matrix_B:
    print(i)

result = [[0 for j in range(columns)] for i in range(rows)]

for i in range(rows):
    for j in range(columns):
        result[i][j] = matrix_A[i][j] + matrix_B[i][j]

print()
print('Addition of Matrix-A and Matrix-B is :')

for i in result:
    print(i)

for i in range(rows):
    for j in range(columns):
        result[i][j] = matrix_A[i][j] - matrix_B[i][j]

print()

print('Subtraction of Matrix-A and Matrix-B is :')
for i in result:
    print(i)

    