rows = int(input("Enter the number of rows"))
columns = int(input("Enter the number of columns"))

matrix = [[int(input(f"Enter {i+1}, {j + 1} element:")) for j in range(columns)] for i in range(rows)]

for i in matrix:
    print(i)
    