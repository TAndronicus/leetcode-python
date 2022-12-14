NOMINALS = [1, 5, 10, 25]


def coins_recursive(amount_left, current_nominal):
    if amount_left == current_nominal == 1:
        return 1
    elif amount_left == 0:
        return 1
    times = 0
    for nominal in NOMINALS:
        if amount_left >= nominal and nominal <= current_nominal:
            times += coins_recursive(amount_left - nominal, nominal)
        else:
            break
    return times


def coins(amount):
    return coins_recursive(amount, NOMINALS[-1])


print(coins(4))
print(coins(5))
print(coins(6))
print(coins(25))
