from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, o: object) -> bool:
        return o is not None and self.val == o.val and self.left == o.left and self.right == o.right


class Solution1:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        else:
            rootVal = preorder[0]
            inorderIndex = inorder.index(rootVal)
            return TreeNode(rootVal, left=self.buildTree(preorder[1:inorderIndex + 1], inorder[:inorderIndex]),
                            right=self.buildTree(preorder[inorderIndex + 1:], inorder[inorderIndex + 1:]))


class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorderIndexes = {}
        for i in range(len(inorder)):
            self.inorderIndexes[inorder[i]] = i
        return self.buildTreeRecursively(preorder, [0, len(preorder)], 0)

    def buildTreeRecursively(self, preorder: List[int], preorderIndexes: List[int], lastInorderIndex: int):
        if preorderIndexes[0] >= preorderIndexes[1]:
            return None
        else:
            rootVal = preorder[preorderIndexes[0]]
            inorderIndex = self.inorderIndexes[rootVal] + lastInorderIndex
            return TreeNode(rootVal, left=self.buildTreeRecursively(preorder, [preorderIndexes[0] + 1, inorderIndex + 1], lastInorderIndex + 1),
                            right=self.buildTreeRecursively(preorder, [inorderIndex + 1, preorderIndexes[1]], lastInorderIndex))


if __name__ == '__main__':
    s1 = Solution1()
    t1 = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    print(s1.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]) == t1)
    t2 = TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3, left=TreeNode(5), right=TreeNode(6, left=TreeNode(7))))
    print(s1.buildTree([1, 2, 4, 3, 5, 6, 7], [4, 2, 1, 5, 3, 7, 6]) == t2)
    print(s1.buildTree([-1], [-1]) == TreeNode(-1))
    s2 = Solution2()
    print(s2.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]) == t1)
    print(s2.buildTree([1, 2, 4, 3, 5, 6, 7], [4, 2, 1, 5, 3, 7, 6]) == t2)
    print(s2.buildTree([-1], [-1]) == TreeNode(-1))
