def partition(list, mask):
    left, right = [], []
    index = 1
    for el in list:
        if index & mask:
            right.append(el)
        else:
            left.append(el)
        index <<= 1
    return generate_permutations_recursive(left), generate_permutations_recursive(right)


def generate_permutations_recursive(chars):
    if len(chars) == 0:
        return ['']
    if len(chars) == 1:
        return chars
    else:
        ch, res = chars.pop(), []
        for i in range(0, 1 << len(chars)):
            left_part, right_part = partition(chars, i)
            for left in left_part:
                for right in right_part:
                    res.append(left + ch + right)
        return res


def generate_permutations(s):
    return generate_permutations_recursive(list(s))


print(generate_permutations("abc"))
print(len(generate_permutations("abcd")))
