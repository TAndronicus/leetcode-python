from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, o: object) -> bool:
        return o is not None and self.val == o.val and self.left == o.left and self.right == o.right


class Solution1:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        elif len(preorder) == 1:
            return TreeNode(preorder[0])
        else:
            rootVal = preorder[0]
            postorderLeftIndex = postorder.index(preorder[1])
            return TreeNode(rootVal, left=self.constructFromPrePost(preorder[1:postorderLeftIndex + 2], postorder[:postorderLeftIndex + 1]),
                            right=self.constructFromPrePost(preorder[postorderLeftIndex + 2:], postorder[postorderLeftIndex + 1:-1]))


class Solution2:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.postorderIndexes = {}
        for i in range(len(postorder)):
            self.postorderIndexes[postorder[i]] = i
        return self.buildTreeRecursively(preorder, [0, len(preorder)], 0)

    def buildTreeRecursively(self, preorder: List[int], preorderIndexes: List[int], lastPostorderIndex: int):
        if preorderIndexes[0] >= preorderIndexes[1]:
            return None
        elif preorderIndexes[0] + 1 == preorderIndexes[1]:
            return TreeNode(preorder[preorderIndexes[0]])
        else:
            rootVal = preorder[preorderIndexes[0]]
            preorderIndex = self.postorderIndexes[preorder[preorderIndexes[0] + 1]] + lastPostorderIndex
            return TreeNode(rootVal, left=self.buildTreeRecursively(preorder, [preorderIndexes[0] + 1, preorderIndex + 2], lastPostorderIndex + 1),
                            right=self.buildTreeRecursively(preorder, [preorderIndex + 2, preorderIndexes[1]], lastPostorderIndex + 1))


if __name__ == '__main__':
    s1 = Solution1()
    t1 = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    print(s1.constructFromPrePost([3, 9, 20, 15, 7], [9, 15, 7, 20, 3]) == t1)
    t2 = TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3, left=TreeNode(5), right=TreeNode(6, left=TreeNode(7))))
    print(s1.constructFromPrePost([1, 2, 4, 3, 5, 6, 7], [4, 2, 5, 7, 6, 3, 1]) == t2)
    print(s1.constructFromPrePost([-1], [-1]) == TreeNode(-1))
    s2 = Solution2()
    print(s2.constructFromPrePost([3, 9, 20, 15, 7], [9, 15, 7, 20, 3]) == t1)
    print(s2.constructFromPrePost([1, 2, 4, 3, 5, 6, 7], [4, 2, 5, 7, 6, 3, 1]) == t2)
    print(s2.constructFromPrePost([-1], [-1]) == TreeNode(-1))
