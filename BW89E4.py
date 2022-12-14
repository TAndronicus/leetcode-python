from typing import List


class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        maxEl, sum = nums[0], 0
        for el in nums:
            maxEl = max(maxEl, el)
            sum += el
        adj = {}
        for edge in edges:
            if edge[0] in adj:
                adj[edge[0]].append(edge[1])
            else:
                adj[edge[0]] = [edge[1]]
            if edge[1] in adj:
                adj[edge[1]].append(edge[0])
            else:
                adj[edge[1]] = [edge[0]]
        for i in range(maxEl, sum):
            q = sum / maxEl
            if q != int(q):
                continue
            adjC, splittable = dict(adj), True
            while len(adjC) > 0:
                if not (self.canCutOff(adjC, nums, i)):
                    splittable = False
                    break
            if splittable:
                return int(q) - 1
        return 0

    def canCutOff(self, adj, nums, sum):
        canCutOff = False
        for vertex, neighbors in adj.items():
            if len(neighbors) == 1 and nums[vertex] <= sum:
                canCutOff = True
                break
        if not (canCutOff):
            return False
        cumSum = nums[vertex]
        del adj[vertex]
        if len(adj[neighbors[0]]) == 1 and len(adj) == 1:
            del adj[neighbors[0]]
        else:
            adj[neighbors[0]].remove(vertex)
        if cumSum == sum:
            return True
        else:
            return self.canCutOff(adj, nums, sum - cumSum)


if __name__ == '__main__':
    s = Solution()
    print(s.componentValue([6, 2, 2, 2, 6], [[0, 1], [1, 2], [1, 3], [3, 4]]))
    print(s.componentValue([8, 2, 2, 2, 6], [[0, 1], [1, 2], [1, 3], [3, 4]]))
    print(s.componentValue([2], []))
    # print(s.componentValue([8, 2, 2, 4, 2, 4, 2], [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5], [5, 6]]))
