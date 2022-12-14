class Solution:
    def isDecimal(self, s):
        if len(s) == 0:
            return False
        counter = 0
        if s[counter] == '-' or s[counter] == '+':
            counter += 1
        if len(s) == counter or (len(s) == counter + 1 and s[counter] == '.'):
            return False
        hadDot = False
        while counter < len(s):
            if s[counter] == '.' and not hadDot:
                hadDot = True
                counter += 1
                continue
            elif s[counter].isdigit():
                counter += 1
                continue
            return False
        return True

    def isInteger(self, s):
        if len(s) == 0:
            return False
        counter = 0
        if s[counter] == '-' or s[counter] == '+':
            counter += 1
        if len(s) == counter:
            return False
        while counter < len(s):
            if s[counter].isdigit():
                counter += 1
                continue
            return False
        return True

    def isNumber(self, s: str) -> bool:
        parts = s.lower().split('e')
        if len(parts) == 1:
            return self.isDecimal(parts[0]) or self.isInteger(parts[0])
        elif len(parts) == 2:
            return (self.isDecimal(parts[0]) or self.isInteger(parts[0])) and self.isInteger(parts[1])
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(not s.isNumber('e'))
    print(not s.isNumber('e-'))
    print(not s.isNumber('e+'))
    print(not s.isNumber('ee'))
    print(not s.isNumber('e-1'))
    print(s.isNumber('1e-1'))
    print(not s.isNumber('e1'))
    print(s.isNumber('1e1'))
    print(not s.isNumber('+'))
    print(not s.isNumber('-'))
    print(not s.isNumber('-.'))
    print(not s.isNumber('.'))
    print(s.isNumber('.1'))
    print(not s.isNumber('.1.'))
    print(s.isNumber('1.1'))
    print(s.isNumber('-1.1'))
    print(not s.isNumber('-1.1.'))

    print(s.isNumber('2'))
    print(s.isNumber('0089'))
    print(s.isNumber('-0.1'))
    print(s.isNumber('+3.14'))
    print(s.isNumber('4.'))
    print(s.isNumber('-.9'))
    print(s.isNumber('2e10'))
    print(s.isNumber('-90E3'))
    print(s.isNumber('3e+7'))
    print(s.isNumber('+6e-1'))
    print(s.isNumber('53.5e93'))
    print(s.isNumber('-123.456e789'))

    print(not s.isNumber('abc'))
    print(not s.isNumber('1a'))
    print(not s.isNumber('1e'))
    print(not s.isNumber('e3'))
    print(not s.isNumber('99e2.5'))
    print(not s.isNumber('--6'))
    print(not s.isNumber('-+3'))
    print(not s.isNumber('95a54e53'))
