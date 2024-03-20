# Пример 1
def task_1(n):
    # TODO
    x = 0
    i = 1
    while i <= 10:
        x = x + 1 / i
        i = i + 1
    return x


# Пример 2
def task_2(x, n):
    # TODO
    y = 0
    i = 1
    while i <= 17:
        y = y + x / i
        i = i + 2
    return y


# Пример 3
def task_3(n):
    # TODO
    y = 1
    i = 1
    while i <= n:
        y = y * i
        i = i + 1
    return y


# Пример 4
def task_4(x, n):
    # TODO
    z = 1
    i = 2
    while i <= 9:
        z = z * ((x + i) / i)
        i = i + 1
    return z


# Пример 5
def task_5(x, n):
    # TODO
    y = 1
    i = 1
    while i <= 9:
        y = y + ((x * i) / (2 * i))
        i = i + 1
    return y - 4


# Пример 6
def task_6(n):
    # TODO
    z = 1
    i = 2
    while i <= 20:
        z = z * i
        i = i + 2
    return z
