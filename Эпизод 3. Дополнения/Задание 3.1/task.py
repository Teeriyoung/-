def task_1(text):
    sentences = text.split('. ')
    last_point = sentences[-1].split('.')
    sentences[-1] = last_point[0]
    x = {sentence: 'none' for sentence in sentences}
    for sentence in sentences:
        words = sentence.split()
        x[sentence] = len(words)
    return x

def task_2(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
