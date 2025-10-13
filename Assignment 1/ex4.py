import ex1,ex2
import pathlib

def minor(matrix: list[list[float]], i: int, j: int) -> list[list[float]]:
    return [row[:j] + row[j+1:] for k, row in enumerate(matrix) if k != i]

def cofactor(matrix: list[list[float]]) -> list[list[float]]:
    cof = []
    for i in range(len(matrix)):
        cof_row = []
        for j in range(len(matrix)):
            minor_ij = minor(matrix, i, j)
            det_minor = ex2.determinant(minor_ij)
            sign = (-1) ** (i + j)
            cof_row.append(sign * det_minor)
        cof.append(cof_row)
    return cof

def adjoint(matrix: list[list[float]]) -> list[list[float]]:
    return ex2.transpose(cofactor(matrix))

def solve(matrix: list[list[float]], vector: list[float]) -> list[float]:
    det = ex2.determinant(matrix)
    if det == 0:
        return None  

    adj = adjoint(matrix)
    inv = [[adj[i][j] / det for j in range(len(adj))] for i in range(len(adj))]

    return ex2.multiply(inv, vector)

if __name__ == "__main__":
    A, B = ex1.read_system(pathlib.Path('system.txt'))

    solution = solve(A, B)
    if solution is None:
        print("The system has no unique solution.")
    else:
        print(f"Solution: {solution}")
