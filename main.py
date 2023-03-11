rows = int(input("Enter the number of rows"))
columns = int(input("Enter the number of columns"))

matrix = []

for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input(f"Enter value for {i + 1, j + 1}"))
        row.append(value)
    matrix.append(row)

for i in matrix:
    print(i)
    