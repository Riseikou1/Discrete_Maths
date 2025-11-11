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

def copy_matrix(M):
    return [row[:] for row in M]

def is_reflexive(M):
    n = len(M)
    for i in range(n):
        if M[i][i] != 1:
            return False
    return True

def is_symmetric(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            if M[i][j] != M[j][i]:
                return False
    return True

def is_transitive(M):
    n = len(M)
    T = copy_matrix(M)
    for k in range(n):
        for i in range(n):
            if T[i][k]:
                for j in range(n):
                    if T[k][j]:
                        T[i][j] = 1
    for i in range(n):
        for j in range(n):
            if T[i][j] and not M[i][j]:
                return False
    return True

def reflexive_closure(M, verbose=True):
    n = len(M)
    added = []
    for i in range(n):
        if M[i][i] == 0:
            M[i][i] = 1
            added.append((i, i))
    if verbose and added:
        print("반사적 폐포 추가:", [(i+1, j+1) for i, j in added])
    return M

def symmetric_closure(M, verbose=True):
    n = len(M)
    added = []
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1 and M[j][i] == 0:
                M[j][i] = 1
                added.append((j, i))
    if verbose and added:
        print("대칭적 폐포 추가:", [(i+1, j+1) for i, j in added])
    return M

def transitive_closure(M, verbose=True):
    n = len(M)
    added = []
    for k in range(n):
        for i in range(n):
            if M[i][k]:
                for j in range(n):
                    if M[k][j] and M[i][j] == 0:
                        M[i][j] = 1
                        added.append((i, j))
    if verbose and added:
        print("추이적 폐포 추가:", [(i+1, j+1) for i, j in added])
    return M

def is_equivalence(M):
    return is_reflexive(M) and is_symmetric(M) and is_transitive(M)

def equivalence_classes(M):
    n = len(M)
    classes = []
    seen = set()
    for i in range(n):
        if i in seen:
            continue
        cls = [j for j in range(n) if M[i][j] == 1]
        for j in cls:
            seen.add(j)
        classes.append(sorted(cls))
    return [[x+1 for x in group] for group in classes]

def read_matrix(n=5):
    M = []
    for _ in range(n):
        row = list(map(int, input().split()))
        M.append([1 if x else 0 for x in row])
    return M

def main():
    print("5x5 관계행렬을 행 단위로 입력하세요:")
    M = read_matrix(5)

    matrix_print(M, "입력된 관계행렬:")

    r = is_reflexive(M)
    s = is_symmetric(M)
    t = is_transitive(M)

    print(f"반사적: {r}")
    print(f"대칭적: {s}")
    print(f"추이적: {t}")

    if is_equivalence(M):
        print("\n이 관계는 동치관계입니다.")
        classes = equivalence_classes(M)
        print("동치류:")
        for idx, cls in enumerate(classes, 1):
            print(f"동치류 {idx}: {cls}")
        return

    print("\n이 관계는 동치관계가 아닙니다. 폐포를 적용합니다.")

    if not r:
        before = copy_matrix(M)
        matrix_print(before, "\n반사적 폐포 적용 전:")
        reflexive_closure(M, verbose=True)
        matrix_print(M, "반사적 폐포 적용 후:")

    if not s:
        before = copy_matrix(M)
        matrix_print(before, "\n대칭적 폐포 적용 전:")
        symmetric_closure(M, verbose=True)
        matrix_print(M, "대칭적 폐포 적용 후:")

    if not t:
        before = copy_matrix(M)
        matrix_print(before, "\n추이적 폐포 적용 전:")
        transitive_closure(M, verbose=True)
        matrix_print(M, "추이적 폐포 적용 후:")

    print("\n폐포 적용 후 다시 판별:")
    r2, s2, t2 = is_reflexive(M), is_symmetric(M), is_transitive(M)
    print(f"반사적: {r2}")
    print(f"대칭적: {s2}")
    print(f"추이적: {t2}")

    if is_equivalence(M):
        print("\n이제 동치관계가 되었습니다.")
        classes = equivalence_classes(M)
        print("동치류:")
        for idx, cls in enumerate(classes, 1):
            print(f"동치류 {idx}: {cls}")
    else:
        print("\n폐포를 적용해도 동치관계가 아닙니다.")

if __name__ == "__main__":
    main()
