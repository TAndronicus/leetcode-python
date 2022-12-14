def move_disks(n):
    s1, s2, s3 = [i for i in range(n, 0, -1)], [], []

    def move_disks_recursive(s1, s2, s3, num):
        if num == 1:
            s2.append(s1.pop())
        else:
            move_disks_recursive(s1, s3, s2, num - 1)
            s2.append(s1.pop())
            move_disks_recursive(s3, s2, s1, num - 1)

    move_disks_recursive(s1, s2, s3, n)
    print(f's1: {", ".join([str(el) for el in s1])}, s2: {", ".join([str(el) for el in s2])}, s3: {", ".join([str(el) for el in s3])}')


move_disks(5)
