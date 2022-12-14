from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, o: object) -> bool:
        return o is not None and self.val == o.val and self.left == o.left and self.right == o.right


class Solution1:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        else:
            rootVal = postorder[-1]
            inorderIndex = inorder.index(rootVal)
            return TreeNode(rootVal, left=self.buildTree(inorder[:inorderIndex], postorder[:inorderIndex]),
                            right=self.buildTree(inorder[inorderIndex + 1:], postorder[inorderIndex:-1]))


class Solution2:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.inorderIndexes = {}
        for i in range(len(inorder)):
            self.inorderIndexes[inorder[i]] = i
        return self.buildTreeRecursively(postorder, [0, len(postorder)], 0)

    def buildTreeRecursively(self, postorder: List[int], postorderIndexes: List[int], lastInorderIndex: int):
        if postorderIndexes[0] >= postorderIndexes[1]:
            return None
        else:
            rootVal = postorder[postorderIndexes[1] - 1]
            inorderIndex = self.inorderIndexes[rootVal] - lastInorderIndex
            return TreeNode(rootVal, left=self.buildTreeRecursively(postorder, [postorderIndexes[0], inorderIndex], lastInorderIndex),
                            right=self.buildTreeRecursively(postorder, [inorderIndex, postorderIndexes[1] - 1], lastInorderIndex + 1))


if __name__ == '__main__':
    s1 = Solution1()
    t1 = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    print(s1.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]) == t1)
    t2 = TreeNode(1, left=TreeNode(2, left=TreeNode(4)), right=TreeNode(3, left=TreeNode(5), right=TreeNode(6, left=TreeNode(7))))
    print(s1.buildTree([4, 2, 1, 5, 3, 7, 6], [4, 2, 5, 7, 6, 3, 1]) == t2)
    print(s1.buildTree([-1], [-1]) == TreeNode(-1))
    s2 = Solution2()
    print(s2.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]) == t1)
    print(s2.buildTree([4, 2, 1, 5, 3, 7, 6], [4, 2, 5, 7, 6, 3, 1]) == t2)
    print(s2.buildTree([-1], [-1]) == TreeNode(-1))
