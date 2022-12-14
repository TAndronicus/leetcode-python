class Solution:
    def countTime(self, time: str) -> int:
        prod = 1
        if time[0] == '?':
            if time[1] == '?':
                prod = 24
            elif int(time[1]) < 4:
                prod = 3
            else:
                prod = 2
        elif time[1] == '?':
            if time[0] == '2':
                prod = 4
            else:
                prod = 10
        if time[3] == '?':
            prod *= 6
        if time[4] == '?':
            prod *= 10
        return prod


if __name__ == '__main__':
    s = Solution()
    print(s.countTime('?5:00') == 2)
    print(s.countTime('0?:0?') == 100)
    print(s.countTime('??:??') == 1440)
