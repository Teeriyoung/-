# Пример 1
def task_1(A):
    x = 0
    for i in range(0, len(A)):
        if A[i] > 0:
            x += A[i]
    return x


# Пример 2
def task_2(A):
    x = sum(A) / len(A)
    return x


# Пример 3
def task_3(A):
    srznach = sum(A) / len(A)
    sqdev = []
    for i in range(0, len(A)):
        sqdev.append((A[i] - srznach) ** 2)
    return (sum(sqdev) / len(sqdev)) ** 0.5
