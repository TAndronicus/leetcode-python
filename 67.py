class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = max(len(a), len(b))
        res = [''] * length
        a, b, carry = list(reversed(a)), list(reversed(b)), False
        for i in range(length):
            sum = [0, 1][carry]
            if i < len(a):
                sum += int(a[i])
            if i < len(b):
                sum += int(b[i])
            if sum > 1:
                carry = True
            else:
                carry = False
            res[i] = str(sum % 2)
        if carry:
            res.append('1')
        return ''.join(reversed(res))

    def addBinary2(self, a: str, b: str) -> str:
        return "{0:b}".format(int(a, 2) + int(b, 2))


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary('101', '010') == '111')
    print(s.addBinary('11', '1') == '100')
    print(s.addBinary('11', '11') == '110')
    print(s.addBinary('1', '1') == '10')
    print(s.addBinary('0', '0') == '0')
    print(s.addBinary('1010', '1011') == '10101')
    print(s.addBinary2('101', '010') == '111')
    print(s.addBinary2('11', '1') == '100')
    print(s.addBinary2('11', '11') == '110')
    print(s.addBinary2('1', '1') == '10')
    print(s.addBinary2('0', '0') == '0')
    print(s.addBinary2('1010', '1011') == '10101')
