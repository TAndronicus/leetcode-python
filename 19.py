from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dist, length, pointer, lagging = 0, 0, head, head
    while pointer is not None:
        if dist != n + 1:
            dist += 1
        else:
            lagging = lagging.next
        pointer = pointer.next
        length += 1
    if length == n:
        return head.next
    if n == 1:
        lagging.next = None
    else:
        lagging.next = lagging.next.next
    return head


def assertLists(actual: List, expected: List) -> bool:
    return actual == expected


def toListNode(list: List) -> ListNode:
    head = ListNode(list[0])
    pointer = head
    for i in range(1, len(list)):
        pointer.next = ListNode(list[i])
        pointer = pointer.next
    return head


def fromListNode(listNode: ListNode) -> List:
    res = [listNode.val]
    pointer = listNode
    while pointer.next is not None:
        pointer = pointer.next
        res.append(pointer.val)
    return res


def tLN(list: List) -> ListNode:
    return toListNode(list)


def fLN(listNode: ListNode) -> List:
    return fromListNode(listNode)


if __name__ == '__main__':
    print(assertLists([1, 2, 3, 4], [1, 2, 3, 4]))
    print(not assertLists([1, 2, 3, 4], []))
    print(not assertLists([1, 2, 3, 4], [1, 2, 3]))
    print(assertLists(fromListNode(toListNode([1, 2, 3, 4, 5])), [1, 2, 3, 4, 5]))
    print(assertLists(fLN(removeNthFromEnd(tLN([1, 2, 3, 4, 5]), 5)), [2, 3, 4, 5]))
    print(assertLists(fLN(removeNthFromEnd(tLN([1, 2, 3, 4, 5]), 2)), [1, 2, 3, 5]))
    print(removeNthFromEnd(tLN([1]), 1) is None)
    print(assertLists(fLN(removeNthFromEnd(tLN([1, 2]), 1)), [1]))
