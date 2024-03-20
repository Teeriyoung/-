def task_1(N):
    # TODO
    answer = 1
    for x in range(1, N+1):
        answer = answer * x
    return answer



def task_2(N):
    # TODO
    i = 2
    prev = 0
    if (N == 1):
        return prev
    now = 1
    save = 0
    while i < N:
        save = now
        now = prev + now
        prev = save
        i += 1
    return now


def task_3(N):
    # TODO
    answer = []
    for x in range(1, N + 1):
        if N % x == 0:
            answer.append(x)
    return answer
