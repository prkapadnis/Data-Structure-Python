brackets = "[[[[][]]]]"


def check_balance(brackets):
    open = 0
    close = 0
    for i in brackets:
        if '[' == i:
            open += 1
        else:
            close += 1
    if open == close:
        print(True)
    else:
        print(False)


def check_balance_1(brackets):
    check = 0
    for i in brackets:
        if i == '[':
            check += 1
        elif i == ']':
            check -= 1

        if check < 0:
            break
    return check == 0


print(check_balance_1(brackets))
