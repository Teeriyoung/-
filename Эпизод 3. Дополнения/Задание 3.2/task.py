def task_1(list, find_this):
    for index in range(0, len(list)):
        if list[index] == find_this:
            return str(index)

def task_2(number):
    counter = 0
    for x in range(1, 10000):
        if number % x == 0:
            counter += 1
    if counter > 2:
        return False
    else:
        return True
