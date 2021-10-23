def pattern_1(num):
    if num == 0:
        return
    print('* ' * num)
    pattern_1(num-1)


def pattern_2(num):
    if num == 0:
        return
    pattern_2(num-1)
    print('* ' * num)


pattern_1(4)
pattern_2(4)
