from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            queue, used = [], {}
            for i in range(len(nums)):
                if used.get(nums[i]) == 1:
                    continue
                used[nums[i]] = 1
                for el in self.permuteUnique(nums[:i] + nums[i + 1:]):
                    queue.append([nums[i]] + el)
            return queue


if __name__ == '__main__':
    s = Solution()
    print(list(s.permuteUnique([1, 1, 2])))
