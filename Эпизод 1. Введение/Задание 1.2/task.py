import math
# Пример 1
def task_1(a, b):
    # TODO
    if a > b:
        return (a * b) ** 0.5 - 3
    elif a < b:
        return math.log(a ** 3 + 1) / b
    else:
        return math.log10(2)


# Пример 2
def task_2(a, b):
    # TODO
    if a > b:
        return ((a * b - 5) ** 0.5) / a
    elif a < b:
        return math.tan(a / b) + 1
    else:
        return math.tan(-1)


# Пример 3
def task_3(a, b):
    # TODO
    if a > b:
        return math.log10(a * b) + 21
    elif a < b:
        return math.log(3 * a / b) + 1
    else:
        return math.tan(-5)


# Пример 4
def task_4(a, b):
    # TODO
    if a > b:
        return (a * b - 1) ** 0.5
    elif a < b:
        return math.tan(a - 5) / b
    else:
        return math.log10(255)


# Пример 5
def task_5(a, b):
    # TODO
    if a > b:
        return math.log(a / b) + 31
    elif a < b:
        return math.cos(a * 5 - 1) / a
    else:
        return math.tan(-25)


# Пример 6
def task_6(a, b):
    # TODO
    if a > b:
        return math.log10(a ** 3 - 5) / b
    elif a < b:
        return math.sqrt(b / a + 1)
    else:
        return 25 ** 0.5
