from ex1 import read_system

def determinant(matrix: list[list[float]]) -> float:
    n = len(matrix)
    if n == 0:
        return 1.0  
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    if n == 3:
     det = (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )
    return det

def trace(matrix: list[list[float]]) -> float:
    return sum(matrix[i][i] for i in range(len(matrix)))

def norm(vector: list[float]) -> float:
    return sum(x**2 for x in vector) ** 0.5

def transpose(matrix: list[list[float]]) -> list[list[float]]:
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def multiply(matrix: list[list[float]], vector: list[float]) -> list[float]:
    result = []
    for row in matrix:
        result.append(sum(row[i] * vector[i] for i in range(len(vector))))
    return result

if __name__ == "__main__":
    A, B = read_system('system.txt')

    print(f"A: {A}")
    print(f"B: {B}")
    print(f"Determinant(A): {determinant(A)}")
    print(f"Trace(A): {trace(A)}")
    print(f"Norm(B): {norm(B)}")
    print(f"Transpose(A): {transpose(A)}")
    print(f"Multiply(A, B): {multiply(A, B)}")
