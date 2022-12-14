from typing import List


class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        firstStack = []
        secondStack = []
        for i in range(len(nums) - 1, -1, -1):
            assigned = False
            first = False
            while len(firstStack) > 0:
                el = firstStack.pop()
                if el > nums[i]:
                    res[i] = el
                    firstStack.append(el)
                    firstStack.append(nums[i])
                    assigned = True
                    first = True
                else:
                    secondStack.append(el)
            if not assigned:
                res[i] = -1
                firstStack.append(nums[i])
        return res

    def secondGreaterElement2(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        res[-1] = -1
        for i in range(len(nums) - 2, -1, -1):
            first, assigned = False, False
            if nums[i] == nums[i + 1]:
                res[i] = res[i + 1]
            else:
                for j in range(i + 1, len(nums)):
                    if nums[j] > nums[i]:
                        if first:
                            res[i] = nums[j]
                            assigned = True
                            break
                        else:
                            first = True
                if not assigned:
                    res[i] = -1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.secondGreaterElement2([2, 4, 0, 9, 6]))
