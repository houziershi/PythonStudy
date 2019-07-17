# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        head = ListNode(None)
        tail = head

        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    tail.next = ListNode(l1.val)
                    tail = tail.next
                    l1 = l1.next
                else:
                    tail.next = ListNode(l2.val)
                    tail = tail.next
                    l2 = l2.next
            elif l1:
                tail.next = ListNode(l1.val)
                tail = tail.next
                l1 = l1.next
            elif l2:
                tail.next = ListNode(l2.val)
                tail = tail.next
                l2 = l2.next

        return head.next


if __name__ == '__main__':
    print(Solution().mergeTwoLists(ListNode(1), ListNode(2)))
