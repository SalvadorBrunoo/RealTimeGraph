def update(signal:list):

    new_signal = []

    a = 1.0
    b = 0

    for x in signal:
        x = x // 1000 / 100
        y = x*a + b
        new_signal += [y]

    return new_signal
