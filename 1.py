EPS = 1e-12

def printMatrix(mx):
    n = len(mx)
    print("𐌲" + "        " * n + "ㄱ")
    for i in range(n):
        print("|", end=" ")
        for j in range(n):
            print("%7.3f" % mx[i][j], end=" ")
        print("|")
    print("ㄴ" + "        " * n + "┘")

def getTransposeMatrix(matrix):
    n = len(matrix)
    return [[matrix[j][i] for j in range(n)] for i in range(n)]

def getMinorMatrix(matrix, r, c):
    return [row[:c] + row[c + 1:] for row in (matrix[:r] + matrix[r + 1:])]

def getMatrixDeterminant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0.0
    for c in range(n):
        det += (-1.0 if (c & 1) else 1.0) * matrix[0][c] * getMatrixDeterminant(getMinorMatrix(matrix, 0, c))
    return det

def has_inverse(matrix):
    det = getMatrixDeterminant(matrix)
    if abs(det) < EPS:
        return False
    return True

def inverse_by_determinant(m):
    n = len(m)
    det = getMatrixDeterminant(m)
    if n == 1:
        return [[1.0 / m[0][0]]]
    if n == 2:
        return [[ m[1][1] / det, -m[0][1] / det],
                [-m[1][0] / det,  m[0][0] / det]]
    cof = []
    for r in range(n):
        row = []
        for c in range(n):
            minor = getMinorMatrix(m, r, c)
            row.append((-1.0 if ((r + c) & 1) else 1.0)* getMatrixDeterminant(minor))
        cof.append(row)
    adj = getTransposeMatrix(cof)
    for i in range(n):
        for j in range(n):
            adj[i][j] /= det
    return adj

def inverse_by_gauss_jordan(a):
    n = len(a)
    aug = [a[i][:] + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    for col in range(n):
        pivot_row = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot_row][col]) < EPS:
            raise ValueError("소거 과정 중 특이 행렬 발견 (피벗이 0).")
        if pivot_row != col:
            aug[col], aug[pivot_row] = aug[pivot_row], aug[col]

        pivot = aug[col][col]
        for j in range(2 * n):
            aug[col][j] /= pivot

        for r in range(n):
            if r == col:
                continue
            factor = aug[r][col]
            if abs(factor) > 0:
                for j in range(2 * n):
                    aug[r][j] -= factor * aug[col][j]

    inv = [row[n:] for row in aug]
    return inv

def are_same(m1, m2, tol=1e-6):
    n = len(m1)
    for i in range(n):
        for j in range(n):
            if abs(m1[i][j] - m2[i][j]) > tol:
                return False
    return True

def read_square_matrix():
    k = int(input("정방행렬의 차수를 입력하세요: "))
    if k <= 0:
        raise ValueError("차수는 양수여야 합니다.")
    matrix = []
    for i in range(k):
        while True:
            row_input = input(f"{i + 1}행 입력: ")
            try:
                vals = [float(x) for x in row_input.split()]
                if len(vals) != k:
                    print(f"{k}개의 실수를 공백으로 구분해 입력하세요.")
                    continue
                matrix.append(vals)
                break
            except ValueError:
                print("숫자만 입력하세요.")
    return matrix

def main():
    try:
        A = read_square_matrix()
        if not has_inverse(A) :
            print("오류! 행렬식이 0이므로 역행렬을 구할 수 없습니다.")
            return 

        print("\n[가우스-조던 소거법으로 구한 역행렬] : \n")
        inv_gj = inverse_by_gauss_jordan(A)
        printMatrix(inv_gj)

        print("\n[행렬식으로 구한 역행렬] : \n")
        inv_det = inverse_by_determinant(A)
        printMatrix(inv_det)

        if are_same(inv_gj, inv_det) :
            print("두 방법의 결과가 동일합니다.")
        else:
            print("두 방법의 결과가 다릅니다.")

    except ValueError as e:
        print(f"입력/계산 오류: {e}")

if __name__ == "__main__":
    main()
