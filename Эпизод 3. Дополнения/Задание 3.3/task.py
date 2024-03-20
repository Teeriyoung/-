def sost_spiska(list):
    numer = set(list)
    number = {n: 0 for n in numer}
    for x in list:
        for nuznoe_x in numer:
            if x == nuznoe_x:
                number[nuznoe_x] += 1
    return number

def poisk_chastogo(number, list):
    answer = [0, 0]
    numer = set(list)
    for i in numer:
        if number[i] > answer[1]:
            answer[0] = i
            answer[1] = number[i]
    return answer[0]


def task_1(list):
    return poisk_chastogo(sost_spiska(list), list)


def task_2(x, y):
    check = True
    for i in range(8):
        for j in range(i + 1, 8):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                check = False
    if check:
        return 'NO'
    else:
        return 'YES'


def task_3(x, y, xc, yc, r):
    return ((x - xc) ** 2 + (y - yc) ** 2) ** 0.5 <= r


def task_4(number):
    schetchik = 0
    for i in range(1, len(number)-1):
        if number[i] > number[i-1] and number[i] > number[i+1]:
            schetchik += 1
            i += 1
    return schetchik


def task_5(shifr_key):
    text = (open('file.txt', 'r').read().lower()).split('\n')
    alphavit = ''.join([chr(i) for i in range(97, 123)])
    for i in range(len(text)):
        sentence = [a for a in text[i]]
        for j in range(len(sentence)):
            place = alphavit.find(sentence[j])
            new_place = place + shifr_key
            sentence[j] = alphavit[new_place]
        text[i] = ''.join(sentence)
    del text[3]
    return text