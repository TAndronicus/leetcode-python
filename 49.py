from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for str in strs:
            srt = ''.join(sorted(str))
            if res.get(srt) is None:
                res[srt] = [str]
            else:
                res[srt].append(str)
        return res.values()


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(s.groupAnagrams([""]))
