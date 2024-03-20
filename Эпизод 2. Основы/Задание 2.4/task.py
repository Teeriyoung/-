def task_1(str):
    # TODO
    text = str
    alphavit = [chr(i) for i in range(97, 123)]
    x = {letter: 0 for letter in alphavit if letter in text}
    for text_letter in text:
        for letter in alphavit:
            if text_letter == letter:
                x[letter] += 1
    return x


def task_2(list):
    list = set(list)
    return sum(list)


def task_3(cities):
    return ', '.join(cities) + '.'

def task_4(a, b):
    a = set(a)
    b = set(b)
    x = [i for i in a & b]
    return x
