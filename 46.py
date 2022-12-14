from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            queue = []
            for i in range(len(nums)):
                for el in self.permute(nums[:i] + nums[i + 1:]):
                    queue.append([nums[i]] + el)
            return queue


if __name__ == '__main__':
    s = Solution()
    print(list(s.permute([1, 2, 3])))
