def number_print(num):
    if num > 5:
        return
    print(num)
    number_print(num + 1)


number_print(1)
