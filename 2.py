def matrix_print(mx, title=None):
    if title:
        print(title)
    n = len(mx)
    print("𐌲" + "        " * n + "ㄱ")
    for i in range(n):
        print("|", end=" ")
        for j in range(n):
            print("%7d" % (1 if mx[i][j] else 0), end=" ")
        print("|")
    print("ㄴ" + "        " * n + "┘")

def is_reflexive(matrix) :
    for i in range(5) :
        if matrix[i][i] != 1 :
            return False
    return True

def is_symmetric(matrix) :
    for i in range(5) :
        for j in range(5) :
            if matrix[i][j] != matrix[j][i] :
                return False
    return True

def is_transitive(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                for k in range(n):
                    if matrix[j][k] and not matrix[i][k]:
                        return False
    return True


def reflexive_closure(matrix, verbose = True) :
    added = []
    for i in range(5) :
        if matrix[i][i] == 0 :
            matrix[i][i] = 1
            added.append((i, i))
    if verbose and added :
        print("반사적 폐포 추가:", [(i+1, j+1) for i, j in added])
    return matrix

def symmetric_closure(matrix, verbose = True) :
    added = []
    for i in range(5) :
        for j in range(5) :
            if matrix[i][j] == 1 and matrix[j][i] == 0 :
                matrix[j][i] = 1
                added.append((j, i))
    if verbose and added:
        print("대칭적 폐포 추가:", [(i+1, j+1) for i, j in added])
    return matrix

def transitive_closure(matrix, verbose=True):
    n = len(matrix)
    added = []
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] and matrix[k][j] and matrix[i][j] == 0:
                    matrix[i][j] = 1
                    added.append((i, j))
    if verbose and added:
        print("추이적 폐포 추가:", [(i+1, j+1) for i, j in added])
    return matrix

def equivalence_classes(matrix):
    classes = []
    for i in range(5) :
        cls = [j for j in range(5) if matrix[i][j] == 1]
        print(f"{i+1}의 동치류 → {{{', '.join(str(x+1) for x in cls)}}}")
        classes.append(cls)
    print()
    return classes

def read_matrix(n) :
    matrix = []
    for _ in range(n) :
        row = list(map(int, input().split()))
        matrix.append([1 if x else 0 for x in row])
    return matrix

def main():
    print("5x5 관계행렬을 행 단위로 입력하세요:")
    matrix = read_matrix(5)

    matrix_print(matrix, "입력된 관계행렬:")

    r = is_reflexive(matrix)
    s = is_symmetric(matrix)
    t = is_transitive(matrix)

    print(f"반사적: {r}")
    print(f"대칭적: {s}")
    print(f"추이적: {t}")

    if r and s and t : 
        print("\n이 관계는 동치관계입니다.")
        equivalence_classes(matrix)
        return

    print("\n이 관계는 동치관계가 아닙니다. 폐포를 적용합니다.")

    if not r:
        before = [row[:] for row in matrix]
        matrix_print(before, "\n반사적 폐포 적용 전:")
        reflexive_closure(matrix, verbose=True)
        matrix_print(matrix, "반사적 폐포 적용 후:")

    if not s:
        before = [row[:] for row in matrix]
        matrix_print(before, "\n대칭적 폐포 적용 전:")
        symmetric_closure(matrix,  verbose=True)
        matrix_print(matrix, "대칭적 폐포 적용 후:")

    if not t:
        before = [row[:] for row in matrix]
        matrix_print(before, "\n추이적 폐포 적용 전:")
        transitive_closure(matrix, verbose=True)
        matrix_print(matrix, "추이적 폐포 적용 후:")

    print("\n폐포 적용 후 다시 판별:")
    r2, s2, t2 = is_reflexive(matrix), is_symmetric(matrix), is_transitive(matrix)
    print(f"반사적: {r2}")
    print(f"대칭적: {s2}")
    print(f"추이적: {t2}")

    if r2 and s2 and t2 :
        print("\n이제 동치관계가 되었습니다.")
        equivalence_classes(matrix)
    else:
        print("\n폐포를 적용해도 동치관계가 아닙니다.")

if __name__ == "__main__":
    main()

