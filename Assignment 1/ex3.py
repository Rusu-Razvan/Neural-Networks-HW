import ex1,ex2
import pathlib

def solve_cramer(matrix: list[list[float]], vector: list[float]) -> list[float]:
    det = ex2.determinant(matrix)
    if det == 0:
        return None  

    def replace_column(mat: list[list[float]], col_index: int, new_col: list[float]) -> list[list[float]]:
        new_mat = [row[:] for row in mat] 
        for i in range(len(new_mat)):
            new_mat[i][col_index] = new_col[i]
        return new_mat

    solutions = []
    for i in range(len(matrix)):
        modified_matrix = replace_column(matrix, i, vector)
        det_i = ex2.determinant(modified_matrix)
        solutions.append(det_i / det)

    return solutions


if __name__ == "__main__":
    A, B = ex1.read_system(pathlib.Path('system.txt'))

    solution = solve_cramer(A, B)
    if solution is None:
        print("The system has no unique solution.")
    else:
        print(f"Solution: {solution}")
