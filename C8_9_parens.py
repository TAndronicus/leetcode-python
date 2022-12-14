def parens_recursive(current, left_to_open):
    if current == 1 and left_to_open == 0:
        return [')']
    else:
        res = []
        if left_to_open > 0:
            for remainder in parens_recursive(current + 1, left_to_open - 1):
                res.append('(' + remainder)
        if current > 0:
            for remainder in parens_recursive(current - 1, left_to_open):
                res.append(')' + remainder)
        return res


def parens(n):
    return list(parens_recursive(0, n))


print(', '.join(parens(3)))
print(', '.join(parens(4)))
